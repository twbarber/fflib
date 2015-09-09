import mechanize
import re
from bs4 import BeautifulSoup
from fflib.common.table import StandingsTable, RosterTable, BasicSettingsTable


class EspnDao(object):

    def __init__(self, config):
        self.config = dict(config.items('espn'))
        self.league = self.config.get('user.league')
        self.season = self.config.get('user.season')
        self.browser = self.connect()
        self.basic_settings()

    def connect(self):
        return mechanize.Browser()

    def standings(self):

        EAST_STANDINGS_ID = 2
        WEST_STANDINGS_ID = 3

        html = self.standings_html()
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.findAll("table")
        east = tables[EAST_STANDINGS_ID]
        west = tables[WEST_STANDINGS_ID]
        tab = StandingsTable(False)
        standings_map = {}
        standings_map["west"] = tab.standings(west)
        standings_map["east"] = tab.standings(east)
        return standings_map

    def standings_detail(self):

        EAST_DETAIL_ID = 4
        div_2_DETAIL_ID = 5

        html = self.standings_html()
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.findAll("table")
        div_1 = tables[EAST_STANDINGS_ID]
        div_2 = tables[WEST_STANDINGS_ID]
        tab = StandingsTable(False)
        standings_map = {}
        standings_map["west"] = tab.standings(west)
        standings_map["east"] = tab.standings(east)
        return standings_map

    def roster(self, team):
        html = self.roster_html(team)
        soup = BeautifulSoup(html, "html.parser")
        roster_html = soup.find("table", id=re.compile('playertable_'))
        roster_table = RosterTable(roster_html)
        return roster_table

    def rosters(self):
        x = 1
        rosters = {}
        while x <= 12:
            rosters[x] = self.roster(x)
            x += 1
        return rosters

    def basic_settings(self):
        html = self.settings_html()
        soup = BeautifulSoup(html, "html.parser")
        basic_html = soup.find("div", {"name": re.compile("basic")}).find("table")
        team_html = soup.find("div", {"name": re.compile("info")}).find("table")
        table = BasicSettingsTable(basic_html, team_html)

    def standings_html(self):
        url = UrlConstants.STANDINGS_URL.format(self.league, self.season)
        return self.get_html(url)

    def standings_detail_html(self):
        url = UrlConstants.STANDINGS_URL.format(self.league, self.season)
        return self.get_html(url)

    def roster_html(self, team):
        url = UrlConstants.ROSTER_URL.format(self.league, team, self.season)
        return self.get_html(url)

    def free_agent_html(self, team):
        url = UrlConstants.FA_URL.format(team)
        return self.get_html(url)

    def transaction_html(self):
        url = UrlConstants.TRANSACTIONS_URL.format(self.league)
        return self.get_html(url)

    def settings_html(self):
        url = UrlConstants.SETTINGS_URL.format(self.league)
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
