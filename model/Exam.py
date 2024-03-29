from model.Database import *
from model.Result import Result

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

def load_all():
    global g_Database
    rows = g_Database.fetchAll('SELECT * FROM exam')
    exams = []
    for row in rows:
        exam = Exam()
        exam.read_row(row)
        exams.append(exam)

    return exams

class Exam:
    examID      = None
    room        = None
    resit       = None
    date        = None
    time        = None
    courseID    = None

    #create static method 
    load_all = staticmethod(load_all)

    def load(self, id):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM exam WHERE ExamID='+str(id))

        if not len(rows):
            return False # no row found

        self.read_row(rows[0])
        return True

    def read_row(self, row):
        self.examID         = row['ExamID']
        self.room           = row['room']
        self.resit          = row['resit']
        self.date           = row['date']
        self.time           = row['time']
        self.courseID       = row['courseID']

    def getStudentGrade(self, studentID):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM result where ExamID=' + str(self.examID) + ' and studentID = ' + str(studentID))
        if not len(rows):
            return None # no row found
        result = Result()
        result.read_row(rows[0])
        return result

    def insert(self):
        global g_Database
        self.examID = g_Database.executeQuery(
            """
                INSERT INTO exam
                (room, resit, date, time, courseID)
                VALUES (%s, %s, %s, %s, %s)
            """,
            (
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
                SET room = %s, resit = %s, date = %s, time = %s, courseID = %s
                WHERE ExamID=%s
            """,
            (
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
