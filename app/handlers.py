from app import app, models, db

import flask

@app.route('/')
def index():
    return "Hello"

@app.route('/music/delete/<uid>')
def del_youtube_audio(uid):
    collection = db['pyusic']['youtube']
    result = collection.delete_one({'id': uid})
    return flask.jsonify({'deleted': result.deleted_count})

@app.route('/music/info/<uid>')
def add_youtube_audio(uid):
    collection = db['pyusic']['youtube']

    music = collection.find_one({'id': uid})
    if music is None:
        music = models.YoutubeAudio(uid)
        title = flask.request.args.get('title')
        artist = flask.request.args.get('artist')
        if title is not None:
            music.title = title
        if artist is not None:
            music.artist = artist
        music.update(collection)
    else:
        music = models.YoutubeAudio(music)

    return flask.jsonify(music.serialize)

@app.route('/music/info/<uid>/<key>')
def get_info(uid, key):
    collection = db['pyusic']['youtube']

    music = collection.find_one({'id': uid})
    if music is None:
        return '{}'

    if key in music:
        return flask.jsonify({key: music[key]})

    return '{}'

@app.route('/music/info/modify/<uid>/<key>/<value>')
def modify_info(uid, key, value):
    collection = db['pyusic']['youtube']

    music = collection.find_one({'id': uid})
    if music is None:
        return '{}'

    if key in music and type(music[key]) is str:
        music[key] = value

    music = models.YoutubeAudio(music)
    music.update(collection)

    return flask.jsonify(music.serialize)

@app.route('/music/info/add_tag/<uid>/<tag>')
def add_tag(uid, tag):
    collection = db['pyusic']['youtube']

    music = collection.find_one({'id': uid})
    if music is None:
        return '{}'

    music = models.YoutubeAudio(music)
    if tag not in music.tags:
        music.tags.append(tag)
        music.update(collection)

    return flask.jsonify({'tags': music.tags})

@app.route('/music/info/del_tag/<uid>/<tag>')
def del_tag(uid, tag):
    collection = db['pyusic']['youtube']

    music = collection.find_one({'id': uid})
    if music is None:
        return '{}'

    music = models.YoutubeAudio(music)
    if tag in music.tags:
        music.tags.remove(tag)
        music.update(collection)

    return flask.jsonify({'tags': music.tags})

@app.route('/music/search')
def search():
    collection = db['pyusic']['youtube']

    search_filter = {}

    tags = flask.request.args.get('tags')
    if tags is not None:
        search_filter['tags'] = {'$in': tags.split(',')}

    music_info_list = collection.find(search_filter)
    musics = [models.YoutubeAudio(info) for info in music_info_list]
    musics_json = [music.serialize for music in musics]
    return flask.jsonify(musics_json)
