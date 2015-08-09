from espnscraper import EspnScraper
from config import Config
from tablemapper import StandingsTableMapper

config = Config()
scraper = EspnScraper(config)
std_table = StandingsTableMapper(config)

html = scraper.get_standings_html()
tables = std_table.get_standings_tables(html)
standings_e = std_table.get_standings_map(tables.get("east"))
standings_w = std_table.get_standings_map(tables.get("west"))
standings_d_e = std_table.get_standings_detail_map(tables.get("east_detail"))
standings_d_w = std_table.get_standings_detail_map(tables.get("west_detail"))

print 'East' + '\n'
for i, entry in enumerate(standings_d_e, start=1):
    print standings_d_e.get(i)
print '\n'
print 'West' + '\n'
for i, entry in enumerate(standings_d_w, start=1):
    print standings_d_w.get(i)
