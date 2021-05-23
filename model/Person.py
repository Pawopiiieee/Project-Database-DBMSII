from model.Database import *



class Person: # Table person
    personID = None
    userName = None
    userPass = None
    fname = None
    lname = None
    birthday = None
    nationality = None
    gender = None
    street = None
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
        self.load(rows[0]['PersonID'])
        return True

    def load(self, id): # by PersonID
        global g_Database
        rows = g_Database.fetchAll('SELECT * FROM person WHERE PersonID='+str(id))
        if not len(rows):
            return False # no row found

        self.personID     = rows[0]['PersonID']
        self.userName     = rows[0]['username']
        self.userPass     = rows[0]['userpass']
        self.fname        = rows[0]['fname']
        self.lname        = rows[0]['lname']
        self.birthday     = rows[0]['birthday']
        self.gender       = rows[0]['gender']
        self.nationality  = rows[0]['nationality']
        self.streetname   = rows[0]['streetname']
        self.streetnumber = rows[0]['streetnumber']
        self.postalcode   = rows[0]['postalcode']
        self.city         = rows[0]['city']
        self.phone        = rows[0]['phone']
        self.email        = rows[0]['email']

        return True


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
                self.street,
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
                self.street,
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
