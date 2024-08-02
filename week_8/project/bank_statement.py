import csv

with open("week_8/project/2024-08-01_transaction_download.csv","r") as file:
  read = csv.reader(file)
  list_item = list(read)

  for transaction in list_item:
    print(transaction)