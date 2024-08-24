import csv

class Store:
  store_list = []
  def __init__(self, store_id:int, store_area:int, items_available:int, daily_customer_count:int, store_sales:int):
    self.store_id = store_id 
    self.store_area = store_area
    self.items_available = items_available
    self.daily_customer_count = daily_customer_count
    self.store_sales = store_sales
    self.store_list.append(self)
  
  def view(self):
    print([x for x in self.store_list])

  @classmethod
  def instantiate(cls):
    with open("week_9/stores.csv") as file:
      content = list(csv.DictReader(file))

      for values in content:
        Store(
          store_id = values.get('\ufeffStore_ID'),
          store_area = values.get('Store_Area'),
          items_available = values.get('Items_Available'),
          daily_customer_count = values.get('Daily_Customer_Count'),
          store_sales = values.get('Store_Sales')
        )

  def __repr__(self):
    return f"store_id: {self.store_id}, store_area: {self.store_area}, items_available: {self.items_available}, daily_customer_count: {self.daily_customer_count}, store_sales: {self.store_sales}"

Store.instantiate()
print(Store.store_list)

# with open("week_9/stores.csv") as file:
#   content = list(csv.DictReader(file))
#   print(content)