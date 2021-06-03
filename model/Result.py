from model.Database import *

"""
+-----------+---------------+------+-----+---------+----------------+
| Field     | Type          | Null | Key | Default | Extra          |
+-----------+---------------+------+-----+---------+----------------+
| ResultID  | int           | NO   | PRI | NULL    | auto_increment |
| examID    | int           | YES  | MUL | NULL    |                |
| studentID | int           | YES  | MUL | NULL    |                |
| passed    | enum('Y','N') | YES  |     | NULL    |                |
| grade     | int           | NO   |     | NULL    |                |
+-----------+---------------+------+-----+---------+----------------+
"""

def load_all():
	global g_Database
	rows = g_Database.fetchAll('SELECT * FROM result')
	results = []
	for row in rows:
		result = Result()
		result.read_row(row)
		results.append(result)

	return results

class Result:
	resultID  = None
	examID    = None
	studentID = None
	grade     = None
	passed    = None

	#create static method
	load_all = staticmethod(load_all)

	def load(self, id):
		global g_Database
		rows = g_Database.fetchAll('SELECT * FROM result WHERE ResultID='+str(id))

		if not len(rows):
			return False #no row found

		self.read_row(rows[0])
		return True

	def read_row(self, row):
		self.resultID 	= row['ResultID']
		self.examID 	= row['examID']
		self.studentID  = row['studentID']
		self.grade 		= row['grade']
		self.passed 	= row['passed']

	def insert(self):
		global g_Database
		self.resultID = g_Database.executeQuery(
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
		print("Result ID = " + str(self.resultID))


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
				self.resultID
			)
		)

	def delete(self):
		global g_Database
		g_Database.executeQuery('DELETE FROM result WHERE ResultID = ' + str(self.ResultID))

	def __repr__(self):
		return str(self.__dict__)
###
