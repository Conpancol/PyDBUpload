import csv
from Materials import Material
from Utilities import *

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.conpancol
collection = db.mnmaterials
#... result = collection.delete_many({})

def alreadyExists(newID):
    if collection.find({'itemcode': newID}).count() > 0:
        return True
    else:
        return False

with open('data/DBMetals-3364.csv', 'r', encoding='utf-8') as f:
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
            print(material)
        result = find_dimensions(dsc)
        material.setDimensions(result)
        if result == 'NA':
            print(material)

        if alreadyExists(material.getItemCode()):
            print(material)
            continue
        else:
            print(material.getItemCode() + " : added")
            obj_id = collection.insert_one(material.__dict__)

