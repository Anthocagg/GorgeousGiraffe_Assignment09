import random
import pyodbc
from connectPackage.connect import *

if __name__ == "__main__":
    """
    This package attempts to connect to the DB and uses queries and its data to make a sentence of it
    """
    try:
        cursor = DatabaseConnection.connect_to_database()
   
    except Exception as e:
        print("Error accessing database")
        print(e)
        exit()
       
    emptyListForData = []
    query_string = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID  FROM tProduct"
    results = cursor.execute(query_string)
    for row in results.fetchall():
        emptyListForData.append(row)
    random_row_from_list = random.choice(emptyListForData)
   
    productID = random_row_from_list[0]
    description = random_row_from_list[2]
    manufacturerID = random_row_from_list[3]
    brandID = random_row_from_list[4]    

    manufacturer_query_string = "SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = " + str(manufacturerID)
    Manufacturer = cursor.execute(manufacturer_query_string)
    for row in Manufacturer.fetchone():
         Manufacturer = row
   
    brand_query_string = "SELECT Brand FROM tBrand WHERE BrandID = " + str(brandID)
    Brand = cursor.execute(brand_query_string)
    for row in Brand.fetchone():
        Brand = row


    number_sold_query_string = "SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold FROM dbo.tTransactionDetail INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = " + str(productID) +")"
    number_sold = cursor.execute(number_sold_query_string)
    for row in number_sold.fetchone():
        number_sold = row

    Sentence = "The product " + str(Brand) + " is manufactured by " + str(Manufacturer) + ", has a description of " + str(description) + " and at this grocery store location " + str(number_sold) + " have sold."
    print(Sentence)
