from model.Database import *

"""
+-----------+---------------+------+-----+---------+----------------+
| Field     | Type          | Null | Key | Default | Extra          |
+-----------+---------------+------+-----+---------+----------------+
| ResultID  | int           | NO   | PRI | NULL    | auto_increment |
| examID    | int           | YES  |     | NULL    |                |
| studentID | int           | YES  |     | NULL    |                |
| pass      | enum('Y','N') | YES  |     | NULL    |                |
| grade     | int           | NO   |     | NULL    |                |
+-----------+---------------+------+-----+---------+----------------+
"""

class Result:
    ResultID = None
    examID    = None
    studentID = None
    grade = None
    passed = None

    def load(self, id):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM result WHERE ResultID='+str(id))
        if not len(rows):
            return False # no row found

        self.ResultID  = rows[0]['ResultID']
        self.examID    = rows[0]['examID']
        self.studentID = rows[0]['studentID']
        self.passed    = rows[0]['passed']
        self.grade     = rows[0]['grade']

        return True


    def insert(self):
        global g_Database
        self.ResultID = g_Database.executeQuery(
            """
                INSERT INTO result
                (ResultID, examID, studentID, passed, grade
                VALUES (%s, %s, %s, %s, %s)
            """,
            (
                self.ResultID,
                self.examID,
                self.studentID,
                self.passed,
                self.grade
            )
        )
        print("Result ID = " + str(self.ResultID))


    def update(self):
        global g_Database
        g_Database.executeQuery(
            """
            UPDATE person
            SET ResultID = %s, examID = %s, studentID = %s, passed = %s, grade = %s
            WHERE ResultID=%s
            """,
            (
                self.resultID,
                self.examID,
                self.studentID,
                self.passed,
                self.grade,
            )
        )

    def delete(self):
        global g_Database
        g_Database.executeQuery('DELETE FROM result WHERE ResultID = ' + str(self.resultID))

    def __repr__(self):
        return str(self.__dict__)
###
