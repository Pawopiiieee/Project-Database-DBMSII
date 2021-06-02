from model.Database import *
from model.Course import Course
import model.Student

"""
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| StudyID     | int         | NO   | PRI | NULL    | auto_increment |
| studyname   | varchar(60) | YES  |     | NULL    |                |
| description | varchar(60) | YES  |     | NULL    |                |
| language    | varchar(60) | YES  |     | NULL    |                |
| studyyears  | int         | YES  |     | NULL    |                |
| teacherID   | int         | YES  |     | NULL    |                |
| studentID   | int         | YES  |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
"""

def load_all():
    global g_Database
    rows = g_Database.fetchAll('SELECT * FROM study')
    studies = []
    for row in rows:
        study = Study()
        study.read_row(row)
        studies.append(study)

    return studies

class Study:
    studyID     = None
    studyname   = None
    description = None
    language    = None
    studyyears  = None

    #create static method
    load_all = staticmethod(load_all)

    #gets all studies options: ID or No ID
    def load(self, id):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM study WHERE StudyID='+str(id))

        if not len(rows):
            return False # no row found

        self.read_row(rows[0])
        return True

    #gets all studies options: ID or No ID
    def loadByName(self, name):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM study WHERE studyname="'+str(name)+'"')

        if not len(rows):
            return False # no row found

        self.read_row(rows[0])
        return True

    def read_row(self, row):
        self.studyID      = row['StudyID']
        self.studyname    = row['studyname']
        self.description  = row['description']
        self.language     = row['language']
        self.studyyears   = row['studyyears']

    def getCoursesInStudy(self):
        global g_Database
        rows = g_Database.fetchAll('select * from course where studyID = ' + str(self.studyID))

        courses = []
        for row in rows:
            course = Course()
            course.read_row(row)
            courses.append(course)

        return courses

    def getStudentsEnrolledInStudy(self):
        global g_Database
        rows = g_Database.fetchAll('select * from student where enrolled = "' + str(self.studyname) + '"')

        students = []
        for row in rows:
            student = model.Student.Student()
            student.read_row(row)
            students.append(student)

        return students

    def insert(self):
        global g_Database
        self.studyID = g_Database.executeQuery(
            """
                INSERT INTO study
                (studyname, description, language, studyyears)
                VALUES (%s, %s, %s, %s)
            """,
            (
                self.studyname,
                self.description,
                self.language,
                self.studyyears
            )
        )
        print("Study ID = " + str(self.studyID))

    def update(self):
        global g_Database
        g_Database.executeQuery(
            """
                UPDATE study
                SET studyname = %s, description = %s, language = %s, studyyears = %s
                WHERE studyID=%s
            """,
            (
                self.studyname,
                self.description,
                self.language,
                self.studyyears,
                self.studyID
            )
        )

    def delete(self):
        global g_Database
        g_Database.executeQuery('DELETE FROM study WHERE studyID = ' + str(self.studyID))

    def __repr__(self):
        return str(self.__dict__)
