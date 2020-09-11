# -----------------------------------------------------------
# Desktop Application back-end
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

import sqlite3

def connect():
    conn=sqlite3.connect("student_database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(name text,roll INTEGER PRIMARY KEY,section text,country text)")
    conn.commit()
    conn.close()

def insert(name,roll,section,country):
    conn=sqlite3.connect("student_database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO student VALUES (?,?,?,?)",(name,roll,section,country))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("student_database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    conn.commit()
    return rows
    conn.close()

def search(name="",roll="",section="",country=""):
    conn=sqlite3.connect("student_database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student WHERE name=? OR roll=? OR section=? OR country=?",(name,roll,section,country))
    rows=cur.fetchall()
    conn.commit()
    return rows
    conn.close()

def delete(id):
    conn=sqlite3.connect("student_database.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM student WHERE roll=?",(id,))
    conn.commit()
    conn.close()


def update(id,name,roll,section,country):
    conn=sqlite3.connect("student_database.db")
    cur=conn.cursor()
    cur.execute("UPDATE student SET name=?, roll=?, section=?, country=? WHERE roll=?",(name,roll,section,country,id))
    conn.commit()
    conn.close()

#Create database if doesn't exist and connect to it.
connect()

