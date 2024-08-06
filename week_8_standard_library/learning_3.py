# CSV

import csv

file_path = "week_8/data.csv"

with open(file_path,"w") as file:
  writer = csv.writer(file)
  writer.writerow(["transaction","product_id","price"])
  writer.writerow(["ABC123","ABC123",10])
  writer.writerow(["BCA231","BCA231",9])
  writer.writerow(["CAB312","CAB312",8])

with open(file_path, 'r') as read_file:
  reader = csv.reader(read_file)
  # print([i for i in reader])
  # or 
  print(list(reader))

  # Reader really just outputs the CSV as it is
  # Like:
  # [name,id,city],['Adriana',1,'Seattle']

  # DictReader outputs the CSV as if it's a dictionary with the corresponding headers
  # Like
  # {'name': 'Adriana','id': 1, 'city':'Seattle'}


  # If you ever want to see the value of the 