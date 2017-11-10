from __future__ import unicode_literals

import youtube_dl

url = 'https://www.youtube.com/watch?v=jzGaS5kWj0U'

class YoutubeAudio:
    def __init__(self, url):
        options = {'format': 'm4a/best'}
        ydl = youtube_dl.YoutubeDL(options)
        info = ydl.extract_info(url, download=False)
        
        self.id = info['id']
        self.title = info['title']
        self.artist = info['uploader']
        self.src_url = info['webpage_url']
        self.audio_url = info['url']
        self.tags = info['tags']
        self.thumbnail = info['thumbnail']

    def serialize(self):
        return {'id': self.id,
                'title': self.title,
                'artist': self.artist,
                'src_url': self.src_url,
                'audio_url': self.audio_url,
                'tags': self.tags,
                'thumbnail': self.thumbnail,}

    def update(self, collection):
        res = collection.find_one_and_replace({'id': self.id}, self.serialize())
        if res is None:
            collection.insert_one(self.serialize())
