# OPTION 1:

from sales import calculate_shipping, calculate_tax
  # from sales import * (avoid importing all, just import what you need)

calculate_shipping()
calculate_tax()



# OPTION 2:
import sales

sales.calculate_shipping()
#if you just import sales file, you need to use it as a method sales.
