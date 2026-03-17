import contextlib
import os

import psycopg2

from factories.boroughs import create_boroughs_repo, create_boroughs_service
from factories.pt import create_pt_repo, create_pt_service


@contextlib.contextmanager
def get_db_conn():
    conn = None
    try:
        conn = psycopg2.connect(database=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PWD"))
        yield conn
    finally:
        if conn is not None:
            conn.close()


def get_pt_service(func):
    def wrapper(*args, **kwargs):
        with get_db_conn() as conn:
            repo = create_pt_repo(conn)
            service = create_pt_service(repo)
            return func(service, *args, **kwargs)

    return wrapper


def get_boroughs_service(func):
    def wrapper(*args, **kwargs):
        with get_db_conn() as conn:
            repo = create_boroughs_repo(conn)
            service = create_boroughs_service(repo)
            return func(service, *args, **kwargs)

    return wrapper
