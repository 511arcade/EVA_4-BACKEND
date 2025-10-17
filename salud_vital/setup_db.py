"""
Script de inicialización de PostgreSQL para crear el rol "Felipe" y la BD "salud_vital".
Usa psycopg3 y se conecta como superusuario 'postgres' con la contraseña proporcionada.
Edita POSTGRES_SUPERUSER si tu admin no es 'postgres'.
"""
import os
import sys
import psycopg
from psycopg import sql

POSTGRES_HOST = os.getenv("DB_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("DB_PORT", "5432"))
POSTGRES_SUPERUSER = os.getenv("PG_SUPERUSER", "postgres")
POSTGRES_SUPERPASS = os.getenv("PG_SUPERPASS") or "20708Fel-"

TARGET_ROLE = os.getenv("DB_USER", "Felipe")
TARGET_PASS = os.getenv("DB_PASSWORD", "20708Fel-")
TARGET_DB = os.getenv("DB_NAME", "salud_vital")

if not POSTGRES_SUPERPASS:
    print("ERROR: Debes definir la contraseña del superusuario de PostgreSQL en la variable de entorno PG_SUPERPASS.")
    sys.exit(1)

try:
    with psycopg.connect(dbname="postgres", user=POSTGRES_SUPERUSER, password=POSTGRES_SUPERPASS,
                         host=POSTGRES_HOST, port=POSTGRES_PORT, autocommit=True) as conn:
        with conn.cursor() as cur:
            # Crear rol si no existe
            cur.execute("SELECT 1 FROM pg_roles WHERE rolname=%s", (TARGET_ROLE,))
            if not cur.fetchone():
                cur.execute(
                    sql.SQL('CREATE ROLE {} WITH LOGIN PASSWORD {}').format(
                        sql.Identifier(TARGET_ROLE), sql.Literal(TARGET_PASS)
                    )
                )
                print(f"Rol '{TARGET_ROLE}' creado.")
            else:
                # Asegurar contraseña por si cambió
                cur.execute(
                    sql.SQL('ALTER ROLE {} WITH PASSWORD {}').format(
                        sql.Identifier(TARGET_ROLE), sql.Literal(TARGET_PASS)
                    )
                )
                print(f"Rol '{TARGET_ROLE}' ya existía. Contraseña actualizada.")
            # Otorgar CREATEDB (opcional)
            cur.execute(sql.SQL('ALTER ROLE {} CREATEDB').format(sql.Identifier(TARGET_ROLE)))

            # Crear BD si no existe
            cur.execute("SELECT 1 FROM pg_database WHERE datname=%s", (TARGET_DB,))
            if not cur.fetchone():
                cur.execute(
                    sql.SQL('CREATE DATABASE {} OWNER {}').format(
                        sql.Identifier(TARGET_DB), sql.Identifier(TARGET_ROLE)
                    )
                )
                print(f"Base de datos '{TARGET_DB}' creada y asignada a '{TARGET_ROLE}'.")
            else:
                print(f"Base de datos '{TARGET_DB}' ya existe.")

    print("Inicialización de PostgreSQL completada.")
except Exception as e:
    print("Error inicializando PostgreSQL:", e)
    sys.exit(2)
