# Version 1
# import spacepackage.calc

# Version 2
from spacepackage.calc import planet_mass,planet_vol

class Planet:

  def number():
    return "There are 8 planets"
  

  def dwarf():
    return "There is 1 dwarf plane"

#Version 1
# print(spacepackage.calc.planet_mass())

#Version 2
print(planet_mass())
print(planet_vol())