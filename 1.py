# a=[]
# n=int(input("How many elements you want to enter? "))
# for i in range(n):
#     print("Enter an element : ",end = "")
#     a.append(int(input()))
# print("The element of list are :",a)
# find = int(input("Enter an element to count :"))
# cnt = 0
# for i in a:
#     if(find  == i):
#         cnt = cnt + 1
# print("{} is found {} times ." .format(find, cnt))



# name_object = ['Lotus','Mango','Mustang GT']
# category = ['Flower' ,'Fruit','Cars']
# a=zip(category,name_object)
# d1=dict(a)
# print(d1)



# marks={}
# print("How many subject you want to enter?",end = "")
# n = int(input())
# for i in range(n):
#     print("Enter Subject :",end="")
#     key = input()
#     print("Enter Marks :",end="")
#     values = int(input())
#     marks.update({key:values})
# print("Subject and respective marks are :",marks)
# total = sum(marks.values())
# print("Total marks ", total)



# dic= {'eid':101,'name':'ABC','dept':'MCA','sal':1000}
# print(dic)
# dic1=dic.copy()
# print(dic1)
# a=dic.values()
# print(a)
# a=dic.keys()
# print(a)
# print(dic.get('sal'))



# x= lambda a,b:a+b
# print(x(2,7))



# def sum(a,b):
#     ans=a+b
#     print(ans)
# sum(10,85)



# def sum(a,b):
#     ans=a+b
#     return ans
# a= sum(10,85)
# print (a)



# def num(a):
#     if a % 2==0:
#         print("The number is Even")
#     else :
#         print("The number is Odd")
# num(69)



# def arith(a,b):
#     add = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return add, div, mul, sub



# x=int(input("Enter the number 1 : "))
# b=int(input("Enter the number 2 : "))
# a,s,d,m = arith(x,b)
# print("The Addition of two number is : ",a)
# print("The Subtraction of two number is : ",s)
# print("The division of two number is : ",d)
# print("The Multiplication of two number is : ",m)



# def mod(a):
#     a=9
#     print("The value is ",id(a))



# a=9
# mod(a)    
# print("The value of outer function a is : ",id(a))



# def conc(s1,s2):
#     s3=s1+s2
#     print(s3)



# conc("Atmiya" ,"University")
# conc("University","Atmiya")
# conc("University")



# def emp(eid,name='Milan'):
#     print("The id number is :",eid)
#     print("The name is :",name)
    
    
    
# emp(eid=101,name="Milan")
# emp(eid=105,name="Vishal")
# emp(eid=105)



# sqr = lambda a:a*a
# a=int(input("Entre the number you want to find square : "))
# print("The Square of the number is : ",sqr(a))



# f = open("example.txt","w")
# str = input("Enter the string you want to add :")
# f.write(str)
# f.close()



# f = open("example.txt","r")
# str = f.read()
# print(str)
# f.close()



# f=open("example.txt","a")
# str = input("Enter the string you want to add :")
# f.write(str)
# f.close()



# import os 
# fname = input("Enter the name of the file tp open : ")
# if os.path.isfile(fname):
#     f=open(fname,'r')
#     str = f.read()
#     print(str)
# else:
#     print("The file does not exists")






# f= open('download.png','rb')
# f1= open('atmiya.png','wb')
# img = f.read()
# f1.write(img)
# f.close()
# f1.close()









# from zipfile import *
# f=ZipFile('demo1.zip','w','ZIP_DEFLATED')
# f.write("atmiya.png")
# f.write("download.png")
# f.close()


# from zipfile import *
# z=ZipFile('demo1.zip','r')
# z.extractall('D:')



# Retrive the word having 3,4,5 characters

# import re
# str1="sun mon tues wedn thurs frida saturday"
# result = re.findall(r'\b\w{3,5}\b',str1)
# print(result)




# import re
# str1="Hello my name is Milan Bhalodiya. I am Studing in Atmiya University"
# result = re.findall(r'\b\w{4,}\b',str1)
# print(result)



# import re
# str1="onr 2 6 85 "
# result = re.findall(r'\b\d{2}\b',str1)
# print(result)





# import re
# str1="onr 2 6 85  +895 6565 95265 "
# result = re.findall(r'\b\d{2,}\b',str1)
# print(result)





# import re
# str1="Hello my name is Milan Bhalodiya. I am studing in Atmiya University stars"
# result = re.findall(r's[\w]\Z',str1)
# print(result)




#  1.
# import os
# f=open('sample.txt','w')
# str1 = input("Enter the data")
# f.write(str1)
# f.close()


# 2.
# f=open('sample.txt','r')
# str1=f.read()
# print(str1)
# f.close()




# 3.
# f= open('sample.txt','a')
# str1=input("Enter the data : ")
# while str1 !='$':
#     if(str1 !='$'):
#         f.write(str1)
#         break
# f.close()


# 4.Accept the file name from the user, check the availability of the file: i). If the file exists display
# the data on the screen, ii). If the file is not available, display the appropriate message.
# import os
# fname=input("Enter the file name : ")
# if os.path.isfile(fname):
#     f=open(fname,'r')
#     str = f.read()
#     print(str)
#     f.close()
# else : 
#     print("The file does not Exist.")


# 5. Accept the file name from the user, check the availability of the file:
# a. If the file exists, display: i). No. of characters, ii). No. of words and iii). No. of lines
# b. If the file does exist, than display the appropriate message.

# import os
# fname=input("Enter the file name : ")
# if os.path.isfile(fname):
#     f=open(fname,'r')
# else : 
#     print("The file does not Exist.")
# cl = cw = cc = 0
# for line in f:
#     words = line.split()
#     cl = cl+1
#     cw = cw+len(words)
#     cc = cc+len(line)
# print('Number of Lines is : ',cl)
# print('Number of Words is : ',cw)
# print('Number of Characters is : ',cc)
# f.close()



# 6. Create and open the binary file with ‘with’ option. Store names of all the subjects you study in
# semester 2. Ask user to enter the subject number they wanted to see and display that subject
# name.






#Python Database Connection
import mysql.connector
mydb= mysql.connector.connect(host = 'localhost', user='root',password = '')
print(mydb)






#Creating Database

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="")
mycursor=mydb.cursor()
mycursor.execute('create database mypy')




# Showing the list of database

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
mycursor=mydb.cursor()
mycursor.execute('show databases')
for i in mycursor:
    print(i)



# Creatint the Table
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
mycursor=mydb.cursor()
mycursor.execute('create table stud (name varchar(50), roll_no int)')



# Inserting into database

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
mycursor = mydb.cursor()
sql = "INSERT INTO STUD (name , roll_no) VALUES (%s, %s)"
val = [("Milan ","04"),
       ("Vishal","29"),
       ("Krushal","32"),
       ("Khan","23"),
       ("Paras","42"),
       ("Rahul","20")]

mycursor.executemany(sql,val)
mydb.commit()



# Showing data
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
mycursor = mydb.cursor()
mycursor.execute('select * from stud')
myresut=mycursor.fetchall()
for i in myresut:
    print(i)



# Updating the data

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
mycursor = mydb.cursor()
mycursor.execute('update stud set name ="Prince" where roll_no = 23')
mydb.commit()
mydb.close()



# Delete a Record

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mypy")
mycursor = mydb.cursor()
mycursor.execute('delete from stud where roll_no = 42')
mydb.commit()
mydb.close()