import pymongo
from pymongo import MongoClient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tkinter_friendend"]
mycol = mydb["users"]