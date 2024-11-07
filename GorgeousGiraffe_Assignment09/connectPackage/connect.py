# Connect.py
import pyodbc


class DatabaseConnection(object):
    """
    Establishes a connection to the UC database
    """
    def __init__(self, conn):
        """
        Constructor
        @param conn Connection: Connection object to connect to database
        """
        self.__conn = conn
       
    def connect_to_database():
        """
        Connect to the database
        @return Connection Object: The open connection, or None on error
        """
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=GroceryStoreSimulator;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
        except:
            conn = None
       
        return conn
       
    def __str__(self):
        """
        @return String: A readable basic representation of the current object.
        """
        return "model: " + self.__conn

    def __repr__(self):
        """
        @return String: A string that can be executed to create a copy of the current data
        """
        return f"Connection('{self.__conn}')"

