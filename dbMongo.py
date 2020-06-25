from pymongo import MongoClient
import datetime

cliente = MongoClient('mongodb://localhost:27017/')

dbMongo = cliente.TrabalhoNoSQL
