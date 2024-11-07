#connect.py 

# Name: Connor MacFarland, Anthony Caggiano, JD Poindexter
# email: macfarct@mail.uc.edu, caggiaaj@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:  11/07/2024
# Course #/Section:   IS 4010- 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Collaborating with a team to develop a VS project that accesses our SQL Server instance, extracts some data from the Grocery Store Simulator database, and produces some interesting results.  
# Brief Description of what this module does: this is where the code connects to the sql database and pulls the data into the prompt. 
# Anything else that's relevant: 
# Citations: https://stackoverflow.com/questions/69145633/how-to-initialize-a-database-connection-only-once-and-reuse-it-in-run-time-in-py, https://softwareengineering.stackexchange.com/questions/200522/how-to-deal-with-database-connections-in-a-python-library-module, and AccessingData in class assignment 


import pyodbc

# Establish the connection and make it a global object
class dataSource(object):
    """
    connects to the sql data source 
    """
    def __init__(self, conn):
        """
        Checking connection to the database
        @param conn Connection: SQL database connection 
        """
        self.__conn = conn
        
    def connect():
        """
        Connect to the database
        @return Connection Object: The open connection or None on error
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
        @return String: showing what the object is  
        """
        return "model: " + self.__conn

    def __repr__(self):
        """
        @return String: a copy of dataSource that shows the string. 
        """
        return f"Connection('{self.__conn}')"