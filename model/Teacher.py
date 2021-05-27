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

    #retrieves teachers, option: ID or No ID
    def load(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('SELECT * FROM teacher WHERE teacherID='+str(id))
        else:
            rows = g_Database.fetchAll('SELECT * FROM teacher')
        for row in rows:
            print(row)
        if not len(rows):
            return False # no row found

        self.teacherID      = rows[0]['TeacherID']
        self.salary         = rows[0]['salary']
        self.studycouncelor = rows[0]['studycouncelor']
        self.personID       = rows[0]['personID']

        return True
    #retrieves full information of teachers from person table: Options: ID or No ID
    def getTeacher(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('select * from teacher inner join person on teacher.personID = person.PersonID where teacher.teacherID=' +str(id))
        else:
            rows = g_Database.fetchAll('select * from teacher inner join person on teacher.personID = person.PersonID')
        for row in rows:
            print(rows)
        if not len(rows):
            return False

        self.teacherID = rows[0]['TeacherID']
        self.salary = rows[0]['salary']
        self.studycouncelor = rows[0]['studycouncelor']
        self.personID = rows[0]['personID']

        return True

    def getTeacherStudies(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('select studyname, teacherID from study where teacherID =' +str(id))
        else:
            rows = g_Database.fetchAll('select studyname, teacherID from study')
        for row in rows:
            print(row)
        if not len(rows):
            return False

        self.studyname = rows[0]['studyname']
        self.teacherID = rows[0]['teacherID']

        return True

    def getTeacherCourse(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('select coursetitle, teacherID from course where teacherID=' +str(id))
        else:
            rows = g_Database.fetchAll('select coursetitle, teacherID from course')
        for row in rows:
            print(row)
        if not len(rows):
            return False;

        self.coursetitle = rows[0]['coursetitle']
        self.teacherID = rows[0]['teacherID']

        return True

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
        g_Database.executeQuery('DELETE FROM teacher WHERE teacherID = ' + str(self.teacherID))

    def __repr__(self):
        return str(self.__dict__)
