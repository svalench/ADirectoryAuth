import os
from dotenv import load_dotenv

load_dotenv()

LDAP_SERVER_HOST = os.getenv('LDAP_SERVER_HOST')
LDAP_SERVER_PORT = os.getenv('LDAP_SERVER_PORT')
