import mechanize
from bs4 import BeautifulSoup, SoupStrainer
import re

league = "574839"
season = "2015"


def standings_html():
    url = UrlConstants.STANDINGS_URL.format(league, season)
    return get_html(url)


def standings_detail_html():
    url = UrlConstants.STANDINGS_URL.format(league, season)
    return get_html(url)


def roster_html(team):
    url = UrlConstants.ROSTER_URL.format(league, team, season)
    return get_html(url)


def free_agent_html(team):
    url = UrlConstants.FA_URL.format(team)
    return self.get_html(url)


def transaction_html():
    url = UrlConstants.TRANSACTIONS_URL.format(self.league)
    return self.get_html(url)


def settings_html():
    url = UrlConstants.TRANSACTIONS_URL.format(self.league)
    return self.get_html(url)


def get_html(url):
    browser = mechanize.Browser()
    browser.open(url)
    return browser.response().read()


class UrlConstants:

    STANDINGS_URL = 'http://games.espn.go.com/ffl/standings?leagueId={0}&seasonId={1}'
    SCOREBOARD_URL = 'http://games.espn.go.com/ffl/scoreboard?leagueId={0}&seasonId={1}'
    ROSTER_URL = 'http://games.espn.go.com/ffl/clubhouse?leagueId={0}&teamId={1}&seasonId={2}'
    FA_URL = 'http://games.espn.go.com/ffl/freeagency?leagueId={0}&teamId={1}'
    SCORING_URL = 'http://games.espn.go.com/ffl/}eaders?leagueId={0}&teamId={1}&scoringPeriodId={2}'
    WAIVER_URL = 'http://games.espn.go.com/ffl/tools/waiverorder?leagueId={0}'
    TRANSACTIONS_URL = 'http://games.espn.go.com/ffl/tools/transactioncounter?leagueId={0}'
    SETTINGS_URL = 'http://games.espn.go.com/ffl/leaguesetup/settings?leagueId={0}'


ROSTER_URL = 'http://games.espn.go.com/ffl/clubhouse?leagueId={0}&teamId={1}&seasonId={2}'

only_tags_with_id_link2 = SoupStrainer(id=re.compile("playertable_"))

