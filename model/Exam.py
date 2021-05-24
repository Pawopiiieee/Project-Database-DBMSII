from model.Database import *


"""
+-------------+---------------+------+-----+---------+----------------+
| Field       | Type          | Null | Key | Default | Extra          |
+-------------+---------------+------+-----+---------+----------------+
| ExamID      | int           | NO   | PRI | NULL    | auto_increment |
| coursetitle | varchar(60)   | YES  |     | NULL    |                |
| room        | varchar(10)   | YES  |     | NULL    |                |
| resit       | enum('Y','N') | YES  |     | NULL    |                |
| date        | date          | YES  |     | NULL    |                |
| time        | time          | YES  |     | NULL    |                |
| courseID    | int           | YES  |     | NULL    |                |
+-------------+---------------+------+-----+---------+----------------+
"""

class Exam:
    ExamID = None
    coursetitle = None
    room = None
    resit = None
    date = None
    time = None
    courseID = None

    def load(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('SELECT * FROM exam WHERE ExamID='+str(id))
        else:
            rows = g_Database.fetchAll('SELECT * FROM exam')
        if not len(rows):
            return False # no row found

        self.examID    = rows[0]['ExamID']
        self.coursetitle    = rows[0]['coursetitle']
        self.room = rows[0]['room']
        self.resit    = rows[0]['resit']
        self.date     = rows[0]['date']
        self.time = rows[0]['time']
        self.courseID = rows[0]['courseID']

        return True

    def insert(self):
        global g_Database
        self.examID = g_Database.executeQuery(
            """
                INSERT INTO exam
                (coursetitle, room, resit, date, time, courseID)
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                self.coursetitle,
                self.room,
                self.resit,
                self.date,
                self.time,
                self.courseID
            )
        )
        print("Exam ID = " + str(self.examID))

    def update(self):
        global g_Database
        g_Database.executeQuery(
            """
                UPDATE exam
                SET coursetitle = %s, room = %s, resit = %s, date = %s, time = %s, courseID = %s
                WHERE ExamID=%s
            """,
            (
                self.coursetitle,
                self.room,
                self.resit,
                self.date,
                self.time,
                self.courseID,
                self.examID
            )
        )

    def delete(self):
        global g_Database
        g_Database.executeQuery('DELETE FROM exam WHERE ExamID = ' + str(self.examID))

    def __repr__(self):
        return str(self.__dict__)
