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
        self.connect()
        cursor = self.db_connect.cursor()

        sql_query = 'SELECT rooms.name, ' \
                    'AVG(YEAR(CURRENT_DATE()) - YEAR(students.birthday)) as avg_age ' \
                    'FROM rooms LEFT JOIN students ON rooms.id=students.room ' \
                    'GROUP BY rooms.id ' \
                    'ORDER BY avg_age ASC ' \
                    'LIMIT {limit}'.format(limit=limit)
