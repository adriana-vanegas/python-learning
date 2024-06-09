from generate_land import generate_land
import os #creates a folder

os.makedirs("output",exist_ok=True) 
  #creates a folder called Output
  #exist_ok means that if I run this output again, I won't have an error if the output file already exists. It will let the code run



noise = [1,5,10,25,30,50,75,100,250]

for num in noise:
  output = generate_land(200,200,num)
  #print (output)
  filename = os.path.join("output",f"test_{num}.txt")

  with open(filename, "w") as f: 
    #w stands for write (writing the file)
    #f stands for file
    f.write(output)