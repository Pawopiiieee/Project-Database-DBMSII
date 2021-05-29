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
    studyID = None
    studyname = None
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

    def read_row(self, row):
        self.studyID      = row['StudyID']
        self.studyname    = row['studyname']
        self.description  = row['description']
        self.language     = row['language']
        self.studyyears   = row['studyyears']

        #@todo debug where clause!!!!!
    def getStudentsEnrolledInStudy(self):
        global g_Database
        rows = g_Database.fetchAll('select student.StudentID, studyname from student inner join study on student.enrolled = study.studyname')
        for row in rows:
            print(row)
        if not len(rows):
            return False

        self.studyname = rows[0]['studyname']
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
