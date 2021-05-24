from model.Database import *
from model.Person import *

"""
+----------------+---------------+------+-----+---------+----------------+
| Field          | Type          | Null | Key | Default | Extra          |
+----------------+---------------+------+-----+---------+----------------+
| TeacherID      | int           | NO   | PRI | NULL    | auto_increment |
| salary         | int           | YES  |     | NULL    |                |
| studycouncelor | enum('Y','N') | YES  |     | NULL    |                |
| personID       | int           | YES  |     | NULL    |                |
+----------------+---------------+------+-----+---------+----------------+
"""


class Teacher:
    TeacherID      = None
    salary         = None
    studycouncelor = None

    def load(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('SELECT * FROM teacher WHERE teacherID='+str(id))
        else:
            rows = g_Database.fetchAll('SELECT * FROM teacher')
        if not len(rows):
            return False # no row found

        self.teacherID      = rows[0]['TeacherID']
        self.salary         = rows[0]['salary']
        self.studycouncelor = rows[0]['studycouncelor']
        self.personID       = rows[0]['personID']

        return True

    def getPerson(self):
        if self.personID is None:
            return None
        person = Person()
        person.load(self.personID)
        return person

    def insert(self):
        global g_Database
        return g_Database.executeQuery(
            """
                INSERT INTO Teacher
                (salary, studycouncelor, personID)
                VALUES (%s, %s, %s)
            """,
            (
                self.salary,
                self.studycouncelor,
                self.personID
            )
        )

    def update(self):
        global g_Database
        g_Database.executeQuery(
            """
            UPDATE teacher
            SET salary = %s, studycouncelor = %s, personID = %s
            WHERE teacherID=%s
            """,
            (
                self.salary,
                self.studycouncelor,
                self.personID,
                self.teacherID
            )
        )

    def delete(self):
        global g_Database
        g_Database.executeQuery('DELETE FROM teacher WHERE teacherID = ' + str(self.studentID))

    def __repr__(self):
        return str(self.__dict__)
