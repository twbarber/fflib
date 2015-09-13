import re


class Table(object):

    def __init__(self, title, columns):
        self.title = title
        self.columns = columns
        self.rows = []

    def add_row(self, values):
        self.rows.append(values)

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


class StandingsTable(Table):

    def __init__(self, html):
        parsed_html = self.parse_html(html)
        self.division = parsed_html[0]
        columns = parsed_html[1]
        data = parsed_html[2:(len(parsed_html))]
        Table.__init__(self, 'Standings', columns)
        self.standings(data)

    def __repr__(self):
        return str(self.rows)

    def standings(self, data):
        for team in data:
            entry = StandingsEntry(*team)
            self.add_row(entry)


class StandingsDetailTable(Table):
    def __init__(self, html):
        parsed_html = self.parse_html(html)
        self.division = parsed_html[0]
        columns = parsed_html[1]
        data = parsed_html[2:(len(parsed_html))]
        Table.__init__(self, 'Standings Detail', columns)
        self.detail(data)

    def __repr__(self):
        return str(self.rows)

    def detail(self, data):
        for team in data:
            entry = DetailStandingsEntry(*team)
            self.add_row(entry)


class RosterTable(Table):

    def __init__(self, html):
        parsed_html = self.parse_html(html)
        columns = parsed_html[1]
        data = parsed_html[2:(len(parsed_html))]
        Table.__init__(self, 'Roster', columns)
        self.populate(data)

    def __repr__(self):
        return str(self.rows)

    def populate(self, data):
        starters = data[0:9]
        bench = data[11:len(data) - 1]
        full = starters + bench
        for i, team in enumerate(full, start=1):
            if len(team) == 12:
                team = self.scrub_bye(team)
            elif len(team) == 10:
                team = self.scrub_empty(team)
            entry = RosterEntry(*team)
            self.add_row(entry)

    def scrub_empty(self, team):
        team.extend(('--', '--', '--'))
        return team

    def scrub_bye(self, team):
        team.insert(4, '** BYE **')
        return team


class FreeAgentTable(Table):

    def __init__(self, html):
        parsed_html = self.parse_html(html)
        columns = parsed_html[1]
        data = parsed_html[2:(len(parsed_html))]
        Table.__init__(self, 'Free Agents', columns)
        self.populate(data)

    def __repr__(self):
        return str(self.rows)

    def populate(self, data):
        for i, team in enumerate(data, start=1):
            if len(team) == 12:
                team = self.scrub_bye(team)
            elif len(team) == 10:
                team = self.scrub_empty(team)
            entry = FreeAgentEntry(*team)
            self.add_row(entry)

    def scrub_empty(self, team):
        team.extend(('--', '--', '--'))
        return team

    def scrub_bye(self, team):
        team.insert(4, '** BYE **')
        return team


class BasicSettingsTable(Table):
    def __init__(self, basic_html, team_html):
        Table.__init__(self, 'BasicSettings', ['Key', 'Value'])
        self.basic_settings(basic_html)
        self.division_settings(team_html)

    def basic_settings(self, html):
        parsed_html = self.parse_html(html)
        self.league = parsed_html[1][1]
        self.teams = parsed_html[2][1]

    def division_settings(self, html):
        divisions = self.parse_divisions(html)
        self.num_divisions = len(divisions.keys())

    def parse_divisions(self, table):
        divs = table.findAll("tr", {"class": re.compile("row*")})
        data = {}
        for div in divs:
            div_name = div.find("td", {"class": re.compile("settingLabel")}).text.strip()
            table = div.find("table").findAll("td")
            team_list = []
            for team in table:
                team_list.append(team.text.strip())
            data[div_name] = team_list
        return data


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


class RosterEntry(object):

    def __init__(self, slot, player_team_pos, opp, status, prk, pts, avg, last, proj, oprk, start, own, add):
        self.slot = slot.encode('utf-8').strip()
        self.player_team_pos = player_team_pos.encode('utf-8').strip()
        self.opp = opp.encode('utf-8').strip()
        self.status = status.encode('utf-8').strip()
        self.prk = prk.encode('utf-8').strip()
        self.pts = pts.encode('utf-8').strip()
        self.avg = avg.encode('utf-8').strip()
        self.last = last.encode('utf-8').strip()
        self.proj = proj.encode('utf-8').strip()
        self.oprk = oprk.encode('utf-8').strip()
        self.start = start.encode('utf-8').strip()
        self.own = own.encode('utf-8').strip()
        self.add = add.encode('utf-8').strip()

    def __repr__(self):
        string = (
            'Slot:\t' + self.slot + '\n' +
            'Player:\t' + self.player_team_pos + '\n' +
            'Opponent:\t' + self.opp + '\n' +
            'Status:\t' + self.status + '\n' +
            'Prk:\t' + self.prk + '\n' +
            'Pts:\t' + self.pts + '\n' +
            'Avg:\t' + self.avg + '\n' +
            'Last:\t' + self.last + '\n' +
            'Proj:\t' + self.proj + '\n' +
            'Oprk:\t' + self.oprk + '\n' +
            'Start:\t' + self.start + '\n' +
            'Own:\t' + self.own + '\n' +
            'Add/Drop:\t' + self.add
        )
        return string

    def values(self):
        values = [
            self.slot,
            self.player_team_pos,
            self.opp,
            self.status,
            self.prk,
            self.pts,
            self.avg,
            self.last,
            self.proj,
            self.oprk,
            self.start,
            self.own,
            self.add
        ]
        return values


class FreeAgentEntry(object):
    def __init__(self, player_team_pos, team, opp, status, prk, pts, avg, last, proj, oprk, start, own, add):
        self.player_team_pos = player_team_pos.encode('utf-8').strip()
        self.team = team.encode('utf-8').strip()
        self.opp = opp.encode('utf-8').strip()
        self.status = status.encode('utf-8').strip()
        self.prk = prk.encode('utf-8').strip()
        self.pts = pts.encode('utf-8').strip()
        self.avg = avg.encode('utf-8').strip()
        self.last = last.encode('utf-8').strip()
        self.proj = proj.encode('utf-8').strip()
        self.oprk = oprk.encode('utf-8').strip()
        self.start = start.encode('utf-8').strip()
        self.own = own.encode('utf-8').strip()
        self.add = add.encode('utf-8').strip()

    def __repr__(self):
        string = (
            'Player:\t' + self.player_team_pos + '\n' +
            'Team:\t' + self.team + '\n' +
            'Opponent:\t' + self.opp + '\n' +
            'Status:\t' + self.status + '\n' +
            'Prk:\t' + self.prk + '\n' +
            'Pts:\t' + self.pts + '\n' +
            'Avg:\t' + self.avg + '\n' +
            'Last:\t' + self.last + '\n' +
            'Proj:\t' + self.proj + '\n' +
            'Oprk:\t' + self.oprk + '\n' +
            'Start:\t' + self.start + '\n' +
            'Own:\t' + self.own + '\n' +
            'Add/Drop:\t' + self.add
        )
        return string

    def values(self):
        values = [
            self.player_team_pos,
            self.team,
            self.opp,
            self.status,
            self.prk,
            self.pts,
            self.avg,
            self.last,
            self.proj,
            self.oprk,
            self.start,
            self.own,
            self.add
        ]
        return values


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
