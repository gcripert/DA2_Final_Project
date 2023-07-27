
# Importing necessary modules

import csv
import sqlite3
from datetime import datetime
import pandas as pd



def create_table_from_csv(sql, csv_file_path, table_name):

    print(f"creating table {table_name} from {csv_file_path}")

    # Using 'reader' to read the headers; these will be the column names for the table

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)

    # Determining the data types for each column based on the first row of data in the csv with no empty values

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if all(row.values()):
                sample_row = row
                break

    column_types = {}
    for header, value in sample_row.items():
        if value.isdigit():

            # Checking if the value is an integer

            column_types[header] = 'INTEGER'
        else:
            try:
                # Checking if the value is a float

                float_value = float(value)
                if float_value.is_integer():
                    column_types[header] = 'INTEGER'
                else:
                    column_types[header] = 'REAL'
            except ValueError:
                try:
                    # Checking if the value is a date

                    datetime.strptime(value, '%Y-%m-%d')
                    column_types[header] = 'DATE'
                except ValueError:

                    # If none of the above conditions are met, consider the value as text

                    column_types[header] = 'TEXT'

    # Generating the sql create table statement

    columns = ", ".join([f"{header} {column_types[header]}" for header in headers])
    create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"

    # Creating the table

    print(f'executing sql query {create_table_sql}')

    sql.execute(create_table_sql)



# Function for determining if the table is empty

def table_is_empty(sql, table_name):
    print(f'checking if table {table_name} is empty')
    sql.execute(f'SELECT COUNT(*) FROM {table_name}')
    count = sql.fetchone()[0]
    return count == 0



# Function for importing data from csv into sqlite table


def import_data_from_csv(csv_file_path, db_file_path, table_name):
    print(f'importing table {table_name} from {csv_file_path} into {db_file_path}')

    # Connecting to the SQLite database. uri=True will create the database if it does not already exist

    conn = sqlite3.connect(db_file_path, uri=True)
    sql = conn.cursor()

    # Creating the table (if it doesn't exist) based on the csv data

    create_table_from_csv(sql, csv_file_path, table_name)

    # Checking if the table is not empty

    if not table_is_empty(sql, table_name):
        print(f"The table '{table_name}' is not empty. Data import skipped.")
        conn.close()
        return

    # Reading data from the csv file and inserting it into the SQLite table

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        # Skipping the header row

        next(csvreader)

        for row in csvreader:

            # Creating sql INSERT for data row
            query = f'INSERT INTO {table_name} VALUES ({", ".join("?" * len(row))})', row
            print(f'executing sql query {query}')

            sql.execute(query)

    # Committing the changes and closing the connection

    conn.commit()
    conn.close()


# Testing

def print_first_five_rows(db_file_path, table_name):

    # Connecting to the SQLite database

    conn = sqlite3.connect(db_file_path)
    sql = conn.cursor()

    # Executing the SELECT query to retrieve the first five rows from the table

    sql.execute(f'SELECT * FROM {table_name} LIMIT 5')
    rows = sql.fetchall()

    if not rows:
        print(f"The table '{table_name}' is empty.")
    else:

        # Printing the first five rows

        print(f"First five rows of table '{table_name}':")
        for row in rows:
            print(row)

    # Closing the connection

    conn.close()

# Function for querying the database and printing the results

def query_and_print(database_file, query):
    try:
        # Connecting to the database

        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        # Executing the query

        print(f'executing and printing sql query {query}')

        cursor.execute(query)

        # Fetching all results

        results = cursor.fetchall()

        if len(results) > 0:

            # Printing the column headers

            column_names = [description[0] for description in cursor.description]
            print('\t'.join(column_names))

            # Printing the results

            for row in results:
                print('\t'.join(str(value) for value in row))
        else:
            print("No results found.")

    except sqlite3.Error as e:
        print("An error occurred:", e)

    finally:

        # Closing the connection

        if connection:
            connection.close()

# Call the function to import data from the csv to the SQLite database


import_data_from_csv('Data/articles.csv', 'Data\\HM_data.db', 'articles')
import_data_from_csv('Data/customers.csv', 'Data\\HM_data.db', 'customers')
import_data_from_csv('Data/transactions_train.csv', 'Data\\HM_data.db', 'transactions')

# Verifying the data was properly imported


print_first_five_rows('Data\\HM_data.db', 'articles')
print_first_five_rows('Data\\HM_data.db', 'customers')
print_first_five_rows('Data\\HM_data.db', 'transactions') 

# Checking the date range of the data

query_and_print('Data\\HM_data.db', 'Select * from transactions order by t_dat asc limit 5')
query_and_print('Data\\HM_data.db', 'Select * from transactions order by t_dat desc limit 5')

# Checking the age range of the data

query_and_print('Data\\HM_data.db', "Select min(age), max(age) from customers where age!=''")

# Connecting to sqlite

conn = sqlite3.connect('Data\\HM_data.db')
sql = conn.cursor()

# Creating indexes for age and price to speed up sqlite queries

print(f'creating indexes on age and price columns on customers and transactions tables')

sql.execute('CREATE INDEX IF NOT EXISTS idx_age ON Customers (age)')
sql.execute('CREATE INDEX IF NOT EXISTS idx_price ON Transactions (price)')

# Removing records with empty ages and prices

print('removing records with empty age or price')

sql.execute("DELETE FROM customers WHERE age = ''")
sql.execute("DELETE FROM transactions WHERE price = ''")


# Origin of 590x, which was used in the data as the multiplier of price to get dollar values. https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/discussion/310496 
# Joining transactions and customers to analyze customer spending
# Grouping by age range, separated by decade using CASE
# Using COUNT, ROUND, and SUM to calculate percentages and totals

query="""
SELECT CASE
         WHEN age BETWEEN 16 AND 24 THEN '16-24'
         WHEN age BETWEEN 25 AND 34 THEN '25-34'
         WHEN age BETWEEN 35 AND 44 THEN '35-44'
         WHEN age BETWEEN 45 AND 54 THEN '45-54'
         ELSE '55+'
       END AS age_group, 
       COUNT(age) AS num_customers, 
       ROUND(COUNT(age)*100.0/SUM(COUNT(age)) OVER(),2) AS population_share_percentage,
       ROUND(SUM(price)*590,2) AS transaction_total, 
       ROUND(SUM(price)*590/COUNT(price),2) AS transaction_average
FROM Transactions
INNER JOIN Customers ON Transactions.customer_id = Customers.customer_id
GROUP BY age_group;
"""

# Executing query and storing the results in a dataframe

print(f'executing sql query {query}')

sql.execute(query)
results = sql.fetchall()
df = pd.DataFrame(results, columns=['age_group', 'num_customers', 'population_share_percentage', 'transaction_total', 'transaction_average'])

# Saving results data to csv for use in a Tableau dashboard visualization

print('saving results to age_data.csv')

df.to_csv('age_data.csv')

print('completed')


