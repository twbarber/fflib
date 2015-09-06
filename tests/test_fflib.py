#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_fflib
----------------------------------

Tests for `fflib` module.
"""
from fflib import fflib

"""
league = fflib.League('ESPN')
standings_map = league.standings()
print(standings_map["east"].rows)
print(standings_map["west"].rows)
"""
league = fflib.League('ESPN')
standings_map = league.rosters()
print(standings_map["east"].rows)
print(standings_map["west"].rows)

"""
table = PrettyTable(standings_w.columns)
table.align[standings_w.columns[0]] = 'l'
for i, row in enumerate(standings_w.rows, start=1):
    table.add_row(standings_w.rows[i].values())
print(table)

class TestFflib(unittest.TestCase):
    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass
"""
