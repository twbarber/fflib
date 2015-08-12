from bs4 import BeautifulSoup


class StandingsTableMapper(object):

    EAST_STANDINGS_ID = 2
    WEST_STANDINGS_ID = 3
    EAST_DETAIL_ID = 4
    WEST_DETAIL_ID = 5

    def __init__(self, config):
        self.config = config

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

    def standings_table(self, table, mask):
        data = self.parse_rows(table)
        standings = Table(data[0], data[1])
        for i, team in enumerate(data[2:8], start=1):
            team_entry = StandingsEntry(*team)
            if mask:
                team_entry.name = 'Team ' + str(i)
            standings.add_row(i, team_entry.values())
        return standings

    def standings_detail_table(self, table, mask):
        data = self.parse_rows(table)
        standings_detail = Table(data[0], data[1])
        for i, team in enumerate(data[2:10], start=1):
            team_entry = StandingsDetailEntry(*team)
            if mask:
                team_entry.owner = ''
                team_entry.team = 'Team ' + str(i)
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


class Table(object):
    def __init__(self, title, columns):
        self.title = title
        self.columns = columns
        self.rows = {}

    def add_row(self, row, values):
        self.rows[row] = values


class StandingsEntry(object):
    def __init__(self, name, win, loss, tie, pct, gb):
        self.name = name
        self.win = win
        self.loss = loss
        self.tie = tie
        self.pct = pct
        self.gb = gb

    def __repr__(self):
        string = (
            'Team:\t' + self.name + '\n' +
            'Wins:\t' + self.win + '\n' +
            'Loses:\t' + self.loss + '\n' +
            'Ties:\t' + self.tie + '\n' +
            'Pct:\t' + self.pct + '\n' +
            'GB:\t' + self.gb
        )
        return string

    def values(self):
        values = [
            self.name,
            self.win,
            self.loss,
            self.tie,
            self.pct,
            self.gb
        ]
        return values


class StandingsDetailEntry(object):
    def __init__(self, club, pf, pa, home, away, div, streak):
        club_info = self.parse_club(club)
        if len(club_info) == 1:
            self.team = club_info[0]
            self.owner = ''
        else:
            self.team = club_info[0]
            self.owner = club_info[1]
        self.pf = pf
        self.pa = pa
        self.home = home
        self.away = away
        self.div = div
        self.streak = streak

    def __repr__(self):
        string = (
            'Team:\t' + self.team + '\n' +
            'Owner:\t' + self.owner + '\n' +
            'PF:\t' + self.pf + '\n' +
            'PA:\t' + self.pa + '\n' +
            'Home:\t' + self.home + '\n' +
            'Away:\t' + self.away + '\n' +
            'Div:\t' + self.div + '\n' +
            'Streak:\t' + self.streak + '\n'
        )
        return string

    def parse_club(self, club):
        club_info = club.split('(')
        if len(club_info) == 1:
            return club_info
        club_info[0] = club_info[0][:-1]
        club_info[1] = club_info[1][:-1]
        return club_info
