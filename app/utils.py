from functools import reduce
from urllib.parse import urlparse, parse_qsl
import requests

your_api_key = ''   # get from google developer account 

def extract_playlist_id_from_url(url):
    query = urlparse(url)[4]
    return reduce((lambda s, z: s+z), map((lambda x: x[1] if x[0] == 'list' else ''), parse_qsl(query)), '')

def get_video_ids_from_playlist(pid, max_results=25):
    target_url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={}&playlistId={}&key={}".format(max_results, pid, your_api_key)
    data = requests.get(target_url).json()
    if "error" in data:
        return []
    else:
        return [extract_info(info['snippet']['resourceId']['videoId']) for info in data['items']]

