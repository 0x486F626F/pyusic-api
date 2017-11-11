from app import models
import time

def update_all_audio_url(db):
    collection = db['pyusic']['youtube']
    music_info_list = collection.find()
    musics = [models.YoutubeAudio(info) for info in music_info_list]
    for music in musics:
        if music.update_audio_url():
            music.update(collection)
            time.sleep(5)
    print('All audio url updated')
    time.sleep(3600)
