import csv
import sqlite3

# with open("week_9/stores.csv") as file_csv:
#   content = list(csv.reader(file_csv))
#   print(content[0])

with sqlite3.connect("week_9/stores.sql") as connection:
  cursor = connection.cursor()

  cursor.execute('''CREATE TABLE stores (
                 store_id INT,
                 store_area INT,
                 items_available INT,
                 daily_customer_count INT,
                 store_sales INT
                 )
                 ''')
  
  file_csv = open("week_9/stores.csv")
  content = csv.reader(file_csv)
  next(content)

  insert = '''INSERT INTO stores (
              store_id, store_area, items_available, daily_customer_count, store_sales)
              VALUES (?,?,?,?,?)'''
  
  cursor.executemany(insert,content)

  rows = cursor.execute("SELECT * FROM stores LIMIT 10").fetchall()
  print(rows)