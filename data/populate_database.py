import pandas as pd
import sqlite3

# Load Spreadsheet 0
df0 = pd.read_csv('data/shipping_data_0.csv')

# Load Spreadsheet 1
df1 = pd.read_csv('data/shipping_data_1.csv')

# Load Spreadsheet 2
df2 = pd.read_csv('data/shipping_data_2.csv')

# Connect to SQLite database
conn = sqlite3.connect('forage-walmart-task-4/shipment_database.db')
cursor = conn.cursor()

# Insert data from Spreadsheet 0 into the database
df0.to_sql('spreadsheet0_data', conn, if_exists='replace', index=False)

# Combine data from Spreadsheet 1 and Spreadsheet 2
combined_data = pd.merge(df1, df2, on='shipping_identifier')

# Iterate through the combined data to insert rows into the database
for index, row in combined_data.iterrows():
    shipping_identifier = row['shipping_identifier']
    product_name = row['product_name']
    quantity = row['quantity']
    origin = row['origin']
    destination = row['destination']

    # You need to adjust the table and column names based on your database schema
    query = f"INSERT INTO your_table_name (shipping_identifier, product_name, quantity, origin, destination) " \
            f"VALUES ('{shipping_identifier}', '{product_name}', {quantity}, '{origin}', '{destination}')"

    cursor.execute(query)

# Commit changes and close connection
conn.commit()
conn.close()
