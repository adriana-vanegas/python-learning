
class Room:

  def __init__(self, room_name:str, room_quant:int,max_capacity:int, price_per_night:float):
    assert room_quant >= 0, 'Room quantity must be a valid number'
    assert max_capacity >=0, 'Max capacity must be a valid number'
    assert max_capacity >=0, 'Max capacity must be a valid number'

    self.room_name = room_name
    self.room_quant = room_quant
    self.max_capacity = max_capacity
    self.price_per_night = price_per_night

  def __str__(self):
    return f"{self.room_name}, quant: {self.room_quant}, max cap: {self.max_capacity}, price: {self.price_per_night:.2f}"


class Booking:
  def __init__(self):
    self.rooms_available = []

  def add_room(self,room_name, room_quant, max_capacity, price_per_night):
    room = Room(room_name, room_quant, max_capacity, price_per_night)
    self.rooms_available.append(room)
    print(f"Room added: {room}")

  def view_rooms(self):
    for room in self.rooms_available:
      print(room)
  
  def book_a_room(self, room_to_book, quantity):
    for room in self.rooms_available:
      if room.room_name in room_to_book:
        if room.room_quant - quantity > 0:
          room.room_quant = room.room_quant - quantity
          price = room.price_per_night * quantity
          print(f"{room_to_book} is booked for ${price:.2f}")
        else:
          print(f"{room_to_book} has no availability")

  def cancel_a_room(self,room_to_cancel, quantity):
    for room in self.rooms_available:
      print(room.room_quant)
      # if room.room_name in room_to_cancel:
      #     room.room_quant = room.room_quant + quantity
      #     return_amount = room.price_per_night * quantity
      #     print(f"{room_to_cancel} is cancelled for ${return_amount:.2f}")



booking = Booking()
booking.add_room('Grand King',3,3,700)
booking.add_room('Classic King',2,3,600)
booking.add_room('Classic Queen',4,2,300)
booking.add_room('Petite Queen',4,2,250)
booking.add_room('Petite Full',2,2,180)



booking.book_a_room('Petite Queen',3)

booking.view_rooms()

booking.cancel_a_room('Petite Queen',2)
