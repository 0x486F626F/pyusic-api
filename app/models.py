from __future__ import unicode_literals

import youtube_dl

class YoutubeAudio:
    def __init__(self, param):
        info = param
        if type(param) is str:
            info = self.get_youtube_info(param)
        self.init_by_dict(info)

    def get_youtube_info(self, uid):
        options = {'format': 'm4a/best', 'ignoreerrors': True}
        ydl = youtube_dl.YoutubeDL(options)
        return ydl.extract_info(uid, download=False)

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

    def update_audio_url(self):
        try:
            info = self.get_youtube_info(self.id)
            if 'url' not in info:
                return False
            self.audio_url = info['url']
            return True
        except:
            return False

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
