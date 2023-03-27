import mysql.connector as connection


class RoomRepository:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def connect(self):
        # Make a connection
        self.db_connect = connection.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            database = self.database
        )

    def disconnect(self):
        # Make a disconnection
        self.db_connect.close()

    def get_rooms_with_num_students(self):
        '''Connect to database and return all rooms and number of students
        in that rooms'''
        self.connect()
        cursor = self.db_connect.cursor()

        sql_query = 'SELECT rooms.name, COUNT(students.id) as number_of_students ' \
                    'FROM rooms ' \
                    'INNER JOIN students ON rooms.id = students.room ' \
                    'GROUP BY rooms.id'
        cursor.execute(sql_query)

        # Put the result into dict
        result = {}
        for row in cursor.fetchall(): # fetchall() return tuple(room, number_of_students)
            result[row[0]] = row[1]

        self.disconnect()
        return result

    def get_rooms_with_min_avg_age(self, limit=5):
        '''Connect to database and return 5(as a default) rooms with the smallest average age'''
        self.connect()
        cursor = self.db_connect.cursor()

        sql_query = 'SELECT rooms.name, ' \
                    'AVG(YEAR(CURRENT_DATE()) - YEAR(students.birthday)) as avg_age ' \
                    'FROM rooms LEFT JOIN students ON rooms.id=students.room ' \
                    'GROUP BY rooms.id ' \
                    'ORDER BY avg_age ASC ' \
                    'LIMIT {limit}'.format(limit=limit)

        cursor.execute(sql_query)
        result = cursor.fetchall()
        return result

    def get_rooms_with_age_diff(self, limit=5):
        '''Connect to database and return 5(as a default) rooms with the largest age difference'''
        self.connect()
        cursor = self.db_connect.cursor()

        sql_query = 'SELECT rooms.name, ' \
                    'MAX(YEAR(CURRENT_DATE()) - YEAR(students.birthday)) - MIN(YEAR(CURRENT_DATE() - YEAR(students.birthday)) as age_difference ' \
                    'FROM rooms LEFT JOIN students ON rooms.id=students.room ' \
                    'GROUP BY rooms.id ' \
                    'ORDER BY age_difference DESC ' \
                    'LIMIT {limit}'.format(limit=limit)

        cursor.execute(sql_query)
        result = cursor.fetchall()
        return result

    def get_rooms_with_diff_genders(self):
        '''Connect to database and return rooms with different gender students'''
        self.connect()
        cursor = self.db_connect.cursor()

        sql_query = 'SELECT DISTINCT rooms.name, ' \
                    'FROM rooms JOIN students ON rooms.id=students.room ' \
                    'WHERE EXISTS(SELECT * FROM students WHERE students.room=rooms.id AND students.sex="M") ' \
                    'AND EXISTS(SELECT * FROM students WHERE students.room=rooms.id AND students.sex="F")'

        cursor.execute(sql_query)
        result = cursor.fetchall()
        return result

