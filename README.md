# Loading data from JSON files into a MySQL database and some queries to that database

The `filling_database.py` script reads from JSON files and writes to the already created database with tables with the following schemes:

**rooms**
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int         | NO   | PRI | NULL    |       |
| name  | varchar(50) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+

**students**
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| id       | int           | NO   | PRI | NULL    |       |
| name     | varchar(50)   | YES  |     | NULL    |       |
| birthday | date          | YES  |     | NULL    |       |
| sex      | enum('M','F') | YES  |     | NULL    |       |
| room     | int           | YES  | MUL | NULL    |       |
+----------+---------------+------+-----+---------+-------+

The `db_repository.py` script, based on the "Repository" pattern and OOP, allows instances of the `RoomRepository` class to connect to the database, and these instances contain the following methods to query the database:

- `get_rooms_with_num_students` - returns a list of rooms and the number of students in each room
- `get_rooms_with_min_avg_age` - returns 5 rooms with the smallest average age of students (the default value is 5, you can pass any integer to the `limit` parameter)
- `get_rooms_with_age_diff` - returns 5 rooms with the largest age difference between students (the default value is 5, any integer can be passed in the `limit` parameter)
- `get_rooms_with_diff_genders` - returns the list of rooms where different-sex students live

All results are returned in JSON format.