
# table = tabula.read_pdf(pdf_file, pages='1')


import psycopg2
import csv
import tabula


# Database connection parameters
hostname = 'localhost'
username = 'newuser'
password = 'newpassword'
database = 'mydatabase'

# PDF file path, CSV file path and table name
pdf_file = 'https://nbviewer.org/github/kuruvasatya/Scraping-Tables-from-PDF/blob/master/data1.pdf'
csv_file = 'output.csv'
table_name = 'bureaux_de_change'

# Convert pdf table to csv
tabula.convert_into(pdf_file, csv_file, output_format='csv', pages='all')


# Connect to the database
conn = psycopg2.connect(
    host=hostname,
    user=username,
    password=password,
    dbname=database
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Create the table if it does not exist
cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, bdc_name text, address text, location text)")

# Open the CSV file and insert data into the table
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header row
    for row in reader:
        id, name, address, location = row
        cur.execute(f"INSERT INTO {table_name} (bdc_name, address, location) VALUES (%s, %s, %s)", (name, address, location))


# Commit the changes to the database
conn.commit()

# Close the database connection
cur.close()
conn.close()