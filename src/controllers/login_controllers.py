import sqlite3
import bcrypt

from ..data.database import create_user, user_exists, authenticate_user

# Conectar ao banco de dados
DB_PATH = "users.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Criação da tabela de usuários, se ainda não existir
cursor.execute(
"""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    level TEXT
)
""")
conn.commit()

def get_db_connection():
    """Cria e retorna uma nova conexão SQLite para evitar problemas de thread."""
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def hash_password(password):
    """Gera um hash seguro para a senha usando bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(username, password):
    """Verifica a senha do usuário no banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()

    conn.close()
    
    if row:
        return bcrypt.checkpw(password.encode(), row[0].encode())
    return False
    
# Criando um usuário com o máximo de permissões
if not user_exists("admin"):
    create_user("admin", "2y6J#UhBUrEKt*6", 1)

# # Criando um usuário com o máximo de permissões
# register_user("anot", "5nDpgG#PBad!nRE", "Anotador")