# database.py
class DatabaseHandler:
    def __init__(self, connection_string):
        # Assume some initialization with connection string
        pass

    def get_user_by_id(self, user_id):
        # This method interacts with the database to get user data
        query = f"SELECT * FROM users WHERE id = {user_id}"
        # Here you would normally execute the query and fetch the result
        result = self.execute_query(query)
        return result

    def execute_query(self, query):
        # This method would contain logic to execute a query
        pass

# get the database handler as an input pull data from database : 
# 2 mocking inputs one is the databse handler when you are writing 
# test case you wont be directly connecting to the database but mocking 
# this scenario
# and 2nd one is the response from the databse also needs to mocked . 
# How will you use the mocking libraries (look for some use case and 
# understand the scenario)
