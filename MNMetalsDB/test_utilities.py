from DBUtlities import *
from readDB import *

nps = "16\""
sch = "SCH40"

result = get_tube_diameters(nps, sch)
print(result['odMM'], result['idMM'])

get_plate_dimensions()

get_tube_dimensions()

get_bar_dimensions()




