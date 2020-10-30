import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


'''
get_playId

Input: 
    plays --> dataframe consisting of all the plays
    gameId (int) --> game id of a specific game
Return:
    returns an array of all the play ids in that game

'''

def get_playId(plays,gameId):
    try:
        return plays[plays['gameId']==gameId]['playId'].values
    except Exception as e:
        print(e)

'''
get_plays

Input: 
    plays --> dataframe consisting of all the plays
    gameId (int)--> game id of a specific game
Return:
    returns a dataframe consisting of all the information
    about the plays in that game

'''

def get_plays(plays,gameId):
    try:
        return plays[plays['gameId']==gameId]
    except Exception as e:
        print(e)

'''
get_track_game

Input: 
    track --> dataframe consisting of all the tracking data/ can use the weeks too
    gameId (int)--> game id of a specific game
Return:
    returns a dataframe consisting of all the tracking data collected in that game

'''

def get_track_game(track,gameId):
    try:
        return track[track['gameId']==gameId]
    except Exception as e:
        print(e)

'''
get_track_play

Input: 
    track --> dataframe consisting of all the tracking data/ can use the weeks too
    playId (int)--> play id of the specific play
Return:
    returns a dataframe of the tracking data collected from the play

'''
def get_track_play(track,playId):
    try:
        return track[track['playId']==playId]
    except Exception as e:
        print(e)

'''
get_track_team

Input:
    track --> dataframe consisting of tracking data
    team --> home/away/football being the three choices

Return:
    returns dataframe with tracking data of home & away players and football
'''

def get_track_team(track,team):
    try:
        return track[track['team']==team]
    except Exception as e:
        print(e)

'''
get_coord

Input:
    track --> dataframe consisting of tracking data for the home, away and football objects

Return:
    c_x --> list of x coordinates
    c_y --> list of y coordinates
    
    returns list of coordinates for the home, away and football
    (to get coordinates for the animation)
'''

def get_coord(track):
    try:
        c_x = {}
        c_y = {}
        for f in set(track['frameId']):
            c_x[f] = [x for x,x_f in zip(track['x'],track['frameId']) if x_f==f]
            c_x[f] = [y for y,y_f in zip(track['y'],track['frameId']) if y_f==f]

        return c_x,c_y
    except Exception as e:
        print(e)


'''
animate_play

Input:
    playId --> integer indicating play for which you need the animation
    home_coord --> coordinates of home team players for a frame
    away_coord --> coordinates of away team players for a frame
    football_coord --> coordinates of football team players for a frame
    plays --> plays dataframe for the match to get the play description

Return:
    saves the animated gif to the animation folder
'''

def animate_play(playId,home_coord,away_coord,football_coord,plays):
    anim_fig,anim_ax = plt.subplots(figsize=(15,10))
    img = plt.imread('football_field_grayscale.png')
    anim_ax.imshow(img,extent=[0,120,0,53,34])

    h, = anim_ax.plot(home_coord.iloc[0]['h_x'],home_coord[0]['h_y'],'ro')
    a, = anim_ax.plot(away_coord.iloc[0]['h_x'],away_coord[0]['h_y'],'ro')
    f, = anim_ax.plot(football_coord.iloc[0]['h_x'],football_coord[0]['h_y'],'ro')

    def animate(i):
        h.set_data(home_coord.iloc[i]['h_x'],home_coord.iloc[i]['h_y'])
        a.set_data(away_coord.iloc[i]['h_x'],away_coord.iloc[i]['h_y'])
        f.set_data(football_coord.iloc[i]['h_x'],football_coord.iloc[i]['h_y'])

        return h,a,f,

    anim_ax.set_title(plays[plays['playId']==playId].iloc[0]['playDescription'])
    animation_gif = animation.FuncAnimation(anim_fig,animate,frames=home_coord.index,interval=85)

    animation_gif.save(f"animate_play/play_{plays['gameid'].iloc[0]}_{plays['playId'].iloc[0]}.mp4",writer='ffmpeg')