import os

# # # Get current directory
# print(os.getcwd())

# # # Get all folders and files within current directory
# print(os.listdir())

# # # Get all folders and files in a different directory
# print(os.listdir("/Users/avanegas/Downloads"))

# # To create a new folder
# os.mkdir("/Users/avanegas/Downloads/a")
# os.mkdir("/Users/avanegas/Downloads/b")

# # To delete a folder
# os.rmdir("/Users/avanegas/Downloads/twilio")

# # To delete a file
# os.remove("/Users/avanegas/Downloads/twilio/data.py")

# # Move file from folder a to folder b
# files_in_a = os.listdir("/Users/avanegas/Downloads/a")
# print(files_in_a)

# # for file in files_in_a:
#   # os.path.join concatenates path into a single path
# a = os.path.join("/Users/avanegas/Downloads/a",file)
# b = os.path.join("/Users/avanegas/Downloads/b",file)
# os.rename(a,b)


# os.mkdir('/Users/avanegas/Documents/GitHub/python-learning/week_9_10/pandas')

# Transfer files from one place to another
# destination = '/Users/avanegas/Documents/GitHub/python-learning/week_9_10/pandas'
# origin = '/Users/avanegas/Downloads/'
# file_name = ['countries of the world.csv','countries of the world.txt','json_sample.json','world_population_excel_workbook.xlsx']

# for file in file_name:
#   original_path = os.path.join(origin,file)
#   destination_path = os.path.join(destination,file)
#   os.rename(original_path,destination_path)
# print("Transfer complete")

# Transfer files from one place to another
destination = '/Users/avanegas/Documents/GitHub/python-learning/week_9_10/learning_pandas'
origin = '/Users/avanegas/Downloads'
file_name = 'world_population.csv'

original_path = os.path.join(origin,file_name)
destination_path = os.path.join(destination,file_name)
os.rename(original_path,destination_path)
print("Transfer complete")
