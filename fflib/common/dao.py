import mechanize
import cookielib


class EspnDao(object):

    LOGIN_URL = 'http://m.espn.go.com/wireless/login'
    STANDINGS_URL = 'http://games.espn.go.com/ffl/standings?leagueId={0}&seasonId={1}'
    SCOREBOARD_URL = 'http://games.espn.go.com/ffl/scoreboard?leagueId={0}&seasonId={1}'
    ROSTER_URL = 'http://games.espn.go.com/ffl/clubhouse?leagueId={0}&teamId={1}&seasonId={2}'
    FA_URL = 'http://games.espn.go.com/ffl/freeagency?leagueId={0}&teamId={1}'
    SCORING_URL = 'http://games.espn.go.com/ffl/leaders?leagueId={0}&teamId={1}&scoringPeriodId={2}'
    WAIVER_URL = 'http://games.espn.go.com/ffl/tools/waiverorder?leagueId={0}'
    TRANSACTIONS_URL = 'http://games.espn.go.com/ffl/tools/transactioncounter?leagueId={0}'
    SETTINGS_URL = 'http://games.espn.go.com/ffl/leaguesetup/settings?leagueId={1}'

    def __init__(self, config):
        self.config = dict(config.items('espn'))
        self.league = self.config.get('user.league')
        self.season = self.config.get('user.season')
        self.user = self.config.get('user.name')
        self.password = self.config.get('user.password')
        self.browser = self.connect()

    def connect(self):
        cj = cookielib.CookieJar()
        br = mechanize.Browser()
        br.set_cookiejar(cj)
        br.open(self.LOGIN_URL)
        br.form = list(br.forms())[0]
        br.form['username'] = self.user
        br.form['gspw'] = self.password
        br.submit()
        return br

    def standings(self):
        self.browser.open(self.STANDINGS_URL.format(self.league, self.season))
        return self.browser.response().read()

    def roster(self, team):
        self.browser.open(self.ROSTER_URL.format(self.league, team, self.season))
        return self.browser.response().read()

    def freeagent(self, team):
        self.browser.open(self.FA_URL.format(self.league, team))
        return self.browser.response().read()

    def transactions(self):
        self.browser.open(self.TRANSACTIONS_URL.format(self.league))
        return self.browser.response().read()

    def settings(self):
        self.browser.open(self.TRANSACTIONS_URL.format(self.league))
        return self.browser.response().read()


class CbsDao(object):
    def __init__(self, config):
        self.config = dict(config.items('cbs'))
        self.league = self.config.get('user.league')
        self.season = self.config.get('user.season')
        self.user = self.config.get('user.name')
        self.password = self.config.get('user.password')
        self.browser = self.connect()


class NflDao(object):
    def __init__(self, config):
        self.config = dict(config.items('nfl'))
        self.league = self.config.get('user.league')
        self.season = self.config.get('user.season')
        self.user = self.config.get('user.name')
        self.password = self.config.get('user.password')
        self.browser = self.connect()
