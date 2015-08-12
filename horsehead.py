import ConfigParser

from espnscraper import EspnScraper
from tablemapper import StandingsTableMapper

config = ConfigParser.RawConfigParser()
config.read('config.ini')

scraper = EspnScraper(config)
std_table = StandingsTableMapper(config)

html = scraper.get_standings_html()
tables = std_table.get_standings_tables(html)
standings_e = std_table.get_standings_map(tables.get("east"))
standings_w = std_table.get_standings_map(tables.get("west"))
standings_d_e = std_table.get_standings_detail_map(tables.get("east_detail"))
standings_d_w = std_table.get_standings_detail_map(tables.get("west_detail"))
print str(standings_e)
