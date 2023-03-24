import json
import mysql.connector as connection
import os


# Open JSON files with data
with open ('students.json', 'r') as file_1, open ('rooms.json', 'r') as file_2:
    students = json.load(file_1)
    rooms = json.load(file_2)

# Make a connection to database and cursor
password = os.environ.get('PASSWORD_FOR_PYTHON_INTRO')
con_to_db = connection.connect(user='alexander',
                               password=password,
                               host='localhost',
                               database='python_intro')
cursor = con_to_db.cursor()

# Filling the rooms table
for room in rooms:
    sql_query_rooms = 'INSERT INTO rooms (id, name) VALUES (%s, %s)'
    values_for_fill_rooms = (room['id'],
                             room['name'])
    cursor.execute(sql_query_rooms, values_for_fill_rooms)

# Filling the students table
for student in students:
    sql_query_students = 'INSERT INTO students (id, name, birthday, sex, room) VALUES (%s, %s, %s, %s, %s)'
    values_for_fill_students = (student['id'],
                                student['name'],
                                student['birthday'],
                                student['sex'],
                                student['room'])
    cursor.execute(sql_query_students, values_for_fill_students)

# Commiting and closing connections
con_to_db.commit()
cursor.close()
con_to_db.close()