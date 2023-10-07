import pymongo
import os

MONGO_URL = os.environ.get('mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority')

database = pymongo.MongoClient(MONGO_URL)['notes']['notes']
