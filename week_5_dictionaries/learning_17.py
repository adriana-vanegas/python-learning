# Find the most frequently used letter
from pprint import pprint
sentence = "This is a common interview question"

build = {}

# Create a dictionary of the unique letters in the sentence
for val in set(sentence.lower().replace(' ','')):
  build[val]=0
# print(build)


for add in sentence:
  if add in build:
    build[add]+=1
# print(build)

ordered = sorted(build.items(),key=lambda key_val: key_val[1],reverse=True)
pprint(ordered, width = 1) #Pretty print - width determines the number of "characters" in 
# each line, in this case each key value pair
print(ordered[0])
