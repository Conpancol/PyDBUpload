from DBUtlities import *
from readDB import *
from Utilities import *


nps = "16\""
sch = "SCH40"

result = get_tube_diameters(nps, sch)
print(result['odMM'], result['idMM'])

get_plate_dimensions()

get_tube_dimensions()

get_bar_dimensions()

description = "STUB-END, 16\", SCH40, BW, TITANIUM, SHORT PATTER, SEAMLESS, ASME B16.9"

print("type: " + find_type(description.split(',')))





