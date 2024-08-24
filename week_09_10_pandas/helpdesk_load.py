import sqlite3
import csv

# Step 1: create a sqlite3 db

with sqlite3.connect("week_9/helpdesk_db.sql") as connection:
  # Step 2: Cursor
  cursor = connection.cursor()

  # cursor.execute('DROP TABLE helpdesk')

  # # Step 3: Create a table
  # cursor.execute('''CREATE TABLE helpdesk (
  #                id INTEGER,
  #                subject TEXT,
  #                body TEXT,
  #                answer TEXT,
  #                type TEXT,
  #                queue TEXT,
  #                priority TEXT,
  #                language TEXT,
  #                business_type TEXT,
  #                tag_1 TEXT,
  #                tag_2 TEXT,
  #                tag_3 TEXT,
  #                tag_4 TEXT,
  #                tag_5 TEXT,
  #                tag_6 TEXT,
  #                tag_7 TEXT,
  #                tag_8 TEXT,
  #                tag_9 TEXT
  #                )''')
  
  # # Step 4 insert data into table
  # # Step 4a open csv
  # file = open("week_9/helpdesk_customer_tickets.csv", 'r')
  # content = csv.reader(file)
  # next(content)

  # # Automate ? build for inserting data
  # # count_setup = list(content)
  # # num_of_q = "?"+",?"*(len(list(count_setup[0]))-1)

  # insert = f'''INSERT INTO helpdesk (
  #             id,subject,body,answer,type,queue,priority,language,business_type,
  #             tag_1,tag_2,tag_3,tag_4,tag_5,tag_6,tag_7,tag_8,tag_9) 
  #             VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
  
  # # Step 4b insert data
  # insert = cursor.executemany(insert, content)
  file.close()
  # Step 5 check data
  rows = cursor.execute("SELECT id,subject,language FROM helpdesk WHERE language = 'en'").fetchall()
  print(rows)

  # connection.commit()



# How to count number of columns
# with open("week_9/helpdesk_customer_tickets.csv", 'r') as file:
#   content= list(csv.reader(file))
#   print(content)
#   # if you want to see the content of the csv, it needs to be in a list or use DictReader

#   print(len(content[0]))
#   num_of_q = "?"+",?"*(len(content[0])-1)
#   print(num_of_q)