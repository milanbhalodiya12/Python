# # Python Database 

# #Python Database Connection
# import mysql.connector
# mydb= mysql.connector.connect(host = 'localhost', user='root',password = '')
# print(mydb)






# #Creating Database

# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="")
# mycursor=mydb.cursor()
# mycursor.execute('create database mypy')




# # Showing the list of database

# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
# mycursor=mydb.cursor()
# mycursor.execute('show databases')
# for i in mycursor:
#     print(i)



# # Creating the Table
# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
# mycursor=mydb.cursor()
# mycursor.execute('create table stud (name varchar(50), roll_no int)')



# # Inserting into database

# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
# mycursor = mydb.cursor()
# sql = "INSERT INTO STUD (name , roll_no) VALUES (%s, %s)"
# val = [("Milan ","04"),
#        ("Vishal","29"),
#        ("Krushal","32"),
#        ("Khan","23"),
#        ("Paras","42"),
#        ("Rahul","20")]
# mycursor.executemany(sql,val)
# mydb.commit()



# # Showing data
# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
# mycursor = mydb.cursor()
# mycursor.execute('select * from stud')
# myresut=mycursor.fetchall()
# for i in myresut:
#     print(i)



# # Updating the data

# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
# mycursor = mydb.cursor()
# mycursor.execute('update stud set name ="Prince" where roll_no = 23')
# mydb.commit()
# mydb.close()



# # Delete a Record

# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
# mycursor = mydb.cursor()
# mycursor.execute('delete from stud where roll_no = 42')
# mydb.commit()
# mydb.close()



# CRUD OPERATION INT SQL LITE DATABASE

# import sqlite3
# cnt = sqlite3.connect('mydb.dp')

# Creating the Table

# cnt.execute('create table student(roll int , name varchar(255))')
# print('Table created successfully')

# Inserting into Table

# cnt.execute('insert into student values (1,"Milan")')
# print("Record inserted successfully")
# cnt.commit()

# Showing the database

# a=cnt.execute('select * from student ')
# for i in a:
#     print(i)


# Updateing the record in the Table

# cnt.execute('update student set name= "Prince" where roll = 1')
# cnt.commit()


# Deleting the records from the database

# cnt.execute('delete from student where roll = 1')
# cnt.commit()