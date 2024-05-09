import os

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os. getenv("DB_PORT")
DB_USER = os. getenv("DB_USER")
DB_NAME = os. getenv("DB_NAME")
DB_PASSWORD = os. getenv("DB_PASSWORD")
DB_DRIVER = os. getenv("DB_DRIVER")
DB_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

AUTH_SERVICE = os.getenv("AUTH_SERVICE")

TIMEZONE = os.getenv("TIMEZONE")