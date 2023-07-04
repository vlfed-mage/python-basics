# from modules import converters
#
# print(converters.lbs_to_kg(160))
# print(converters.kg_to_lbs(72))

from modules.converters import kg_to_lbs
from modules.converters import lbs_to_kg
from utils.find_max import find_max

from ecommerce import shipping

print(lbs_to_kg(180))
print(kg_to_lbs(75))
print(find_max([1, 2, 5, 8, 4, 2, 6]))

shipping.calc_shipping()
