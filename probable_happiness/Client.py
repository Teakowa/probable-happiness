import requests


class Client(object):

    @staticmethod
    def headers():

        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; MZ-m1 metal Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0'}

        return headers

    @staticmethod
    def get(url: str, params: dict = '', headers: dict = '', proxies: dict = ''):

        headers = headers if headers else Client.headers()

        try:
            response = requests.get(url, params, headers=headers, proxies=proxies)
    
            return response
        except Exception as e:
            return e

