from database_handler import DatabaseHandler
print(".. run1 DatabaseHandler created")
db_handler = DatabaseHandler('example.db')
print(".. run2 'example.db' added ")

# create a connection
db_handler.create_connection()
print(".. run3 create a connection")

# create table 
create_table_query = """
CREATE TABLE IF NOT EXISTS users  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
    );
    """

print(create_table_query)

# execute query 
db_handler.execute_query(create_table_query)

### Insert records 
insert_query = "INSERT INTO users (name, age) VALUES (?, ?)"
db_handler.execute_query(insert_query,("John Doe", 32))
db_handler.execute_query(insert_query,("James Smith", 49))

### Fetch all records
select_all_query = "SELECT * FROM users"
user = db_handler.fetch_all(select_all_query)
print(user)

### Fetch one record
fetch_one_record = """SELECT * FROM users where id = (?)"""
user = db_handler.fetch_one(fetch_one_record, (1,))
print(user)