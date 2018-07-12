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
            raise AttributeError('Material not found')

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
        try:
            with open(csvfile, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, dialect="excel-tab")
                extmaterials = []
                for row in reader:
                    try:
                        orderNum = row[0]
                        itemCode = row[1]
                        quantity = float(row[2])
                        unit = row[3]

                        material = self.lookForMaterial(itemCode)
                        extendedMaterial = ExtMaterials(material)
                        extendedMaterial.setOrderNumber(orderNum)
                        extendedMaterial.setUnit(unit)
                        extendedMaterial.setQuantity(quantity)
                        extmaterials.append(extendedMaterial)
                        logging.info('Material found in DB \t' + itemCode + '\t' + "OK")

                    except AttributeError as ex:
                        logging.info('Material code not found in DB \t' + itemCode + '\t' + "NA")
                        continue

                    except ValueError as ex:
                        logging.info('There is a wrong data format entry. Please check')
                        continue

                self.rfq.setMaterialList(extmaterials)

            rfq_json = self.rfq.__dict__
            rfq_json['materialList'] = self.rfq.to_json()
            output = copy.deepcopy(rfq_json)
            print(json.dumps(output))
            totalMaterials = len(rfq_json['materialList'])
            logging.info('End of RFQ creation  \t' + str(totalMaterials))
            self.rfqcollection.insert_one(output)

        except IOError:
            logging.info('Error opening input file')

    def exportRFQtoCSV(self, code, csvfile):

        labels = []
        labels.append('Id')
        labels.append('OrderId')
        labels.append('ItemId')
        labels.append('Description')
        labels.append('Type')
        labels.append('Quantity')
        labels.append('Unit')

        try:
            path = "./data/export/" + csvfile
            with open(path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f, dialect="excel", delimiter=';')

                if self.alreadyExists(code):

                    cursor = self.rfqcollection.find({'internalCode': code})

                    rfq = cursor.next()

                    header = 'RFQ internal code: ' + str(rfq["internalCode"])
                    writer.writerow([header])
                    info = 'Originator: ' + str(rfq["sender"]) + ' ' + str(rfq["company"])
                    writer.writerow([info])
                    details = 'Received date: ' + str(rfq["receivedDate"])
                    writer.writerow([details])
                    note = 'Note: ' + str(rfq["note"])

                    writer.writerow([note])
                    writer.writerow([''])
                    labels_rwo = '\t'.join(labels)
                    print(labels_rwo)
                    writer.writerow(labels)

                    items = rfq["materialList"]

                    id = 1

                    for item in items:
                        rwo = []
                        rwo.append(str(id))
                        rwo.append(item["orderNumber"])
                        rwo.append(item["itemcode"])
                        description = item["description"]
                        rwo.append(description)
                        rwo.append(item["type"])
                        rwo.append(str(item["quantity"]))
                        rwo.append(str(item["unit"]))

                        if item["category"] == "PLATE":
                            nplates = self.getNumberPlates(item["dimensions"], item["quantity"])
                            rwo.append(str(nplates))
                            rwo.append('PC')

                        writer.writerow(rwo)
                        id += 1

                    for i in range(1,3):
                        writer.writerow([' '])
                    bottom_txt_file = open('./data/Bottom_conditions_EN_FOB.txt', 'r')
                    bottom_txt_rows = bottom_txt_file.readlines()
                    print(bottom_txt_rows)
                    for line in bottom_txt_rows:
                        row = line.replace('\n', ' ')
                        writer.writerow([row])
                    bottom_txt_file.close()

                else:
                    logging.info('RFQ does not exists in DB')

            f.close()

        except IOError:
            logging.info('Problem with file creation')

    def getNumberPlates(self, dimensions, total_area):

        if dimensions.find("MM"):
            dim_values = []
            dims = dimensions.split(',')[1].split('X')
            for dd in dims:

                try:
                    dim_values.append(float( dd.replace(' ','').replace('MM','')))
                except ValueError:
                    dim_values.append(0.0)

            area = dim_values[0] * dim_values[1] * 0.000001
            nplates = format( total_area / (area), '.2f')
            print(dim_values, total_area, nplates)

        return nplates
