from app import app, models, db

import flask

@app.route('/')
def index():
    return "Hello"

@app.route('/music/add/<uid>')
def add_youtube_audio(uid):
    music = models.YoutubeAudio(uid)
    collection = db['pyusic']['youtube']
    music.update(collection)
    return flask.jsonify(music.serialize())
