from model.Database import *

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

class Study:
    StudyID = None
    studyname = None
    description = None
    language = None
    studyyears = None

    def load(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('SELECT * FROM study WHERE StudyID='+str(id))
        else:
            rows = g_Database.fetchAll('SELECT * FROM study')
        if not len(rows):
            return False # no row found

        self.studyID      = rows[0]['StudyID']
        self.studyname    = rows[0]['studyname']
        self.description  = rows[0]['description']
        self.language     = rows[0]['language']
        self.studyyears   = rows[0]['studyyears']

        return True

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
                SET studyname = %s, description = %s, language = %s
                WHERE courseID=%s
            """,
            (
                self.studyname,
                self.description,
                self.language,
                self.studyID
            )
        )

    def delete(self):
        global g_Database
        g_Database.executeQuery('DELETE FROM study WHERE studyID = ' + str(self.studyID))

    def __repr__(self):
        return str(self.__dict__)
