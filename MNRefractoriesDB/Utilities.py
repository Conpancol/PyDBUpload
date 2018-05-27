import re

types = ['BRICK', 'MORTAR', 'CEMENT', 'FLAGSTONE', 'AL203']

dimdesc = ['MM', '\"', '/', 'TYPE', 'R']

def find_type(description):
    for tp in types:
        if any(tp in s.upper() for s in description):
            return tp
    return 'NA'

def find_dimensions(description):
    dimensions = []
    for lm in description:
        if re.search('\d', lm):
            for dm in dimdesc:
                if any( dm in lm for dm in dimdesc):
                    dimensions.append(lm)
                    break
    if len(dimensions) > 0:
        return ','.join(dimensions).strip()
    else:
        return 'NA'
