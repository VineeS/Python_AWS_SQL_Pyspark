import sqlite3
from sqlite3 import Error

class DatabaseHandler:
    def __init__(self,db_file):
        self.db_file = db_file
        self.connection = None

    def create_connection(self):
        """Create a database connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_file)
            print(f"Connected to database {self.db_file}")
        except Error as e:
            print(e)

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print(f"Closed connection to database {self.db_file}")

    def execute_query(self, query, params=None):
        """Execute a single query."""
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor

        except Error as e:
            print(f"Error: '{e}' occurred")
            return None
        
    def fetch_all(self, query, params=None):
        """Fetch all results from a query."""
        cursor = self.execute_query(query, params)
        if cursor:
            return cursor.fetchall()
        return None
    
    def fetch_one(self,  query, params=None):
        """Fetch one result from a query."""

        cursor = self.execute_query(query,params)
        if cursor:
            return cursor.fetchone()

        return None




            