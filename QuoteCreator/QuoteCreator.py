import csv
import copy
import json
import datetime
import logging

from Quotes import *
from QuotedMaterials import QuotedMaterials

from pymongo import MongoClient


class QuoteCreator:

    def __init__(self):
        """clase que crea QUOTES en el formator necesario para guardar en la DB"""
        self.quote = Quotes()
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.conpancol
        self.collection = self.db.quotes
        logging.basicConfig(filename='logs/qcreator.log', level=logging.DEBUG)

    def lookForMaterial(self, itemCode):

        if self.collection.find({'itemcode': itemCode}).count() > 0 :
            material = self.collection.find_one({'itemcode': itemCode})
            return material
        else:
            raise Exception('Material not found')

    def setQuoteInformation(self, internalCode, externalCode, providerCode, provider, contact, receivedDate):
        self.quote.setIntenalCode(internalCode)
        self.quote.setExternalCode(externalCode)
        self.quote.setProviderCode(providerCode)
        self.quote.setContactName(contact)
        self.quote.setProviderName(provider)
        self.quote.setReceivedDate(receivedDate)
        dt = datetime.datetime.now()
        self.quote.setProcessedDate(dt.strftime('%d/%m/%Y'))

    def createQuotefromCSV(self, csvfile):
        with open(csvfile, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, dialect="excel-tab")
            qtmaterials = []
            for row in reader:
                orderNum = row[0]
                itemCode = row[1]
                quantity = float(row[2])
                unit = row[3]
                try:
                    material = self.lookForMaterial(itemCode)
                    quotedMaterial = QuotedMaterials(material)
                    quotedMaterial.setOrderNumber(orderNum)
                    quotedMaterial.setUnit(unit)
                    quotedMaterial.setQuantity(quantity)
                    qtmaterials.append(quotedMaterial)
                except Exception as ex:
                    logging.info('Material code not found in DB \t' + itemCode)
                    continue

            self.quote.setMaterialList(qtmaterials)

        quote_json = self.quote.__dict__
        quote_json['materialList'] = self.quote.to_json()
        output = copy.deepcopy(quote_json)
        print(json.dumps(output))
        totalMaterials = len(quote_json['materialList'])
        logging.info('End of Quote creation  \t' + str(totalMaterials))
        # ... self.rfqcollection.insert_one(output)
