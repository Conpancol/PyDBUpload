import csv
from Materials import Material
from Utilities import *
from pymongo import MongoClient
import logging
import json


class MaterialCreator:

    def __init__(self):
        """clase que crea MATERIALS en el formator necesario para guardar en la DB"""
        dev = False
        with open('config/dbconfig.json', 'r') as f:
            config = json.load(f)
            if dev:
                dburl = config['DEV']['DBURL']
                dport = int(config['DEV']['DBPORT'])
                self.client = MongoClient(dburl, dport)
            else:
                dburl = config['PROD']['DBURL']
                self.client = MongoClient(dburl)

        self.db = self.client.conpancol
        self.collection = self.db.mnmaterials
        # ... result = self.collection.delete_many({})
        logging.basicConfig(filename='logs/mtcreator.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d-%y %H:%M')

    def alreadyExists(self, newID):
        if self.collection.find({'itemcode': newID}).count() > 0:
            return True
        else:
            return False

    def createQuotefromCSV(self, csvfile):
        with open(csvfile, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect="excel-tab")
            filename = csvfile.split('/')[-1]
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
                    logging.info('No type for  \t' + material)
                result = find_dimensions(dsc)
                material.setDimensions(result)
                if result == 'NA':
                    logging.info('No dimensions for  \t' + material)
                if self.alreadyExists(material.getItemCode()):
                    logging.info('Material already exist  \t' + str(material.getItemCode()))
                    continue
                else:
                    print(material.getItemCode() + " : added")
                    obj_id = self.collection.insert_one(material.__dict__)
                    logging.info('Added  \t' + str(material.getItemCode() + '\t' + filename))
