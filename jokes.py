import requests


class Jokes:
    def __init__(self):
        self.url = "https://api.chucknorris.io/jokes/"

    def get_random_joke(self):
        random_url = self.url + "random"
        data = requests.get(url=random_url).json()
        return data['value']
