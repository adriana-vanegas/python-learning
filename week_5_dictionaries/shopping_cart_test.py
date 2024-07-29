dictionary = {'Apple Juice':{'price':5.99,'quantity':2}}

dictionary['pie'] = {'price': 10,'quantity':2}

dictionary['soup'] = {'price': 12,'quantity':1}


print(dictionary)

print(len(dictionary))



ordered_dictionary = sorted(dictionary.items(), key = lambda list:list[1]['quantity'])
for product in ordered_dictionary:
  print(f"{product[1]['quantity']} {product[0]} for ${product[1]['price']}")

val = '3.99'
val = val.replace('.','')
print(val)