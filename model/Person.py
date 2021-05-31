from model.Database import *
from model.Student import *
from model.Teacher import *
from model.Admin import *

class Person: # Table person
    personID = None
    userName = None
    userPass = None
    fname = None
    lname = None
    birthday = None
    nationality = None
    gender = None
    streetname = None
    streetNumber = None
    postalCode = None
    city = None
    phone = None
    email = None

    def loadByUsername(self, username, password):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM person WHERE username="' + username + '" AND userpass="' + password + '"')
        if not len(rows):
            return False # no row found
        
        self.read_row(rows[0])
        return True

    def load(self, id): # by PersonID
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM person WHERE personID='+str(id))
        
        if not len(rows):
            return False # no row found

        self.read_row(rows[0])
        return True

    def read_row(self,row):
        self.personID     = row['PersonID']
        self.userName     = row['username']
        self.userPass     = row['userpass']
        self.fname        = row['fname']
        self.lname        = row['lname']
        self.birthday     = row['birthday']
        self.gender       = row['gender']
        self.nationality  = row['nationality']
        self.streetname   = row['streetname']
        self.streetNumber = row['streetnumber']
        self.postalCode   = row['postalcode']
        self.city         = row['city']
        self.phone        = row['phone']
        self.email        = row['email']

    def getStudent(self):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM student WHERE personID='+str(self.personID))

        if (not len(rows)):
            return None

        student = Student()
        student.read_row(rows[0])
        return student
        
    def getTeacher(self):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM teacher WHERE personID='+str(self.personID))

        if (not len(rows)):
            return None

        teacher = Teacher()
        teacher.read_row(rows[0])
        return teacher
        
    def getAdmin(self):
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM admin WHERE personID='+str(self.personID))

        if (not len(rows)):
            return None

        admin = Admin()
        admin.read_row(rows[0])
        return admin

    def insert(self):
        global g_Database
        self.personID = g_Database.executeQuery(
            """
            INSERT INTO person
            (userName, userPass, fname, lname, birthday, nationality, gender, streetname, streetnumber, postalCode, city, phone, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                self.userName,
                self.userPass,
                self.fname,
                self.lname,
                self.birthday,
                self.nationality,
                self.gender,
                self.streetname,
                self.streetNumber,
                self.postalCode,
                self.city,
                self.phone,
                self.email
            )
        )
        print("Person ID = " + str(self.personID))


    def update(self):
        global g_Database
        g_Database.executeQuery(
            """
            UPDATE person
            SET userName = %s, userPass = %s, fname = %s, lname = %s, birthday = %s, nationality = %s, gender = %s, streetname = %s, streetnumber = %s, postalCode = %s, city = %s, phone = %s, email = %s
            WHERE PersonID=%s
            """,
            (
                self.userName,
                self.userPass,
                self.fname,
                self.lname,
                self.birthday,
                self.nationality,
                self.gender,
                self.streetname,
                self.streetNumber,
                self.postalCode,
                self.city,
                self.phone,
                self.email,
                self.personID
            )
        )

    def delete(self):
        global g_Database
        g_Database.executeQuery('DELETE FROM person WHERE PersonID = ' + str(self.personID))

    def __repr__(self):
        return str(self.__dict__)
###
