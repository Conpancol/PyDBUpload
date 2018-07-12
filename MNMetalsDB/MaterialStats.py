from pymongo import MongoClient
import json
import logging
from Utilities import *


class MaterialStats:
    """DB statistics"""
    def __init__(self):
        dev = True
        with open('config/dbconfig.prod', 'r') as f:
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

        logging.basicConfig(filename='logs/mtstats.log',
                            level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d-%y %H:%M')

        self.categories = {}
        self.types = {}

    def getProjections(self, paramlist):
        select = {key: 1 for key in paramlist}
        select["_id"] = 0
        return self.collection.find({}, select)

    def getCategoryStatS(self):

        vars = ['category']
        vars.append('type')

        cursor = self.getProjections(vars)

        for data in cursor:
            key = data["category"]
            if key in self.categories:
                self.categories[key] += 1
            else:
                self.categories[key] = 1

            key = data["type"]
            if key in self.types:
                self.types[key] += 1
            else:
                self.types[key] = 1

        for key in self.categories:
            print(key + '\t' + str(self.categories[key]))

        for key in self.types:
            print(key + '\t' + str(self.types[key]))

    def checkMaterialType(self):

        vars = []
        vars.append('description')
        vars.append('type')

        cursor = self.getProjections(vars)

        idx = 0
        for data in cursor:
            dsc = data["description"]
            type = data["type"].strip()
            type_xcheck = find_type(dsc.split(','))
            idx += 1
            if type != type_xcheck:
                print(str(idx) + '\t' + dsc + '\t' + type + '\t' + type_xcheck)


mat = MaterialStats()
mat.getCategoryStatS()
mat.checkMaterialType()
