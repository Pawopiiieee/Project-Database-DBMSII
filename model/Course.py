from model.Database import *
import model.Student
import model.Study
"""
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| CourseID    | int          | NO   | PRI | NULL    | auto_increment |
| coursename  | varchar(60)  | YES  |     | NULL    |                |
| description | varchar(120) | YES  |     | NULL    |                |
| teacherID   | int          | YES  |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
"""

def load_all():
    global g_Database
    rows = g_Database.fetchAll('SELECT * FROM course')
    courses = []
    for row in rows:
        course = Course()
        course.read_row(row)
        courses.append(course)
    return courses

class Course:
    courseID    = None
    coursetitle = None
    description = None
    credits     = None
    studyID     = None
    teacherID   = None

    #create static method
    load_all = staticmethod(load_all)

    def load(self,id):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM course WHERE courseID='+str(id))

        if not len(rows):
            return False # no row found

        self.read_row(rows[0])
        return True

    def read_row(self,row):
        self.courseID      = row['CourseID']
        self.coursetitle   = row['coursetitle']
        self.description   = row['description']
        self.credits       = row['credits']
        self.teacherID     = row['teacherID']
        self.studyID       = row['studyID']

    #get students in course
    def getStudentsInCourse(self):
        global g_Database
        rows = g_Database.fetchAll('select * from studentcourse sc inner join student s on sc.studentID = s.studentID where sc.courseID = '+str(self.courseID))

        students = []
        for row in rows:
            student = model.Student.Student()
            student.read_row(row)
            students.append(student)

        return students

    def getStudy(self):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM study WHERE studyID='+str(self.studyID))

        if (not len(rows)):
            return None
        study = model.Study.Study()
        study.read_row(rows[0])
        return study

    def getExams(self):
        global g_Database
        rows = g_Database.fetchAll('select * from exam where courseID = '+str(self.courseID))

        exams = []
        for row in rows:
            exam = model.Exam.Exam()
            exam.read_row(row)
            exams.append(exam)

        return exams

    def insert(self):
        global g_Database
        self.courseID = g_Database.executeQuery(
            """
                INSERT INTO course
                (coursetitle, description, credits, teacherID, studyID)
                VALUES (%s, %s, %s, %s, %s)
            """,
            (
                self.coursetitle,
                self.description,
                self.credits,
                self.teacherID,
                self.studyID
            )
        )
        print("course ID = " + str(self.courseID))

    def update(self):
        global g_Database
        g_Database.executeQuery(
            """
                UPDATE course
                SET coursetitle = %s, description = %s, teacherID = %s
                WHERE courseID=%s
            """,
            (
                self.coursetitle,
                self.description,
                self.teacherID,
                self.courseID
            )
        )

    def delete(self):
        global g_Database
        g_Database.executeQuery('DELETE FROM studentcourse WHERE courseID = ' + str(self.courseID))
        g_Database.executeQuery('DELETE FROM course WHERE courseID = ' + str(self.courseID))

    def __repr__(self):
        return str(self.__dict__)
