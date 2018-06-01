import csv
import copy
import json
import datetime
import logging

from RequestForQuotes import *
from ExtMaterials import ExtMaterials

from pymongo import MongoClient


class RFQCreator:

    def __init__(self):
        """clase que crea RFQs en el formator necesario para guardar en la DB"""
        self.rfq = RequestForQuotes()
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.conpancol
        self.collection = self.db.mnmaterials
        self.rfqcollection = self.db.rfquotes
        logging.basicConfig(filename='logs/rfqcreator.log', level=logging.DEBUG)

    def lookForMaterial(self, itemCode):

        if self.collection.find({'itemcode': itemCode}).count() > 0 :
            material = self.collection.find_one({'itemcode': itemCode})
            return material
        else:
            raise Exception('Material not found')

    def alreadyExists(self, newID):
        if self.rfqcollection.find({'internalCode': newID}).count() > 0:
            logging.info('RFQ already exists  \t' + str(newID))
            return True
        else:
            logging.info('RFQ does not exists  \t' + str(newID))
            return False

    def setRFQInformation(self, internalCode, externalCode, sender, company, receivedDate):
        self.rfq.setIntenalCode(internalCode)
        self.rfq.setExternalCode(externalCode)
        self.rfq.setSender(sender)
        self.rfq.setCompany(company)
        self.rfq.setReceivedDate(receivedDate)
        dt = datetime.datetime.now()
        self.rfq.setProcessedDate(dt.strftime('%d/%m/%Y'))

    def addRFQNote(self, note):
        self.rfq.setNote(note)

    def createRFQfromCSV(self, csvfile):
        with open(csvfile, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect="excel-tab")
            extmaterials = []
            for row in reader:
                orderNum = row[0]
                itemCode = row[1]
                quantity = float(row[2])
                unit = row[3]
                try:
                    material = self.lookForMaterial(itemCode)
                    extendedMaterial = ExtMaterials(material)
                    extendedMaterial.setOrderNumber(orderNum)
                    extendedMaterial.setUnit(unit)
                    extendedMaterial.setQuantity(quantity)
                    extmaterials.append(extendedMaterial)
                except Exception as ex:
                    logging.info('Material code not found in DB \t' + itemCode)
                    continue

            self.rfq.setMaterialList(extmaterials)

        rfq_json = self.rfq.__dict__
        rfq_json['materialList'] = self.rfq.to_json()
        output = copy.deepcopy(rfq_json)
        print(json.dumps(output))
        totalMaterials = len(rfq_json['materialList'])
        logging.info('End of RFQ creation  \t' + str(totalMaterials))
        self.rfqcollection.insert_one(output)
