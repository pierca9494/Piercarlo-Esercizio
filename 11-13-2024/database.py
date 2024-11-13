import mysql.connector
 
mydb = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7744325",
    password="9EDVDBCxZU",
    database="sql7744325"  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace with your database name  # Replace
    
)


mycursor = mydb.cursor()

query = "SELECT * FROM customers"



# query = "show databases"
# mycursor.execute(query)
# for x in mycursor:
#  print(x)


