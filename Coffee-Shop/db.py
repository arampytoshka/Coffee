import mysql.connector
from mysql.connector import Error

class DB:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        last_id = None
        try:
            self.cursor.execute(query)
            self.connection.commit()
            last_id = self.cursor.lastrowid
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
            exit()
        return last_id

    def execute_read_query(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            exit()

    def __del__(self):
        self.connection.close()
