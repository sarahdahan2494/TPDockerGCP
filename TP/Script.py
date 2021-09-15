import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM persons")
myresult=mycursor.fetchall()

for x in mycursor:
    print(x)