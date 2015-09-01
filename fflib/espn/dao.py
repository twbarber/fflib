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

    def __init__(self, config):
        self.config = dict(config.items('espn'))
        self.league = self.config.get('user.league')
        self.season = self.config.get('user.season')
        self.browser = self.connect()

    def connect(self):
        cj = cookielib.CookieJar()
        browser = mechanize.Browser()
        browser.set_cookiejar(cj)
        return browser

    def standings(self):
        tables = self.standings_tables()
        divisions = {
            "east": tables[self.EAST_STANDINGS_ID],
            "west": tables[self.WEST_STANDINGS_ID]
        }
        return divisions

    def standings_detail(self):
        tables = self.standings_tables()
        division_html = {
            "east": tables[self.EAST_DETAIL_ID],
            "west": tables[self.WEST_DETAIL_ID]
        }
        divisions = {}
        divisions["east"] = self.parse_rows(division_html["east"])
        divisions["west"] = self.parse_rows(division_html["west"])
        return divisions

    def standings_tables(self):
        html = html()
        tables = soup.findAll("table")

    def roster(self, team):
        self.browser.open(self.ROSTER_URL.format(self.ESPN_PREFIX, team, self.season))
        return self.browser.response().read()

    def free_agent(self, team):
        self.browser.open(self.FA_URL.format(self.ESPN_PREFIX, team))
        return self.browser.response().read()

    def transactions(self):
        self.browser.open(self.TRANSACTIONS_URL.format(self.ESPN_PREFIX, self.league))
        html = self.browser.response().read()

    def settings(self):
        self.browser.open(self.TRANSACTIONS_URL.format(self.ESPN_PREFIX, self.league))
        html = self.browser.response().read()

    def html(self, url, *args):
        self.browser.open(url, )
        html = self.browser.response().read()
        return html


class Parser(object):
    def standings(self):
        return

    def detail_standings(self):
        return

    @staticmethod
    def parse_rows(table):
        rows = table.findAll('tr')
        data = []
        for row in rows:
            cols = row.findAll('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        return data
