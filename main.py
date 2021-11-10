from typing import Optional

from fastapi import FastAPI
from ldap3 import Server, Connection, ALL

from constants import LDAP_SERVER_HOST, LDAP_SERVER_PORT, LDAP_ROOT_USER, LDAP_ROOT_PASSWORD

server = Server(host=LDAP_SERVER_HOST, port=LDAP_SERVER_PORT, get_info=ALL)
conn = Connection(server, user=LDAP_ROOT_USER, password=LDAP_ROOT_PASSWORD, auto_bind=True, auto_referrals=False)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/connection/check/')
def check_connection():
    conn.bind()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
