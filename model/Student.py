from model.Database import *
from model.Person import *

def load_all():
    global g_Database
    rows = g_Database.fetchAll('SELECT * FROM student')
    students = []
    for row in rows:
        student = Student()
        student.read_row(row)
        students.append(student)
    return students

class Student:
    studentID = None
    startYear = None
    studyCouncelor = None

    #create static method
    load_all = staticmethod(load_all)

    #read student data
    def load(self, id):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM student WHERE StudentID='+str(id))
       
        if not len(rows):
            return False # no row found
        self.read_row(rows[0])
        return True

    def read_row(self,row):
        self.studentID      = row['StudentID']
        self.startYear      = row['start_year']
        self.studyCouncelor = row['studycouncelor']
        self.personID       = row['personID']

    #get full student data: options ID or No ID
    def getStudent(self):
        global g_Database
        rows = g_Database.fetchAll('select * from student inner join person on student.personID = person.PersonID')
        """
        unused lines
        if id != -1:
            rows = g_Database.fetchAll('select * from student inner join person on student.personID = person.PersonID where student.StudentID =' +str(id))
        else:
            rows = g_Database.fetchAll('select * from student inner join person on student.personID = person.PersonID')
        """
        for row in rows:
            print(row)
        if not len(rows):
            return False
        self.studentname = rows[0]["studentname"]
        return True

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
