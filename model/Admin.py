from model.Database import *
from model.Person import *

class Admin:
	adminID = None
	personID = None
	
	#read admin data
	def load(self, id):
		global g_Database
		rows = g_Database.fetchAll('SELECT * FROM admin WHERE adminID='+str(id))

		if not len(rows):
			return False # no row found
		self.read_row(rows[0])
		return True

	def read_row(self,row):
		self.adminID      = row['adminID']
		self.personID       = row['personID']

	def insert(self):
		global g_Database
		self.adminID = g_Database.executeQuery("INSERT INTO admin (personID) VALUES ("+str(self.personID)+")")
		print("admin ID = " + str(self.adminID))
