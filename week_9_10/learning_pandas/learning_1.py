import pandas as pd

# Read CSVs
# r for read
df_csv = pd.read_csv(r'week_9_10/learning_pandas/countries of the world.csv', header = 0, names = ['COUNTRY','GEO'])

# By default, the first row will have the header names (i.e. header = 0)
# If there's no headers, then header = None
# To change header names, write names = ['country','geo'] with the header amount you need

print(df_csv)

# Read Text file
df_txt = pd.read_table(r'week_9_10/learning_pandas/countries of the world.txt')
print(df_txt)


# Read all columns for JSON file

pd.set_option('display.max.columns',40)

# Read JSON file
df_json = pd.read_json(r'week_9_10/learning_pandas/json_sample.json')
print(df_json)


# Read all rows for Excel file
# pd.set_option('display.max.rows',235)

# Read Excel file
df_excel = pd.read_excel(r'week_9_10/learning_pandas/world_population_excel_workbook.xlsx',sheet_name = 'Sheet1')
# If an excel file has multiple sheets, the default output will be the first sheet
print(df_excel)

# Breakdown of data
print(df_excel.info())

# Breakdown of number of rows, columns
print(df_excel.shape) 

#Quick outputs
# First 5 rows
print(df_excel.head())

# First 10 rows
print(df_excel.head(20))

# Last 5 rows
print(df_excel.tail())

# Output a specific column(s)
print(df_excel['Rank'],df_excel['Country'])


# Output the location (i.e. index of the y axis)
print(df_excel.loc[224])
print(df_excel.iloc[224])

# Get column names
print(df_csv.columns)

# loc can change if we change the index, but iloc does not change
# so the iloc will always keep the same numerical index even if the index name changes