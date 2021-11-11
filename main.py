from typing import Optional

from fastapi import FastAPI
from ldap3 import Server, Connection, ALL, NTLM
from ldap3.core.exceptions import LDAPException

from constants import LDAP_SERVER_HOST, LDAP_SERVER_PORT

server = Server(host=LDAP_SERVER_HOST, port=int(LDAP_SERVER_PORT), get_info=ALL)
app = FastAPI()


@app.get("/")
def read_root():
    return {"myName": "сервис Active Directory"}


@app.get('/check/user/{username}/{password}')
def check_connection(username: str, password: str) -> dict:
    return {"status": _ldap_login(username, password), "username": username}


def _ldap_login(username, password):
    """проверка пользователя в LDAP"""
    try:
        with Connection(server, user=username, password=password) as conn:
            print(conn.result["description"])
            return True
    except LDAPException:
        print('Нет соединения с LDAP server')
        return False
