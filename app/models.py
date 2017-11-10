from __future__ import unicode_literals

import youtube_dl

class YoutubeAudio:
    def __init__(self, param):
        info = param
        if type(param) is str:
            options = {'format': 'm4a/best'}
            ydl = youtube_dl.YoutubeDL(options)
            info = ydl.extract_info(param, download=False)
        self.init_by_dict(info)

    def init_by_dict(self, info):
        self.id = info['id']
        self.title = info['title']
        if 'uploader' in info:
            self.artist = info['uploader']
        if 'artist' in info:
            self.artist = info['artist']
        if 'webpage_url' in info:
            self.src_url = info['webpage_url']
        if 'src_url' in info:
            self.src_url = info['src_url']
        if 'url' in info:
            self.audio_url = info['url']
        if 'audio_url' in info:
            self.audio_url = info['audio_url']
        self.tags = info['tags']
        self.thumbnail = info['thumbnail']

    @property
    def serialize(self):
        return {'id': self.id,
                'title': self.title,
                'artist': self.artist,
                'src_url': self.src_url,
                'audio_url': self.audio_url,
                'tags': self.tags,
                'thumbnail': self.thumbnail,}

    def update(self, collection):
        info = self.serialize
        res = collection.find_one_and_replace({'id': self.id}, info)
        if res is None:
            collection.insert_one(info)
