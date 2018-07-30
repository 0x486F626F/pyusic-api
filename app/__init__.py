from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
app.config['JSON_AS_ASCII'] = False

db = MongoClient('mongodb://mongo:27017')

import config
import threading

url_updater = threading.Thread(target=config.update_all_audio_url, args=(db,))
url_updater.start()

from app import handlers, models
