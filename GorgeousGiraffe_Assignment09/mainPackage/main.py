# Name: Anthony Caggiano, Connor MacFarland, JD Poindexter
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

import random
import pyodbc
from connectPackage.connect import *

if __name__ == "__main__":
    """
    This package attempts to connect to the DB and uses and uses the queries to give the output
    """
    try:
        cursor = DatabaseConnection.connect_to_database()
   
    except Exception as e:
        print("Error accessing database")
        print(e)
        exit()

    ''' 
    This query is pulling a random is pulling data from the db and storing it in the string below
    '''
    emptyListForData = []
    query_string = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID  FROM tProduct"
    results = cursor.execute(query_string)
    for row in results.fetchall():
        emptyListForData.append(row)
    random_row_from_list = random.choice(emptyListForData)
    '''
    This is randomly selecting one row from the data structure and storing it in the variable.
    Including the ProductID, ManufacturerId, and the BrandID
    '''
    productID = random_row_from_list[0]
    description = random_row_from_list[2]
    manufacturerID = random_row_from_list[3]
    brandID = random_row_from_list[4]    


    '''
    This builds on the previous code. It is looking for a specific manufacturerID
    '''
    manufacturer_query_string = "SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = " + str(manufacturerID)
    Manufacturer = cursor.execute(manufacturer_query_string)
    for row in Manufacturer.fetchone():
         Manufacturer = row
    
    '''
    A repeat of the previous code, but instead of ManufactererId, we are looking for a BrandID
    '''
   
    brand_query_string = "SELECT Brand FROM tBrand WHERE BrandID = " + str(brandID)
    Brand = cursor.execute(brand_query_string)
    for row in Brand.fetchone():
        Brand = row

    '''
    This is taking the correct product ID based on the queries above and placing it
    into a query that was given to us on the assignment
    '''
    number_sold_query_string = "SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = " + str(productID) +")"
    number_sold = cursor.execute(number_sold_query_string)
    for row in number_sold.fetchone():
        number_sold = row


    '''
    The final product of the previous code.
    We are taking all of the info from the previous code and making it into a readable line
    to print.
    '''
    Sentence = "The product " + str(Brand) + " is manufactured by " + str(Manufacturer) + ", has a description of " + str(description) + " and at this grocery store location " + str(number_sold) + " have sold."
    print(Sentence)
