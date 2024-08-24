import csv

with open("week_8_standard_library/project/2024-08-01_transaction_download.csv","r") as file:
  all_transactions = list(csv.DictReader(file))
  
  for transaction in all_transactions:
    print(transaction['Transaction Date'],transaction['Category'],transaction['Debit'])



