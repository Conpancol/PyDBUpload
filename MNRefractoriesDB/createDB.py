import csv
from Materials import Material
from Utilities import *

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.conpancol
collection = db.mnmaterials

def alreadyExists(newID):
    if collection.find({'itemcode': newID}).count() > 0:
        return True
    else:
        return False

with open('data/DBRefractories.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, dialect="excel-tab")
    for row in reader:
        item = row[1]
        dsc = row[2].rstrip().split(',')
        cat = dsc[0]
        material = Material()
        material.setItemCode(item)
        material.setDescription(','.join(dsc))
        material.setCategory(cat)
        result = find_type(dsc)
        material.setType(result)
        if result == 'NA':
            print("no type: " + material.__str__())
        result = find_dimensions(dsc)
        material.setDimensions(result)
        if result == 'NA':
            print("no dims: " + material.__str__())

        if alreadyExists(material.getItemCode()):
            print("Already present: " + material.__str__())
            continue
        else:
            print(material.getItemCode() + " : added")
            print(material.__dict__)
            obj_id = collection.insert_one(material.__dict__)

