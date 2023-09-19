import os
from src.infra.db.clients.sqlite_client import SqliteClient

class UserIdentityRepository:
    def __init__(self):
        db_file = os.path.abspath(
            "./src/infra/db/database/database.db")
        self.client = SqliteClient(db_file)       

    def authenticate(self, username, password):
        query = "SELECT id FROM users WHERE username = ? AND password = ?"
        parameters = (username, password)
        self.client.connect()
        result = self.client.execute_query_single(query, parameters)
        self.client.disconnect()
        return result

    def create(self, username, password, email):
        query = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)"
        parameters = (username, password, email)
        self.client.connect()
        result = self.client.execute_query(query, parameters)
        self.client.disconnect()
        return result

    def get_by_username_or_email(self, username, email):
        query = "SELECT id FROM users WHERE username = ? OR email = ?"
        parameters = (username, email)
        self.client.connect()
        result = self.client.execute_query_single(query, parameters)
        self.client.disconnect()
        return result
