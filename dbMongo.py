from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017/')#conecta no banco mongo

dbMongo = cliente.TrabalhoNoSQL #usar o banco TrabalhoNoSQL
