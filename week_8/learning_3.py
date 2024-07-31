import csv
import os

try:
  file_path = "/Users/avanegas/Documents/GitHub/python-learning/week_8/data.csv"
  print(f"File will be created at {file_path}")
  with open(file_path,"w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction","product_id","price"])
    writer.writerow(["ABC123","ABC123",10])
    writer.writerow(["BCA231","BCA231",9])
    writer.writerow(["CAB312","CAB312",8])
  
  print(f"File written successfully at {file_path}")

except Exception as e:
  print(f"Error occurred {e}")