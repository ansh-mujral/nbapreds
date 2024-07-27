import pandas as pd
import numpy as np
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import leaguedashplayerbiostats
from nba_api.stats.endpoints import playerdashboardbygeneralsplits

# career = playercareerstats.PlayerCareerStats(player_id='203999') 
# career_data = career.get_data_frames()
# print(career_data)

gamelog = playergamelog.PlayerGameLog(player_id='203999', season='2015-16')
gamelog_data = gamelog.get_data_frames()
print(gamelog_data)

# players = leaguedashplayerbiostats.LeagueDashPlayerBioStats()
# players_data = players.get_data_frames()[0]
# print(players_data[players_data['PLAYER_NAME'] == 'Nikola Jokic'])
