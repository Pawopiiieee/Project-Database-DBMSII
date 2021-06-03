from model.Database import *
import model.Person
import model.Study
import model.Course
import model.Result

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
	enrolled = None
	personID = None

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
		self.enrolled       = row['enrolled']
		self.personID       = row['personID']

	#get full student personal data
	def getPerson(self):
		person = model.Person.Person()
		person.load(self.personID)
		return person
		
	#get full student personal data
	def getStudy(self):
		study = model.Study.Study()
		study.loadByName(self.enrolled)
		return study

	def getEnrolledCourses(self):
		global g_Database
		rows = g_Database.fetchAll('select * from studentcourse sc inner join course c on sc.courseID = c.courseID where sc.studentID = '+str(self.studentID))
		
		courses = []
		for row in rows:
			course = model.Course.Course()
			course.read_row(row)
			courses.append(course)

		return courses

	def getStudentGrades(self):
		global g_Database
		rows = g_Database.fetchAll('Select * from result where studentID='+str(self.studentID))

		grades = []
		for row in rows:
			result = model.Result.Result()
			result.read_row(row)
			grades.append(result)

		return grades

	def enrollInCourse(self, courseId):
		global g_Database
		return g_Database.executeQuery(
			"""
				INSERT INTO studentcourse
				(studentID, courseID)
				VALUES (%s, %s)
			""",
			(
				self.studentID,
				courseId
			)
		)
	def getStudentCounsellor(self):
		studentCounsellor = model.Teacher.Teacher()
		studentCounsellor.load(self.studyCouncelor)
		return studentCounsellor
		
	def insert(self):
		global g_Database
		self.studentID = g_Database.executeQuery(
			"""
				INSERT INTO student
				(start_year, studycouncelor, enrolled, personID)
				VALUES (%s, %s, %s, %s)
			""",
			(
				self.startYear,
				self.studyCouncelor,
				self.enrolled,
				self.personID
			)
		)

	def update(self):
		global g_Database
		g_Database.executeQuery(
			"""
			UPDATE student
			SET start_year = %s, studycouncelor = %s, enrolled = %s, personID = %s
			WHERE StudentID=%s
			""",
			(
				self.startYear,
				self.studyCouncelor,
				self.enrolled,
				self.personID,
				self.studentID
			)
		)

	def delete(self):
		global g_Database
		g_Database.executeQuery('DELETE FROM student WHERE StudentID = ' + str(self.studentID))

	def __repr__(self):
		return str(self.__dict__)
