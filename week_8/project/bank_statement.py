import csv
import sqlite3

file = open("week_8/project/2024-08-01_transaction_download.csv","r") 
contents = csv.reader(file)
  


# Step 1 create a connection with the SQL database
with sqlite3.connect("bank_transaction.sql") as transaction_db:

#   # transaction_db.execute("DROP TABLE IF EXISTS bank_transaction")
#   # print("Data Dropped")
# # Step 2 create a cursor object to execute
  cursor = transaction_db.cursor()

# Step 2 create a table
  # cursor.execute('''CREATE TABLE bank_transaction(
  #                           transaction_date datetime,
  #                           posted_date datetime,
  #                           card_no INT,
  #                           description TEXT,
  #                           category TEXT,
  #                           debit INT,
  #                           credit INT)''')

# Step 3 prep insert into table
  # insert_records = '''INSERT INTO bank_transaction (
  #                     transaction_date,posted_date,card_no,
  #                     description,category,debit,credit) 
  #                     VALUES(?,?,?,?,?,?,?)'''

# Step 4 Insert records
  # cursor.executemany(insert_records,contents)


  cursor.execute("SELECT * FROM bank_transaction")

  select_all = cursor.fetchall()
  print(select_all)



# Step 5 Save changes
  # transaction_db.commit()

# file.close()