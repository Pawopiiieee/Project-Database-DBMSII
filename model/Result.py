from model.Database import *

"""
+-----------+---------------+------+-----+---------+----------------+
| Field     | Type          | Null | Key | Default | Extra          |
+-----------+---------------+------+-----+---------+----------------+
| ResultID  | int           | NO   | PRI | NULL    | auto_increment |
| examID    | int           | YES  |     | NULL    |                |
| studentID | int           | YES  |     | NULL    |                |
| pass      | enum('Y','N') | YES  |     | NULL    |                |
| grade     | int           | NO   |     | NULL    |                |
+-----------+---------------+------+-----+---------+----------------+
"""

class Result:
    ResultID  = None
    examID    = None
    studentID = None
    grade     = None
    passed    = None

    def load(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('SELECT * FROM result WHERE ResultID='+str(id))
        else:
            rows = g_Database.fetchAll('SELECT * FROM result')
        for row in rows:
            print(row)
        if not len(rows):
            return False # no row found

		self.ResultID  = rows[0]['ResultID']
		self.examID    = rows[0]['examID']
		self.studentID = rows[0]['studentID']
		self.passed    = rows[0]['passed']
		self.grade     = rows[0]['grade']

		return True

    def getStudentGrades(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('Select grade from result where studentID = ?'+str(id))
        else:
            rows = g_Database.fetchAll('select result.grade, student.StudentID from result inner join student on student.StudentID = result.StudentID')
        for row in rows:
            print(row)
        if not len(rows):
            return False


	def insert(self):
		global g_Database
		self.ResultID = g_Database.executeQuery(
			"""
			INSERT INTO result
			(examID, studentID, passed, grade)
			VALUES (%s, %s, %s, %s)
			""",
			(
				self.examID,
				self.studentID,
				self.passed,
				self.grade
			)
		)
		print("Result ID = " + str(self.ResultID))


	def update(self):
		global g_Database
		g_Database.executeQuery(
			"""
			UPDATE result
			SET examID = %s, studentID = %s, passed = %s, grade = %s
			WHERE ResultID=%s
			""",
			(
				self.examID,
				self.studentID,
				self.passed,
				self.grade,
				self.ResultID
			)
		)

	def delete(self):
		global g_Database
		g_Database.executeQuery('DELETE FROM result WHERE ResultID = ' + str(self.ResultID))

	def __repr__(self):
		return str(self.__dict__)
###
