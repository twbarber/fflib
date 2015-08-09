import mechanize
import cookielib


class EspnScraper(object):
    def __init__(self, config):
        self.config = config
        self.browser = self.connect()

    def connect(self):
        cj = cookielib.CookieJar()
        br = mechanize.Browser()
        br.set_cookiejar(cj)
        br.open(self.config.ESPN_LOGIN_URL)
        credentials = self.load_credentials()
        br.form = list(br.forms())[0]
        for username, password in credentials:
            br.form['username'] = username
            br.form['gspw'] = password
        br.submit()
        return br

    def load_credentials(self):
        with open(self.config.CRED_FILE_NAME) as f:
            credentials = [x.strip().split(':') for x in f.readlines()]
            return credentials

    def get_standings_html(self):
        self.browser.open(self.config.ESPN_STANDINGS_URL)
        return self.browser.response().read()

    def get_roster_html(self, team):
        self.browser.open(self.config.ESPN_ROSTER_URL)
        return

    def get_fa_tables(self):
        self.browser.open(self.config.ESPN_STANDINGS_URL)
        return

    def get_pkup_tables(self):
        self.browser.open(self.config.ESPN_STANDINGS_URL)
        return
