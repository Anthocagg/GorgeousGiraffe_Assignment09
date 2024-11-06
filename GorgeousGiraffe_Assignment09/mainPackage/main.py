import random
from connectPackage.connect import*  # Import everything from connectPackage, including conn

# Check if the connection was successful
if conn:
    try:
        # Create a cursor object
        cursor = conn.cursor()

        # Step 1: Submit the query and store the results in a data structure
        query = "SELECT ProductID, [UPC-A], Description, ManufacturerID, BrandID FROM tProduct"
        cursor.execute(query)

        print("Query executed successfully. Fetching data...")

        # Fetch all results and store them in a list of dictionaries
        products = []
        for row in cursor.fetchall():
            product = {
                'ProductID': row.ProductID,
                'UPC': row[1],  # Corresponds to [UPC-A]
                'Description': row.Description,
                'ManufacturerID': row.ManufacturerID,
                'BrandID': row.BrandID
            }
            products.append(product)

        print(f"Retrieved {len(products)} products.")

        # Close the cursor after fetching data
        cursor.close()

        # Step 2: Randomly select one row from the data structure
        selected_product = random.choice(products)

        # Store selected values in variables
        selected_description = selected_product['Description']
        selected_product_id = selected_product['ProductID']
        selected_manufacturer_id = selected_product['ManufacturerID']
        selected_brand_id = selected_product['BrandID']

        print(f"Selected Product ID: {selected_product_id}")
        print(f"Description: {selected_description}")
        print(f"Manufacturer ID: {selected_manufacturer_id}")
        print(f"Brand ID: {selected_brand_id}")

        # Step 3 & 4: Use ManufacturerID to get the manufacturer name
        manufacturer_query = "SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = ?"
        cursor = conn.cursor()
        cursor.execute(manufacturer_query, selected_manufacturer_id)
        manufacturer = cursor.fetchone()
        manufacturer_name = manufacturer[0] if manufacturer else "Unknown Manufacturer"
        print(f"Manufacturer Name: {manufacturer_name}")

        # Step 5: Use BrandID to get the brand name
        brand_query = "SELECT Brand FROM tBrand WHERE BrandID = ?"
        cursor.execute(brand_query, selected_brand_id)
        brand = cursor.fetchone()
        brand_name = brand[0] if brand else "Unknown Brand"
        print(f"Brand Name: {brand_name}")

        # Step 6: Query for number of items sold using ProductID
        items_sold_query = """
            SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
            FROM dbo.tTransactionDetail
            INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
            WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = ?)
        """
        cursor.execute(items_sold_query, selected_product_id)
        items_sold = cursor.fetchone()
        number_of_items_sold = items_sold[0] if items_sold else 0
        print(f"Number of Items Sold: {number_of_items_sold}")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Ensure the connection is closed
        conn.close()
        print("Connection closed.")
else:
    print("Failed to establish a connection.")