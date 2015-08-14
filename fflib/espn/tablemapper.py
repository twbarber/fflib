from bs4 import BeautifulSoup


class StandingsTableMapper(object):
    EAST_STANDINGS_ID = 2
    WEST_STANDINGS_ID = 3
    EAST_DETAIL_ID = 4
    WEST_DETAIL_ID = 5

    def __init__(self, config, hide):
        self.config = config
        self.hide = hide

    def all_tables(self, html):
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.findAll("table")
        tabs = {
            "east": tables[self.EAST_STANDINGS_ID],
            "west": tables[self.WEST_STANDINGS_ID],
            "east_detail": tables[self.EAST_DETAIL_ID],
            "west_detail": tables[self.WEST_DETAIL_ID]
        }
        return tabs

    def standings_table(self, table):
        data = self.parse_rows(table)
        standings = Tables.StandingsTable(data[0], data[1])
        for i, team in enumerate(data[2:8], start=1):
            team_entry = StandingsEntry(*team)
            standings.add_row(i, team_entry.values())
        return standings

    def standings_detail_table(self, table):
        data = self.parse_rows(table)
        standings_detail = Table(data[0], data[1])
        for i, team in enumerate(data[2:10], start=1):
            team_entry = StandingsDetailEntry(*team)
            standings_detail.add_row(i, team_entry)
        return standings_detail

    @staticmethod
    def parse_rows(table):
        rows = table.findAll('tr')
        data = []
        for row in rows:
            cols = row.findAll('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])
        return data
