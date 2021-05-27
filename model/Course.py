from model.Database import *
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

class Course:
    courseID    = None
    coursetitle = None
    description = None
    teacherID   = None

    def load(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('SELECT * FROM course WHERE courseID='+str(id))
        else:
            rows = g_Database.fetchAll('SELECT * FROM course')
        for row in rows:
            print(row)
        if not len(rows):
            return False # no row found

        self.courseID      = rows[0]['CourseID']
        self.coursetitle   = rows[0]['coursetitle']
        self.description   = rows[0]['description']
        self.teacherID     = rows[0]['teacherID']

        return True

    #get students in course
    def getStudentsInCourse(self):
        global g_Database
        rows = g_Database.fetchAll('select course.courseID, course.coursetitle, course.description, studentcourse.studentID from course inner join studentcourse on course.courseID = studentcourse.courseID')
        for row in rows:
            print(rows)

    #insert int to table studentcourse
    def insertIntoStudentCourse(self):
        global g_Database
        self.studentID = g_Database.executeQuery(
         """
            INSERT INTO studentcourse
            (studentID, courseID)
            VALUES(%s, %s)
         """,
         (
            self.studentID,
            self.courseID
         )
     )


    def insert(self):
        global g_Database
        self.courseID = g_Database.executeQuery(
            """
                INSERT INTO course
                (coursetitle, description, teacherID)
                VALUES (%s, %s, %s)
            """,
            (
                self.coursetitle,
                self.description,
                self.teacherID,
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
        g_Database.executeQuery('DELETE FROM course WHERE courseID = ' + str(self.courseID))

    def __repr__(self):
        return str(self.__dict__)
