from  sqlite4  import  SQLite4

class SqliteClient:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None

    def connect(self):
        database = SQLite4(self.db_file)
        self.connection = database.connect(debug = True);

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def execute_query(self, query, parameters=None):
        cursor = self.connection.cursor()
        if parameters is not None:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return result

    def execute_query_single(self, query, parameters=None):
        cursor = self.connection.cursor()
        if parameters is not None:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        self.connection.commit()
        return result

    def execute_insert(self, query, parameters=None):
        cursor = self.connection.cursor()
        if parameters is not None:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        result = cursor.lastrowid
        cursor.close()
        self.connection.commit()
        return result
