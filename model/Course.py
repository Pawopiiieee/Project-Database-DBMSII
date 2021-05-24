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
    courseID = None
    coursetitle = None
    description = None
    teacherID = None

    def load(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('SELECT * FROM course WHERE courseID='+str(id))
        else:
            rows = g_Database.fetchAll('SELECT * FROM course')
        if not len(rows):
            return False # no row found

        self.courseID      = rows[0]['CourseID']
        self.coursetitle    = rows[0]['coursetitle']
        self.description   = rows[0]['description']
        self.teacherID     = rows[0]['teacherID']

        return True

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
