# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 13:05:46 2018

@author: Akash
"""

import sqlite3

def createConn():
    # sqlite3.connect connects to database name if such database exist and if doesn't exist,
    # it creates a database by that name and then connects to it.
    connection = sqlite3.connect("BloodDatabase.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS donor (id INTEGER PRIMARY KEY,Name TEXT,BloodGroup Text,City Text,Contact integer)")
    connection.commit()
    connection.close()
    
def insertTable(name,bloodgroup,city,contact):
    connection = sqlite3.connect("BloodDatabase.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO donor VALUES (NULL,?,?,?,?)",(name,bloodgroup,city,contact))
    connection.commit()
    connection.close()
   
def show():
    connection = sqlite3.connect("BloodDatabase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM donor")
    databaseValue = cursor.fetchall()           # cursor.fetchall() to fetch all the data from table to python variable
    connection.close()
    return databaseValue

def delete(id):
    connection = sqlite3.connect("BloodDatabase.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM donor WHERE id=?",(id,))
    connection.commit()
    connection.close()

def updateTable(id,name,bloodgroup,city,contact):
    connection = sqlite3.connect("BloodDatabase.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE donor SET name=?,bloodgroup=?,city=?,contact=? WHERE id=?",(name,bloodgroup,city,contact,id))
    connection.commit()
    connection.close()
   
def search(name="",bloodgroup="",city="",contact=""):
    connection = sqlite3.connect("BloodDatabase.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  donor WHERE name=? OR bloodgroup=? OR City=? OR Contact=?",(name,bloodgroup,city,contact))
    databaseValue = cursor.fetchall()           # cursor.fetchall() to fetch all the data from table to python variable
    connection.commit()
    connection.close()
    return databaseValue
   

createConn()
#insertTable("Akash Tyagi","O+","Noida",7579212810)
#insertTable("Amit","AB+","Delhi",9999415785)
#insertTable("David","B+","Pune",9000415785) 
#print(search(name="Madhu Tyagi"))
#delete(2)
updateTable(8,"Madhu Tyagi","O-","Banglore",242424) 
#print("Search Result: ",search(city="Noida"))
#print("All: ",show())
#updateTable("TVS",80000,"Apache180")
