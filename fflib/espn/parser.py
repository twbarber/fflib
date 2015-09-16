import re
from bs4 import BeautifulSoup


class Parser(object):
    def parse_html(self, html):
        data = self.parse_rows(html)
        return data

    def parse_rows(self, table):
        rows = table.findAll('tr')
        data = []
        for row in rows:
            cols = row.findAll('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        return data

    def scrub_empty(self, team):
        team.extend(('--', '--', '--'))
        return team

    def scrub_bye(self, team):
        team.insert(4, '** BYE **')
        return team
