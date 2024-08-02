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