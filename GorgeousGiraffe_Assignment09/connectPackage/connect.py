import pyodbc

# Establish the connection and make it a global object
try:
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        'Server=lcb-sql.uccob.uc.edu\\nicholdw;'  # Make sure this is correct
        'Database=IS4010;'
        'UID=IS4010Login;'
        'PWD=P@ssword2;'
    )
    print("Connection established successfully.")
except Exception as e:
    print("An error occurred while trying to connect to the database:", e)
    conn = None  # Set conn to None if the connection fails

