from model.Database import *
import model.Person
import model.Course

"""
+----------------+---------------+------+-----+---------+----------------+
| Field          | Type          | Null | Key | Default | Extra          |
+----------------+---------------+------+-----+---------+----------------+
| TeacherID      | int           | NO   | PRI | NULL    | auto_increment |
| salary         | int           | YES  |     | NULL    |                |
| studycouncelor | enum('Y','N') | YES  |     | NULL    |                |
| personID       | int           | YES  |     | NULL    |                |
+----------------+---------------+------+-----+---------+----------------+
"""

def load_all():
	global g_Database
	rows = g_Database.fetchAll('SELECT * FROM teacher')
	teachers = []
	for row in rows:
		teacher = Teacher()
		teacher.read_row(row)
		teachers.append(teacher)
	return teachers

def load_studycounselers():
	global g_Database
	rows = g_Database.fetchAll('SELECT * FROM teacher')
	studycounselers = []
	for row in rows:
		studycounseler = Teacher()
		studycounseler.read_row(row)
		studycounselers.append(studycounseler)
	return studycounselers

class Teacher:
	teacherID      = None
	salary         = None
	studycouncelor = None
	personID = None

	#create static method
	load_all = staticmethod(load_all)
	load_studycounselers = staticmethod(load_studycounselers)

	#retrieves teachers
	def load(self, id):
		global g_Database
		rows = g_Database.fetchAll('SELECT * FROM teacher WHERE teacherID='+str(id))

		if not len(rows):
			return False # no row found

		self.read_row(rows[0])
		return True
		
	def read_row(self,row):
		self.teacherID      = row['TeacherID']
		self.salary         = row['salary']
		self.studycouncelor = row['studycouncelor']
		self.personID       = row['personID']

	#retrieves full information of teachers from person table: 
	def getPerson(self):
		person = model.Person.Person()
		person.load(self.personID)
		return person

	def getTeacherCourses(self):
		global g_Database
		rows = g_Database.fetchAll('select * from course where teacherID =' +str(self.teacherID))

		courses = []
		for row in rows:
			course = model.Course.Course()
			course.read_row(row)
			courses.append(course)
		return courses

	def insert(self):
		global g_Database
		self.teacherID = g_Database.executeQuery(
			"""
				INSERT INTO Teacher
				(salary, studycouncelor, personID)
				VALUES (%s, %s, %s)
			""",
			(
				self.salary,
				self.studycouncelor,
				self.personID
			)
		)

	def update(self):
		global g_Database
		g_Database.executeQuery(
			"""
			UPDATE teacher
			SET salary = %s, studycouncelor = %s, personID = %s
			WHERE teacherID=%s
			""",
			(
				self.salary,
				self.studycouncelor,
				self.personID,
				self.teacherID
			)
		)

	def delete(self):
		global g_Database
		g_Database.executeQuery('DELETE FROM teacher WHERE teacherID = ' + str(self.teacherID))

	def __repr__(self):
		return str(self.__dict__)
