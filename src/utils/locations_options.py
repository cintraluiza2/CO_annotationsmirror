"""Utilitarios para campos dependentes de pais e estado/provincia."""

from functools import lru_cache
import re
import unicodedata

import pycountry
from babel import Locale


_PT_BR = Locale.parse("pt_BR")


def _normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(char for char in value if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]", "", value.casefold())


# Nomes que podem divergir entre o dominio do banco, Babel e ISO 3166.
_COUNTRY_ALIASES = {
    "bolivia": "BO",
    "brasil": "BR",
    "colombia": "CO",
    "coreiadosul": "KR",
    "costarica": "CR",
    "equador": "EC",
    "estadosunidos": "US",
    "haiti": "HT",
    "mexico": "MX",
    "nicaragua": "NI",
    "panama": "PA",
    "paraguai": "PY",
    "peru": "PE",
    "republicadominicana": "DO",
    "uruguai": "UY",
    "venezuela": "VE",
}


@lru_cache(maxsize=1)
def _country_name_index() -> dict[str, str]:
    index: dict[str, str] = dict(_COUNTRY_ALIASES)

    for country in pycountry.countries:
        alpha_2 = country.alpha_2
        names = {
            country.name,
            getattr(country, "official_name", ""),
            getattr(country, "common_name", ""),
            _PT_BR.territories.get(alpha_2, ""),
        }
        for name in names:
            if name:
                index[_normalize(name)] = alpha_2

    return index


def country_code(country_name: str | None) -> str | None:
    """Converte o nome exibido do pais em codigo ISO alpha-2."""
    if not country_name:
        return None
    return _country_name_index().get(_normalize(country_name))


@lru_cache(maxsize=256)
def subdivisions_for_country(country_name: str | None) -> list[str]:
    """Retorna estados, provincias ou departamentos ISO do pais informado."""
    code = country_code(country_name)
    if not code:
        return []

    subdivisions = list(pycountry.subdivisions.get(country_code=code) or [])
    subdivisions.sort(key=lambda item: item.name.casefold())

    # Mantem siglas para o Brasil, preservando o formato ja salvo no banco.
    if code == "BR":
        return [item.code.split("-", 1)[1] for item in subdivisions]

    return [item.name for item in subdivisions]
