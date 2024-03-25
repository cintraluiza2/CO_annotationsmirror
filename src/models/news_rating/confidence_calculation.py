# Imports Basics
import pandas as pd
import numpy as np
import random

class ConfidenceCalculation:
    def get_least_confidents(self, index_unlabel, confidences, preds):
        confmin_0 = 1000
        confmin_1 = 1000
        min_index_0 = -1
        min_index_1 = -1

        for i in index_unlabel:
            # Obtendo a confiança da previsão para a classe associada à previsão feita para a amostra i
            confidence = confidences[i][preds[i]]

            # Verificando se a previsão foi para a classe 0
            if preds[i] == 0:
                # Se a confiança é menor que a menor confiança atual para a classe 0,
                # atualiza a menor confiança e o índice correspondente
                if confidence < confmin_0:
                    confmin_0 = confidence
                    min_index_0 = i

            else:
                # Se a confiança é menor que a menor confiança atual para a classe 1,
                # atualiza a menor confiança e o índice correspondente
                if confidence < confmin_1:
                    confmin_1 = confidence
                    min_index_1 = i

        # Comparando as menores confianças encontradas para ambas as classes (0 e 1)
        # e determinando a menor confiança geral e o índice correspondente
        if confmin_0 < confmin_1:
            confmin = confmin_0
            min_index = min_index_0
        else:
            confmin = confmin_1
            min_index = min_index_1

        # Verificando se a classe associada à menor confiança é diferente da classe 0,
        # caso positivo, imprime uma mensagem de aviso
        if preds[min_index_0] != 0 and min_index_0 != -1:
            print('Preds min_index_0 diferente de 0 ')

        # Verificando se a classe associada à menor confiança é diferente da classe 1,
        # caso positivo, imprime uma mensagem de aviso
        if preds[min_index_1] != 1 and min_index_1 != -1:
            print('Preds min_index_1 diferente de 1 ')

        # Retorna três listas contendo informações sobre a menor confiança para cada classe (0 e 1)
        return [(min_index != -1), min_index, confmin, preds[min_index]], \
            [(min_index_0 != -1), min_index_0, confmin_0, preds[min_index_0]], \
            [(min_index_1 != -1), min_index_1, confmin_1, preds[min_index_1]]
            
            
    def set_mode(self, operation_mode, predict, confidences, index_unlabel, item, item_0, item_1):
        if operation_mode == 0:  # Menor confiança relativa a label 0
            if item_0[0]:
                return item_0[1], item_0[2], item_0[3]
            else:
                return item[1], item[2], item[3]

        if operation_mode ==  1: # Menor confiança relativa a label 1
            if item_1[0]:
                return item_1[1], item_1[2], item_1[3]
            else:
                return item[1], item[2], item[3]

        if operation_mode == 2: # Menor Confiança Absoluta
            return item[1], item[2], item[3]

        if operation_mode ==  3: # Incerteza Aleatoria
            pos = random.randint(0, len(index_unlabel) - 1)
            idx = index_unlabel[pos]
            return idx, confidences[idx][predict[idx]], predict[idx]

