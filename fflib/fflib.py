import ConfigParser

from common.dao import EspnDao
from common.mapper import StandingsTable


def config():
    parser = ConfigParser.RawConfigParser()
    parser.read('../config.ini')
    return parser


class League(object):
    def __init__(self, platform):
        if platform in ['ESPN']:
            self.platform = 'ESPN'
            self.config = config()
            self.dao = EspnDao(self.config)

    def standings(self):
        html = self.dao.standings()
        table = Table()

    def detail_standings(self):
        html = self.dao.standings()
        table = Table(True)

    def settings(self):
        return
