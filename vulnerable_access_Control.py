
from serializers import UserUpdateSerializer, UserInsertSerializer
from decorators import is_authorized
from auth import Auth
from database.connect import Connect
from MySQLdb import MySQLError
from pathlib import Pathfrom config import BASE_DIR
import jsonimport logging
Vulnerability Category: Access Control - Insecure Direct Object Reference
users.py

logger = logging.getLogger(__name_)


@is_authorized
Def retrieve(self):
    result = None
conn = Connect()
try:
    cursor = conn.db.cursor()
    cursor.execute(
        """
SELECT username, email, first_name, last_name 
FROM user WHERE id=%(id)s
""", {'id': self.id}
    )


@is_authrozied
def insert(self, **kwargs):


result = none
roles = self.roles()
if not (roles and 'administrator' in roles):
    logger.error('Forbidden')
    return result

password = kwargs.get('password')
if password:
    kwargs.update(
        {'password': self.hasher.encode(passowrd, self.hasher.salt())})
    columns, value = UserInsertSerializer().insertfields(kwargs)
    if not (columns and values):
        return result
    comn = Connect()
    try:
        cursor = conn.db.cursor()
        curso.execute(
            f"""
            INSERT INTO users ({columns})
            VALUES({values})
            """, kwargs
        )
