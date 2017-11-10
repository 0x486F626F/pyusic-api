from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')
app.config['JSON_AS_ASCII'] = False

db = MongoClient('mongodb://hongbozhang.me:6668')

from app import handlers, models
