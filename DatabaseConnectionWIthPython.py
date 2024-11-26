import mysql.connector


# Create Database
db = mysql.connector.connect(host = "localhost", user = "root" , passwd = "Sqlroot@9990")

# Cursor object
cur = db.cursor()
