import pandas as pd
import os

folder_name = '/Users/avanegas/Documents/Invoices'
files = os.listdir('/Users/avanegas/Documents/Invoices')

for file_name in files:
  if file_name.endswith(".csv"):
    data = pd.read_csv(os.path.join(folder_name,file_name))

    # Filter column
    filtered_data = data[data['Category']=='Healthcare']

    # Add filtered data into a master CSV file
    filtered_data.to_csv('/Users/avanegas/Documents/Invoices/Master/master.csv',mode='a')


