from itertools import count
import re
import requests
from bs4 import BeautifulSoup as bs


class Animego_parser ():
    def __init__(self):
        pass

    def get_all_info(self, url):
        req = requests.get(url)
        soup = ''

        if req.ok:
            soup = bs(req.text, 'lxml')

        info = {}

        banner = soup.find(
            'div', {"class": "anime-poster position-relative cursor-pointer"})\
            .find('img')

        info['banner_url'] = banner.get('src')
        info['title'] = banner.get('title')

        anime_info = soup.find('div', {'class': 'anime-info'}).find('dl')

        for el in anime_info.find_all('dt'):
            if el.text == 'Эпизоды':
                info['cur_episode'] = int(re.findall(
                    r'\d{0,}', el.find_next_sibling().text)[0])

        # print(info)
        return info

    def get_cur_epesode(self, url):
        req = requests.get(url)
        soup = ''

        if req.ok:
            soup = bs(req.text, 'lxml')

        anime_info = soup.find('div', {'class': 'anime-info'}).find('dl')

        for el in anime_info.find_all('dt'):
            if el.text == 'Эпизоды':
                cur_episode = int(re.findall(
                    r'\d{0,}', el.find_next_sibling().text)[0])
                return cur_episode
