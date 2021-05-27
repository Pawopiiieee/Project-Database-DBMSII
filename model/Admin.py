from model.Database import *
from model.Person import *

class Admin:
    adminID = None
    #option by ID or No ID
    def load(self, id = -1):
        global g_Database
        if id != -1:
            rows = g_Database.fetchAll('SELECT * FROM admin inner join person on admin.PersonID = person.PersonID where admin.adminID =' +str(id))
        else:
            rows = g_Database.fetchAll('SELECT * FROM admin inner join person on admin.PersonID = person.PersonID')
        for row in rows:
            print(rows)
        if not len(rows):
            return False

        self.personID = rows[0]['PersonID']
        return True

#im stuck a little bit? Because, admin is a role, so he is the person who performs the actions, so there's no CRUD to insert here.
#im unsure what the admin's functionalities cept for CRUD
