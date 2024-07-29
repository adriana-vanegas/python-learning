class Robot:
  def __init__(self, name, color, weight):
    self.name = name 
    self.color = color
    self.weight = weight
  def introduce(self):
    print(f"My name is {self.name}")

class Person:
  def __init__(self, name, gender,isSitting):
    self.name = name
    self.gender = gender
    self.isSitting = isSitting

  def sit_down(self):
    self.isSitting = True
    print(f"{self.name} is sitting")

  def stand_up(self):
    self.isSitting = False
    print(f"{self.name} is standing")
  



r1 = Robot('Tom','red',30)
r1.introduce() # you can call functions inside of the class

r2 = Robot('Jerry','blue',40)
r2.introduce()


p1 = Person('Maria','Female',True)
p1.robotOwned = r1
p1.stand_up()
p1.robotOwned.introduce() # You can access the r1 function through the p1.robotOwned

p2 = Person('Bob','Male',False)
p2.robotOwned = r2
p2.sit_down()
p2.robotOwned.introduce() # You can access the r2 function through the p2.robotOwned