import ConfigParser
from espn.dao import EspnDao


class League(object):

    def __init__(self, platform):
        if platform in ['ESPN']:
            self.platform = 'ESPN'
            self.config = self.config()
            self.dao = EspnDao(self.config)

    def standings(self, division):
        tables = self.dao.standings(division)
        return tables

    def detail_standings(self):
        tables = self.dao.standings_detail()
        return tables

    def rosters(self):
        tables = self.dao.rosters()
        return tables

    def roster(self, team):
        tables = self.dao.roster(team)
        return tables

    def free_agents(self):
        tables = self.dao.free_agents()
        return tables

    def config(self):
        parser = ConfigParser.RawConfigParser()
        parser.read('../config.ini')
        return parser
