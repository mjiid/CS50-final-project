import requests
from found import app

'''In this file we used an API called Audd api, which is an api that is used for identifying a song 
by only listening to some part of it.'''


def recognize(filename):
    data = {
        'api_token': '03813e4e0944e6564e9831c1f615e5d1',
        'return': 'apple_music,spotify',
    }
    files = {
        'file': open(str(app.config['UPLOAD_FOLDER'][:-5]) + 'results\\' +  str(filename[:-4]) + '.mp3', 'rb'),
    }
    result = requests.post('https://api.audd.io/', data=data, files=files)
    result_dict = result.json()
    if 'result' in result_dict.keys():
        if 'song_link' in result_dict['result'].keys():
            artist = result_dict['result']['artist']
            title = result_dict['result']['title']
            return [result_dict['result']['song_link'], artist, title]
        return False
    return False

