import mysql.connector
# mysql connection 
connection = mysql.connector.connect(
    host="bannerbuzz246-db-1",
    user="root",
    password="root123",
    database="my-salon"
)
# cursor for query with database
cursor = connection.cursor()

#query = "SELECT * FROM users WHERE 1"
cursor.execute("SELECT * FROM voters WHERE 1")
users = cursor.fetchall()


for row in users:
    #print(row)

cursor.close()
connection.close()

