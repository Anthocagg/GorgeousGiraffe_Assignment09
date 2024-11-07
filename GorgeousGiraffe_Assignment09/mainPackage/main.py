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
       
    
# List to store product data
product_data_list = []
product_query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
product_results = cursor.execute(product_query)

# Appending rows to the list
for record in product_results.fetchall():
    product_data_list.append(record)

# Randomly select a row from the data list
random_product_row = random.choice(product_data_list)

# Extract specific details from the selected row
prod_id = random_product_row[0]
prod_description = random_product_row[2]
mfr_id = random_product_row[3]
brand_id = random_product_row[4]

# Query for the manufacturer name using the manufacturer ID
mfr_query = "SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = " + str(mfr_id)
mfr_result = cursor.execute(mfr_query)
for row in mfr_result.fetchone():
    mfr_name = row

# Query for the brand name using the brand ID
brand_query = "SELECT Brand FROM tBrand WHERE BrandID = " + str(brand_id)
brand_result = cursor.execute(brand_query)
for row in brand_result.fetchone():
    brand_name = row

# Query for the total number of items sold using the product ID
sales_query = ("SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS TotalItemsSold "
               "FROM dbo.tTransactionDetail "
               "INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID "
               "WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = " + str(prod_id) + ")")
sales_result = cursor.execute(sales_query)
for row in sales_result.fetchone():
    items_sold = row

# Construct and print the final sentence
summary_sentence = (f"The product '{brand_name}' is manufactured by '{mfr_name}', has a description of '{prod_description}', "
                    f"and at this grocery store location, {items_sold} items have been sold.")
print(summary_sentence)
