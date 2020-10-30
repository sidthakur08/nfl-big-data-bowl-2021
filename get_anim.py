import pandas as pd
import nfl_features as nfl

WEEK_ID = 1
GAME_ID = 2018090600
PLAY_ID = 75

print("Getting the plays data...")
plays = pd.read_csv('data/plays.csv')
print("Getting the tracking data...")
track = pd.read_csv(f'data/week{WEEK_ID}.csv')

print("Getting all the plays from the game...")
event_game = nfl.get_plays(plays,GAME_ID)
print("Getting tracking data of the game...")
track_game = nfl.get_track_game(track,GAME_ID)

print("Getting tracking data for the play...")
track_play = nfl.get_track_play(track_game,PLAY_ID)
print("Getting the tracking data for home team, away team and football...")
home_track = nfl.get_track_team(track_play,'home')
away_track = nfl.get_track_team(track_play,'away')
football_track = nfl.get_track_team(track_play,'football')

print("Getting coordinates of the players for animation...")
home_coord_dict = {}
away_coord_dict = {}
football_coord_dict = {}

home_coord_dict['h_x'],home_coord_dict['h_y'] = nfl.get_coord(home_track)
away_coord_dict['h_x'],away_coord_dict['h_y'] = nfl.get_coord(away_track)
football_coord_dict['h_x'],football_coord_dict['h_y'] = nfl.get_coord(football_track)

home_coord = pd.DataFrame(home_coord_dict)
away_coord = pd.DataFrame(away_coord_dict)
football_coord = pd.DataFrame(football_coord_dict)

print("Generating animation...")
play_gif = nfl.animate_play(PLAY_ID,home_coord,away_coord,football_coord,event_game)

print("Saving animation")
play_gif.save(f"animate_play/play_{GAME_ID}_{PLAY_ID}.mp4",writer='ffmpeg')