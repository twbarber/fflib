import mechanize
from bs4 import BeautifulSoup
from fflib.espn.scraper import Scraper


class EspnDao(object):
    def __init__(self, config):
        self.config = dict(config.items('espn'))
        connection = Scraper(self.config)


class CbsDao(object):
    def __init__(self, config):
        self.config = dict(config.items('cbs'))


class NflDao(object):
    def __init__(self, config):
        self.config = dict(config.items('nfl'))
