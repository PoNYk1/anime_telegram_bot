from itertools import count
import re
import requests
from bs4 import BeautifulSoup as bs


class Animego_parser ():
    def __init__(self, url):
        self.req = requests.get(url)
        self.ok = self.req.ok

        if self.ok:
            self.soup = bs(self.req.text, 'lxml')

    def get_all_info(self):
        info = {}

        banner = self.soup.find(
            'div', {"class": "anime-poster position-relative cursor-pointer"})\
            .find('img')

        info['banner_url'] = banner.get('src')
        info['title'] = banner.get('title')

        anime_info = self.soup.find('div', {'class': 'anime-info'}).find('dl')

        for el in anime_info.find_all('dt'):
            if el.text == 'Эпизоды':
                info['cur_episode'] = int(re.findall(
                    r'\d{0,}', el.find_next_sibling().text)[0])

        print(info)
        return info
