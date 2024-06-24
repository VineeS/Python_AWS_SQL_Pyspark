import unittest
from mockito import mock, when, unstub
from database_handler import DatabaseHandler

class TestDatabaseHandler(unittest.TestCase):
    def setUp(self):
        self.db_handler = mock(DatabaseHandler)
        self.connection_mock = mock
        when(self.db_handler).create_connection().thenReturn(None)
        when(self.db_handler).close_connection().thenReturn(None)
        when(self.db_handler).execute_query(...).thenReturn(self.connection_mock)

    def tearDown(self):
        unstub()

    def test_create_connection(self):
        self.db_handler.create_connection()
        when(self.db_handler).create_connection().thenReturn(None)
        self.db_handler.create_connection()

    def test_execute_query(self):
        query = "INSERT INTO users (name, age) VALUES (?, ?)"
        params = ("John Doe", 32)
        when(self.db_handler).execute_query(query,params).thenReturn(None)
        self.db_handler.execute_query(query,params)
        when(self.db_handler).execute_query(query,params).thenReturn(None)

    def test_fetch_all(self):
        query = "SELECT * FROM users"
        expected_result = [(1,"John Doe", 32),(2,"James Smith", 49)]
        when(self.db_handler).fetch_all(query).thenReturn(expected_result)
        result = self.db_handler.fetch_all(query)
        self.assertEqual(result,expected_result)

    def test_fetch_one(self):
        query = "SELECT * from users where name = ?"
        params = ("John Doe",)
        except_result = (1,"John Doe", 32)
        when(self.db_handler).fetch_one(query,params).thenReturn(except_result)
        result = self.db_handler.fetch_one(query,params)
        self.assertEqual(result,except_result)
        
if __name__ == '__main__':
    unittest.main()