import ConfigParser

from prettytable import PrettyTable

from espn.scraper import EspnScraper
from espn.mapper import StandingsTable

config = ConfigParser.RawConfigParser()
config.read('config.ini')

scraper = EspnScraper(config)
std_table = StandingsTable(config, hide=True)

hidden = True
html = scraper.standings_html()
tables = std_table.all_tables(html)
standings_e = std_table.standings_table(tables.get("east"), hidden)
standings_w = std_table.standings_table(tables.get("west"), hidden)
standings_d_e = std_table.standings_detail_table(tables.get("east_detail"), hidden)
standings_d_w = std_table.standings_detail_table(tables.get("west_detail"), hidden)

table = PrettyTable(standings_w.columns)
table.align[standings_w.columns[0]] = 'l'
for i, row in enumerate(standings_w.rows, start=1):
    table.add_row(standings_w.rows[i])
print table
