fflib
=========

fflib gives access to various fantasy football league data across multiple latforms. The library is intended to provide 
easy access to standings, rosters, free agent, and weekly matchups for use by league managers.

Currently, the only platform supported is ESPN. Others will be added in the future.

fflib is available as both a web service, and python library, with additional language support planned.

espn
=========

In order to use fflib with your ESPN fantasy football data, your league will have to be open to the public. To do this,
your commisioner will need nable this option in the League's settings. Simply visit:

    http://games.espn.go.com/ffl/leaguesetup/settings?leagueId=<YOUR_LEAGUE_ID>
    
Make sure to replace the <YOUR_LEAGUE_ID> token with your actual league id that can be found in the address bar when
you're at your league's home page. Under Basic settings, select 'Yes' from the 'Make League Viewable to Public' 
dropdown. Afterwards, you'll be able to access league data using this library.

## Current Planned Features

- Pull League Standings, and Detail Standings
- Pull Rosters from Individual Teams
- Pull Free Agency List per League
- Pull Transaction Counter per League
- Pull Matchup Information per Matchup
- Pull Leage Scoring Settings

## Config Example

    [espn]
    
    user.league = 574839
    user.season = 2015

## Display Text Based Tables

    +--------+---+---+---+------+----+
    | TEAM   | W | L | T | PCT  | GB |
    +--------+---+---+---+------+----+
    | Team 1 | 0 | 0 | 0 | .000 | -- |
    | Team 2 | 0 | 0 | 0 | .000 | -- |
    | Team 3 | 0 | 0 | 0 | .000 | -- |
    | Team 4 | 0 | 0 | 0 | .000 | -- |
    | Team 5 | 0 | 0 | 0 | .000 | -- |
    | Team 6 | 0 | 0 | 0 | .000 | -- |
    +--------+---+---+---+------+----+

## Standings

## Teams

## Scoreboard

## Transactions

## Free Agency

## League Settings
