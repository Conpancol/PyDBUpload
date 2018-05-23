from PipeSchedules import PipeSchedule

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.conpancol
collection = db.schedules

def get_tube_diameters(nps, sch):
    """Returns OD and ID from tube/pipe NPS and SCHEDULE IN MM"""
    cursor = collection.find({"$and": [{"nps": nps}, {"code": sch}]})
    result = cursor.explain()['executionStats']['nReturned']
    if result > 0:
        odmm = cursor[0]['odMM']
        wtmm = cursor[0]['wtMM']
        idmm = odmm - (2.0* wtmm)
        return {'odMM': odmm,'idMM': idmm}
    else:
        return {'odMM': 0.0,'idMM': 0.0}
