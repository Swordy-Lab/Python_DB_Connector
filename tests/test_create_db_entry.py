import os
from simple_db_connector import database
import decimal
import datetime


# Call the database class
db = database(
    os.environ["db_url"],
    os.environ["db_user"],
    os.environ["db_password"],
    os.environ["db_port"],
    os.environ["db_name"],
)

# Example Table Name 
table_name =  "cars_table"  

# Example Table Content
table_content = {
	"manufacture" : "toyoat",
	"model" : "Aygo X yalp",
	"ps" : 72, 
} 

# Example Table prime key
prime_key = "id"
# To illustrate this, I have entered "id". However, if "prime_key" is empty, "id" is selected.

# Example 
db.create_db_entry(table_name, table_content, prime_key)