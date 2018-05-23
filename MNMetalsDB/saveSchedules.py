import csv
from PipeSchedules import PipeSchedule

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
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
