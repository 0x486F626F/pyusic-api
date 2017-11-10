from app import app, models, db

import flask

@app.route('/')
def index():
    return "Hello"

@app.route('/music/add/<uid>')
def add_youtube_audio(uid):
    collection = db['pyusic']['youtube']

    music = collection.find_one({'id': uid})
    if music is not None:
        music.pop('_id')
        return flask.jsonify(music)

    music = models.YoutubeAudio(uid)
    music.update(collection)
    return flask.jsonify(music.serialize())
