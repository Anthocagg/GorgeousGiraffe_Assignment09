 #Name: Anthony Caggiano, Connor MacFarland, JD Poindexter
# email: caggiaaj@mail.uc.edu, poindejd@mail.uc.edu, macfarcm@mail.uc.edu
# Assignment Number: Assignment 09  
# Due Date:   11/07/24
# Course #/Section:  IS4010
# Semester/Year:  F4
# Brief Description of the assignment: In this assignment we took a dataset and figured out how to manipualte it and get infomation

# Brief Description of what this module does. In this module we learned how to import datasets and how to use them
# Citations: https://www.datacamp.com/tutorial/tutorial-how-to-execute-sql-queries-in-r-and-python
#https://www.w3schools.com/python/python_mysql_select.asp
#https://stackoverflow.com/questions/44149394/select-a-random-row-from-the-table-using-python

# Anything else that's relevant:
# # Connect.py
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

