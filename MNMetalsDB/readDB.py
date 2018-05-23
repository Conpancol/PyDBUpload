import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.conpancol
collection = db.mnmetals

NPSSTD = ['1/8\"', '1/4\"','3/8\"','1/2\"','3/4\"','1\"','1-1/4\"','1-1/2\"','2\"','2-1/2\"','3\"','3-1/2\"','4\"','5\"','6\"','8\"','10\"','12\"','14\"','16\"','18\"','20\"','24\"','30\"','36\"']


def get_plate_dimensions():
    cursor = collection.find({"category": "PLATE"})
    for record in cursor:
        dimensions = record["dimensions"].split(',')
        dimMM = dimensions[-1].replace('MM', '').split('X')
        dimX1 = float(dimMM[0].replace(' ',''))
        dimY1 = float(dimMM[1].replace(' ',''))
        dimZ1 = float(dimMM[2].replace(' ',''))
        print(dimX1,dimY1,dimZ1)

def get_tube_dimensions():
    cursor = collection.find({"category": "PIPE"})
    for record in cursor:
        dims = record["dimensions"].split(',')
        result = {}
        hasNPS = [x for x in dims if '\"' in x]
        if len(hasNPS) > 0:
            result['nps'] = hasNPS[0]
        hasSch = [x for x in dims if 'SCH' in x]
        if len(hasSch) > 0:
            result['sch'] = hasSch[0]
        print(result)

def get_bar_dimensions():
    cursor = collection.find({"category": "BAR"})
    for record in cursor:
        dims = record[ "dimensions" ].split(',')
        print(dims)

def get_material_list( csv_file):

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, dialect="excel-tab")
        for row in reader:
            order_number = row[0]
            code = row[1]
            qty = row[2]
            unit = row[3]
            print(order_number, code, qty, unit)

