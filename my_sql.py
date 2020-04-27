import mysql.connector

mydb = mysql.connector.connect(
  user='username', 
  password='password',
  host='127.0.0.1',
  database='pythondb',
  auth_plugin='mysql_native_password',
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE planets (name VARCHAR(255), daysAroundSun INT)")

# Insert
sql = "INSERT INTO planets (name, daysAroundSun) VALUES ('{}', {})".format("Mercúrio", 88)
mycursor.execute(sql)
mydb.commit()

# Select
mycursor.execute("SELECT * FROM planets")
myresult = mycursor.fetchall()
print(myresult)

# Select with condition
sql = "SELECT * FROM planets WHERE name = 'Mercúrio'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
mydb.commit()
print(myresult)

# Update
sql = "UPDATE planets SET name = '{}' WHERE name = '{}'".format('Terra', 'Mercúrio')
mycursor.execute(sql)
mydb.commit()

# Delete
sql = "DELETE FROM planets WHERE name = 'Terra'"
mycursor.execute(sql)
mydb.commit()
print('Planet removed!')
