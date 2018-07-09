import csv
import json
from ButtWeldingFittings import ButtWeldingFitting

from pymongo import MongoClient


class FittingSaver:

    def __init__(self):
        dev = True
        with open('config/dbconfig.json', 'r') as f:
            config = json.load(f)
            if dev:
                dburl = config['DEV']['DBURL']
                dport = int(config['DEV']['DBPORT'])
                client = MongoClient(dburl, dport)
            else:
                dburl = config['PROD']['DBURL']
                client = MongoClient(dburl)

        self.db = client.conpancol
        self.collection = self.db.fittings
        result = self.collection.delete_many({})

        self.size = ''
        self.schedule = ''
        self.dimensions = ''
        self.weight = 0.0

    def saveFittingTableFromCSV(self, file_list):

        cvsfile = 'data/fittings/' + file_list[0]
        category = file_list[1]
        standards = file_list[2]
        print(cvsfile + " " + category + " " + standards)
        try:
            with open(cvsfile, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, dialect="excel-tab")

                headers = next(reader)
                print(headers)

                for row in reader:
                    fitting = ButtWeldingFitting()
                    fitting.setCategory(category)
                    fitting.setStandars(standards)

                    pos = 0
                    dims = [ ]

                    if headers[1] != 'schedule':
                        self.size = row[0] + '\"' + ' X ' + row[1] + '\"'
                        self.schedule = row[2]
                        pos = 3
                    elif headers[1] == 'schedule':
                        self.size = row[0] + '\"'
                        self.schedule = row[1]
                        pos = 2

                    for idx in range(pos,len(headers)-1):
                        dims.append(headers[idx] + '=' + row[idx] + 'MM')

                    self.dimensions = ' X '.join(dims)
                    self.weight = float(row[-1])

                    fitting.setPipeSize(self.size)
                    fitting.setSchedule(self.schedule)
                    fitting.setDimensions(self.dimensions)
                    fitting.setWeight(self.weight)

                    obj_id = self.collection.insert_one(fitting.__dict__)

        except Exception as ex:
            print(ex)

input_file_list = []
input_file_list.append(['fittings-SL-stubends.csv','SHORT LENGTH STUB ENDS','ASTM A403 / A815 ASME B16.9'])
input_file_list.append(['fittings-elbows-90-LR.csv','ELBOWS 90º LONG RADIUS','ASTM A403 / A815 ASME B16.9'])
input_file_list.append(['fittings-elbows-45-LR.csv','ELBOWS 45º LONG RADIUS','ASTM A403 / A815 ASME B16.9'])
input_file_list.append(['fittings-elbows-90-SR.csv','ELBOWS 90º SHORT RADIUS','ASTM A403 ASME B16.28 / ASME B16.9'])
input_file_list.append(['fittings-endcaps.csv','END CAPS','ASTM A403 / A815 ASME B16.9'])
input_file_list.append(['fittings-conc-reducers.csv','CONCENTRIC REDUCERS','ASTM A403 / A815 ASME B16.9'])
input_file_list.append(['fittings-eccen-reducers.csv','ECCENTRIC REDUCERS','ASTM A403 / ASME B16.9'])
input_file_list.append(['fittings-equal-tees.csv','EQUAL TEES','ASTM A403 / A815 ASME B16.9'])
input_file_list.append(['fittings-reducing-tees.csv','REDUCING TEES','ASTM A403 / A815 ASME B16.9'])

saver = FittingSaver()

for file in input_file_list:
    saver.saveFittingTableFromCSV(file)
