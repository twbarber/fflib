import re
from bs4 import BeautifulSoup


class Parser(object):

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

    def standings_values(self, html):
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.findAll("table", {"class": "tableBody"})
        values = parse
        return tables

    def standings_detail_values(self, html):
        return

    def roster_values(self, html):
        return

    def free_agent_values(self, html):
        soup = BeautifulSoup(html, "html.parser")
        free_agent_html = soup.find("table", id=re.compile('playertable_'))
        return
