import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
students = csv.DictReader(open('peeps.csv'))
courses = csv.DictReader(open('courses.csv'))


#command = "" #put SQL statement in this string
#c.execute(command)    #run SQL statement

studentTable = 'CREATE TABLE students(name TEXT, age INTEGER, id INTEGER);'
c.execute(studentTable)

courseTable = 'CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);'
c.execute(courseTable)

for row in students:
    addStudent = 'INSERT INTO students VALUES (?,?,?)', [row['name'], row['age'], row['id']]
    c.execute(addStudent)

for row in courses:
    addCourse = 'INSERT INTO courses VALUES (?,?,?)', [row['code'], row['mark'], row['id']]
    c.execute(addCourse)


#==========================================================
db.commit() #save changes
db.close()  #close database
