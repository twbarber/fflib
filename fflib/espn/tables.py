class Table(object):
    def __init__(self, title, columns):
        self.title = title
        self.columns = columns
        self.rows = {}

    def add_row(self, row, values):
        self.rows[row] = values


class StandingsTable(Table):
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


class DetailStandingsTable(Table):
    class DetailStandingsEntry(object):
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
