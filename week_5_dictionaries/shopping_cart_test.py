dictionary = {'apple':{'price':5,'quantity':5}}

dictionary['pie'] = {'price': 10,'quantity':2}

dictionary['soup'] = {'price': 12,'quantity':1}


print(dictionary)

print(len(dictionary))



ordered_dictionary = sorted(dictionary.items(), key = lambda list:list[1]['quantity'])
for product in ordered_dictionary:
  print(f"{product[1]['quantity']} {product[0]} for ${product[1]['price']}")
