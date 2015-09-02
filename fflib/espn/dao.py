import mechanize
from bs4 import BeautifulSoup
from fflib.common.table import StandingsTable


class EspnDao(object):

    def __init__(self, config):
        self.config = dict(config.items('espn'))
        self.league = self.config.get('user.league')
        self.season = self.config.get('user.season')
        self.browser = self.connect()

    def connect(self):
        return mechanize.Browser()

    def standings(self):

        EAST_STANDINGS_ID = 2
        WEST_STANDINGS_ID = 3

        html = self.standings_html()
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.findAll("table")
        divisions = {
            "east": tables[EAST_STANDINGS_ID],
            "west": tables[WEST_STANDINGS_ID]
        }
        test = StandingsTable(False)
        test.standings(divisions["west"])
        print test
        return divisions

    def standings_detail(self):
        EAST_DETAIL_ID = 4
        WEST_DETAIL_ID = 5

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
        url = UrlConstants.STANDINGS_URL.format(self.league, self.season)
        return self.get_html(url)

    def standings_detail_html(self):
        url = self.STANDINGS_URL.format(self.league, self.season)
        return self.get_html(url)

    def roster_html(self, team):
        url = self.ROSTER_URL.format(team, self.season)
        return self.get_html(url)

    def free_agent_html(self, team):
        url = self.FA_URL.format(team)
        return self.get_html(url)

    def transaction_html(self):
        url = self.TRANSACTIONS_URL.format(self.league)
        return self.get_html(url)

    def settings_html(self):
        url = self.TRANSACTIONS_URL.format(self.league)
        return self.get_html(url)

    def get_html(self, url):
        self.browser.open(url)
        return self.browser.response().read()


class UrlConstants:
    STANDINGS_URL = 'http://games.espn.go.com/ffl/standings?leagueId={0}&seasonId={1}'
    SCOREBOARD_URL = 'http://games.espn.go.com/ffl/scoreboard?leagueId={0}&seasonId={1}'
    ROSTER_URL = 'http://games.espn.go.com/ffl/clubhouse?leagueId={0}&teamId={1}&seasonId={2}'
    FA_URL = 'http://games.espn.go.com/ffl/freeagency?leagueId={0}&teamId={1}'
    SCORING_URL = 'http://games.espn.go.com/ffl/}eaders?leagueId={0}&teamId={1}&scoringPeriodId={2}'
    WAIVER_URL = 'http://games.espn.go.com/ffl/tools/waiverorder?leagueId={0}'
    TRANSACTIONS_URL = 'http://games.espn.go.com/ffl/tools/transactioncounter?leagueId={0}'
    SETTINGS_URL = 'http://games.espn.go.com/ffl/leaguesetup/settings?leagueId={0}'
