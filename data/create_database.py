
from model.Database import Database

def createDb(db):

	create_person_table = """
	CREATE TABLE IF NOT EXISTS person (
		PersonID INT PRIMARY KEY AUTO_INCREMENT,
		username VARCHAR(60),
		userpass VARCHAR(60),
		fname VARCHAR(60),
		lname VARCHAR(60),
		birthday DATE,
		gender ENUM('M', 'F', 'O'),
		nationality VARCHAR(60),
		streetname VARCHAR(60),
		streetnumber VARCHAR(60),
		postalcode VARCHAR(10),
		city VARCHAR(60),
		phone VARCHAR(20),
		email VARCHAR(100)
	);"""

	#phone number shouldn't be INT, otherwise it gets messed up
	create_teacher_table = """
	CREATE TABLE IF NOT EXISTS teacher (
		TeacherID INT PRIMARY KEY AUTO_INCREMENT,
		salary INT,
		studycouncelor ENUM('Y', 'N'),
		personID INT,
		foreign key (personID) references person(PersonID)
	);"""

	create_study_table = """
	CREATE TABLE IF NOT EXISTS study(
		StudyID INT PRIMARY KEY AUTO_INCREMENT,
		studyname VARCHAR(60) UNIQUE,
		description VARCHAR(60),
		language VARCHAR(60),
		studyyears INT,
		teacherID INT,
		foreign key (teacherID) references teacher(TeacherID)
	);"""

	create_course_table = """
	CREATE TABLE IF NOT EXISTS course (
		CourseID INT PRIMARY KEY AUTO_INCREMENT,
		coursetitle VARCHAR(60),
		description VARCHAR(120),
		credits INT,
		teacherID INT,
		studyID INT,
		foreign key (teacherID) references teacher(TeacherID),
		foreign key (studyID) references study(studyID)
	);"""

	create_student_table = """
	CREATE TABLE IF NOT EXISTS student (
		StudentID INT PRIMARY KEY AUTO_INCREMENT,
		start_year DATE,
		studycouncelor INT,
		enrolled VARCHAR(256),
		personID INT,
		foreign key (personID) references person(PersonID),
		foreign key (enrolled) references study(studyname),
		foreign key (studycouncelor) references teacher(teacherID)
	);"""

	create_exam_table = """
	CREATE TABLE IF NOT EXISTS exam (
		ExamID INT PRIMARY KEY AUTO_INCREMENT,
		room VARCHAR(10),
		resit ENUM('Y', 'N'),
		date DATE,
		time TIME,
		courseID INT,
		foreign key (courseID) references course(courseID)
	);"""

	create_result_table = """
	CREATE TABLE IF NOT EXISTS result (
		ResultID INT PRIMARY KEY AUTO_INCREMENT,
		examID INT,
		studentID INT,
		pass ENUM('Y', 'N'),
		grade int,
		foreign key (examID) references exam(examId),
		foreign key (studentID) references student(studentId)
	);"""

	create_admin_table = """
	CREATE TABLE IF NOT EXISTS admin (
		adminID INT PRIMARY KEY AUTO_INCREMENT,
		personID INT,
		foreign key (personID) references person(PersonID)
	);"""

	create_examResults_table = """
	create table examResults(
		ResultID int Primary key,
     	ExamID int,
		add foreign key (ResultID) references result(ResultID),
		add foreign key (ExamID) references exam(ExamID)
	);
	"""

	create_studentcourse_table = """
	CREATE TABLE IF NOT EXISTS studentcourse (
		studentID INT,
		courseID INT,
		primary key (studentID, courseID),
		foreign key (courseID) references course(courseID) on delete cascade,
		foreign key (studentID) references student(StudentID) on delete cascade
	);"""

	db.executeQuery(create_person_table)
	db.executeQuery(create_teacher_table)
	db.executeQuery(create_study_table)
	db.executeQuery(create_course_table)
	db.executeQuery(create_student_table)
	db.executeQuery(create_exam_table)
	db.executeQuery(create_result_table)
	db.executeQuery(create_admin_table)
	db.executeQuery(create_studentcourse_table)


def check_or_create_db():
	db = Database()
	createDb(db)

	result = db.fetchAll("SELECT studyID FROM study LIMIT 1;")
	if (not len(result)):
		import data.random_student_data
