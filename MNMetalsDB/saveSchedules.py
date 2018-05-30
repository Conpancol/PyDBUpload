import csv
import json
from PipeSchedules import PipeSchedule

from pymongo import MongoClient

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

db = client.conpancol
collection = db.schedules
result = collection.delete_many({})

nrow = 0
label = []
data = []

with open('data/pipe-schedules.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, dialect="excel-tab")
    for row in reader:
        if nrow == 0:
            labels = row
        else:
            nps = row[0]
            od = row[1]
            for i in range(2,len(labels)):
                if row[i] != '':
                    wt = row[i]
                    dsc = labels[i]
                    sch = PipeSchedule()
                    sch.setSchedule(dsc)
                    sch.setNps(nps)
                    sch.setOd(od)
                    sch.setWt(wt)
                    sch.setCode(dsc.split()[1])
                    data.append(sch)
        nrow += 1

nrow = 0
print(len(data))
pos = 0
with open('data/pipe-schedules-MM.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, dialect="excel-tab")
    for row in reader:
        if nrow > 0:
            npsMM = row[0]
            odMM = row[1]
            for i in range(2, len(labels)):
                if row[i] != '':
                    wtMM = row[i]
                    data[pos].setNpsMM(npsMM)
                    data[pos].setOdMM(odMM)
                    data[pos].setWtMM(wtMM)
                    print(data[ pos ])
                    obj_id = collection.insert_one(data[ pos ].__dict__)
                    pos +=1

        nrow +=1
