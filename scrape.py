from nba_api.stats.endpoints import leaguehustlestatsplayer
import pandas as pd


years = ['2015','2016','2017','2018','2019','2020','2021','2022']
hustle_stats_2015 = leaguehustlestatsplayer.LeagueHustleStatsPlayer(per_mode_time='PerGame',
    season='2016',season_type_all_star='Regular Season')

print(h for h in hustle_stats_2015)
df = hustle_stats_2015.get_data_frames()[0]
print(df)
