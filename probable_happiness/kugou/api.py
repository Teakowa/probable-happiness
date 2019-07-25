from probable_happiness.Client import Client


class Artist(object):

    @staticmethod
    def get_class():
        url = "http://m.kugou.com/singer/class&json=true"
        response = Client.get(url)

        return response.json()

    @staticmethod
    def list(id: int, page: int = 1):
        url = 'http://m.kugou.com/singer/list/' + str(id)
        params = {'page': page, 'json': 'true'}

        response = Client.get(url, params=params)

        return dict(response.json())

    @staticmethod
    def info(id: int, page: int = 1):
        url = 'http://m.kugou.com/singer/info/' + str(id)
        params = {'page': page, 'json': 'true'}

        response = Client.get(url, params=params)

        return dict(response.json())

    @staticmethod
    def song(id: int, page: int = 1):
        response = Artist.info(id, page)['songs']

        return dict(response.json())


class Song(object):

    @staticmethod
    def new(type: int = 1):
        url = "http://mobilecdnbj.kugou.com/api/v3/rank/newsong"
        params = {'type': type, 'pagesize': 100, 'version': 9259, 'with_cover': 1, 'area_code': 1}

        response = Client.get(url, params)

        return dict(response.json())

    @staticmethod
    def info(hash: str):
        url = 'http://m.kugou.com/app/i/getSongInfo.php'
        params = {'cmd': 'playInfo', 'hash': hash}

        response = Client.get(url, params=params)

        return dict(response.json())

    @staticmethod
    def index(hash: str):
        data = Album.special_recommend(hash)

        index = {
            'hash': hash,
            'index': data['data']['info']['kugou_index']
        }

        return index


class Album(object):

    @staticmethod
    def info(album_id: int):
        url = "http://m.kugou.com/app/i/getablum.php"

        params = {'type': '1', 'ablumid': album_id}
        response = Client.get(url, params=params)

        return dict(response.json())

    @staticmethod
    def special_recommend(hash: str):
        url = "http://servicebj.mobile.kugou.com/v1/yueku/special_album_recommend"

        params = {'hash': hash, 'api_ver': '2'}
        response = Client.get(url, params=params)

        return dict(response.json())
