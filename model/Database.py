import mysql.connector
from mysql.connector import Error
from getpass import getpass

# Connection credentials
HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'welkom01' # This is the database password, not the user password
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
                host     = HOSTNAME,
                user     = USERNAME,
                password = PASSWORD,
                database = DB_NAME,
                auth_plugin='mysql_native_password'
            )

        except Error as err:
            print(f"Database Error: '{err}'")

    # String         query
    # Tuple<String>  params
    def fetchAll(self, query, params = ()):
        if self.connection is None:
            print("executeQuery failed")
            return None

        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()

            if (result == None):
                return []
            return result
        except Error as err:
            print(query, params)
            print(f"Database Error: '{err}'")
            return []

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
            print(query, params)
            print(f"Database Error: '{err}'")
            return None



# Global database object
#if __name__ == '__main__':
print("setting g_Database\n...")
g_Database = Database()
