from model.Database import *
from model.Person import *

class Student:
    studentID = None
    startYear = None
    studyCouncelor = None
    #read student data
    def load(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('SELECT * FROM student WHERE StudentID='+str(id))
        else:
            rows = g_Database.fetchAll('SELECT * FROM student')
        if not len(rows):
            return False # no row found

        self.studentID      = rows[0]['StudentID']
        self.startYear      = rows[0]['start_year']
        self.studyCouncelor = rows[0]['studycouncelor']
        self.personID       = rows[0]['personID']

        return True

    #get full student data: options ID or No ID
    def getStudent(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('select * from student inner join person on student.personID = person.PersonID where student.StudentID =' +str(id))
        else:
            rows = g_Database.fetchAll('select * from student inner join person on student.personID = person.PersonID')
        for row in rows:
            print(rows)
        if not len(rows):
            return False

    def insert(self):
        global g_Database
        return g_Database.executeQuery(
            """
                INSERT INTO student
                (start_year, studycouncelor, personID)
                VALUES (%s, %s, %s)
            """,
            (
                self.startYear,
                self.studyCouncelor,
                self.personID
            )
        )

    def update(self):
        global g_Database
        g_Database.executeQuery(
            """
            UPDATE student
            SET start_year = %s, studycouncelor = %s, personID = %s
            WHERE StudentID=%s
            """,
            (
                self.startYear,
                self.studyCouncelor,
                self.personID,
                self.studentID
            )
        )

    def delete(self):
        global g_Database
        g_Database.executeQuery('DELETE FROM student WHERE StudentID = ' + str(self.studentID))

    def __repr__(self):
        return str(self.__dict__)
