import mechanize
from bs4 import BeautifulSoup


class EspnDao(object):

    ESPN_PREFIX = 'http://games.espn.go.com/ffl/'
    STANDINGS_URL = '{0}standings?leagueId={1}&seasonId={2}'
    SCOREBOARD_URL = '{0}scoreboard?leagueId={1}&seasonId={2}'
    ROSTER_URL = '{0}clubhouse?leagueId={1}&teamId={2}&seasonId={3}'
    FA_URL = '{0}freeagency?leagueId={1}&teamId={2}'
    SCORING_URL = '{0}eaders?leagueId={1}&teamId={2}&scoringPeriodId={3}'
    WAIVER_URL = '{0}tools/waiverorder?leagueId={1}'
    TRANSACTIONS_URL = '{0}tools/transactioncounter?leagueId={1}'
    SETTINGS_URL = '{0}leaguesetup/settings?leagueId={1}'

    EAST_STANDINGS_ID = 2
    WEST_STANDINGS_ID = 3
    EAST_DETAIL_ID = 4
    WEST_DETAIL_ID = 5

    def __init__(self, config):
        self.config = dict(config.items('espn'))
        self.league = self.config.get('user.league')
        self.season = self.config.get('user.season')
        self.browser = self.connect()

    def connect(self):
        return mechanize.Browser()

    def standings(self):
        tables = self.standings_html()
        print tables
        divisions = {
            "east": tables[self.EAST_STANDINGS_ID],
            "west": tables[self.WEST_STANDINGS_ID]
        }
        return divisions

    def standings_detail(self):
        tables = self.standings_tables_html()
        print tables
        """
        division_html = {
            "east": tables[self.EAST_DETAIL_ID],
            "west": tables[self.WEST_DETAIL_ID]
        }
        divisions = {}
        divisions["east"] = self.parse_rows(division_html["east"])
        divisions["west"] = self.parse_rows(division_html["west"])
        return divisions
        """

    def standings_html(self):
        url = self.STANDINGS_URL.format(self.ESPN_PREFIX, self.league, self.season)
        return self.get_html(url)

    def standings_detail_html(self):
        url = self.STANDINGS_URL.format(self.ESPN_PREFIX, self.league, self.season)
        return self.get_html(url)

    def roster_html(self, team):
        url = self.ROSTER_URL.format(self.ESPN_PREFIX, team, self.season)
        return self.get_html(url)

    def free_agent_html(self, team):
        url = self.FA_URL.format(self.ESPN_PREFIX, team)
        return self.get_html(url)

    def transaction_html(self):
        url = self.TRANSACTIONS_URL.format(self.ESPN_PREFIX, self.league)
        return self.get_html(url)

    def settings_html(self):
        url = self.TRANSACTIONS_URL.format(self.ESPN_PREFIX, self.league)
        return self.get_html(url)

    def get_html(self, url):
        self.browser.open(url)
        return self.browser.response().read()


class Parser(object):

    @staticmethod
    def parse_rows(table):
        rows = table.findAll('tr')
        data = []
        for row in rows:
            cols = row.findAll('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        return data
