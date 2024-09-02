from pymongo import MongoClient

connector = MongoClient("mongodb://localhost:27017/")

print(connector)