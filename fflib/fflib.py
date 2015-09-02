import ConfigParser
from espn.dao import EspnDao


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
        tables = self.dao.standings()
        return tables

    def detail_standings(self):
        html = self.dao.standings()
        table = Table(True)

    def settings(self):
        return
