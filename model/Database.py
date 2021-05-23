import mysql.connector
from mysql.connector import Error
from getpass import getpass

# Connection credentials
HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'Dolfijn123%' # This is the database password, not the user password
DB_NAME  = 'Diemen'

class Database:

    """
    Connects to the database.
    """
    def __init__(self):
        self.connection = None # close connection so it doest become confused with multiple open connections

        # try to connect, or return mysql error, if successfull will return connection object
        try:
            self.connection = mysql.connector.connect(
                host = HOSTNAME,
                user = USERNAME,
                password = PASSWORD,
                database = DB_NAME
            )

        except Error as err:
            print(f"Database Error: '{err}'")


    """ @TODO: remove
    def create_db(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("database created succesfully")
        except Error as err:
            print(f"Error: '{err}'")
    """


    # String         query
    # Tuple<String>  params
    def fetchAll(self, query, params = ()):
        if self.connection is None:
            print("executeQuery failed")
            return None

        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as err:
            print(f"Database Error: '{err}'")
            return None

    # String         query
    # Tuple<String>  params
    # @return {int|None} Last inserted row ID if applicable
    def executeQuery(self, query, params = ()):
        if self.connection is None:
            print("executeQuery failed")
            return None

        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit() #suicido
            print("Query Succesfull")
            return cursor.lastrowid
        except Error as err:
            print(f"Database Error: '{err}'")
            return None



    def createDb(self):
        create_university_table = """
        CREATE TABLE person (
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
            phone INT UNIQUE,
            email VARCHAR(100),
            studentID INT,
            adminID INT,
            teacherID INT);"""

        create_teacher_table = """
        CREATE TABLE teacher (
            TeacherID INT PRIMARY KEY AUTO_INCREMENT,
            salary INT,
            studycouncelor ENUM('Y', 'N'),
            personID INT);"""

        create_course_table = """
        CREATE TABLE course (
            CourseID INT PRIMARY KEY AUTO_INCREMENT,
            coursename VARCHAR(60),
            description VARCHAR(120),
            teacherID INT);"""

        create_student_table = """
        CREATE TABLE student (
            StudentID INT PRIMARY KEY AUTO_INCREMENT,
            start_year DATE,
            studycouncelor ENUM('Y', 'N'),
            personID INT);"""

        create_study_table = """
        CREATE TABLE study(
            StudyID INT PRIMARY KEY AUTO_INCREMENT,
            studyname VARCHAR(60),
            description VARCHAR(60),
            language VARCHAR(60),
            studyyears INT,
            teacherID INT,
            studentID INT);"""

        create_exam_table = """
        CREATE TABLE exam (
            ExamID INT PRIMARY KEY AUTO_INCREMENT,
            coursetitle VARCHAR(60),
            room VARCHAR(10),
            resit ENUM('Y', 'N'),
            date DATE,
            time TIME,
            courseID INT);"""

        create_result_table = """
        CREATE TABLE result (
            ResultID INT PRIMARY KEY AUTO_INCREMENT,
            examID INT,
            studentID INT,
            pass ENUM('Y', 'N'));"""

        create_admin_table = """
        CREATE TABLE admin (
            ID INT PRIMARY KEY AUTO_INCREMENT
        );"""

        self.executeQuery(create_university_table)
        self.executeQuery(create_teacher_table)
        self.executeQuery(create_student_table)
        self.executeQuery(create_course_table)
        self.executeQuery(create_study_table)
        self.executeQuery(create_exam_table)
        self.executeQuery(create_result_table)
        self.executeQuery(create_admin_table)


# Global database object
#if __name__ == '__main__':
print("setting g_Databas\ne...")
g_Database = Database()
#g_Database.createDb()
