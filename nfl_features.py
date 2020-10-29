import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


'''
get_playId

Input: 
    plays --> dataframe consisting of all the plays
    gameId --> game id of a specific game
Return:
    returns an array of all the play ids in that game

'''
def get_playId(plays,gameId):
    return plays[plays['gameId']==gameId]['playId'].values

'''
get_plays

Input: 
    plays --> dataframe consisting of all the plays
    gameId --> game id of a specific game
Return:
    returns a dataframe consisting of all the information
    about the plays in that game

'''
def get_plays(plays,gameId):
    return plays[plays['gameId']==gameId]

'''
get_track_game

Input: 
    track --> dataframe consisting of all the tracking data/ can use the weeks too
    gameId --> game id of a specific game
Return:
    returns a dataframe consisting of all the tracking data collected in that game

'''
def get_track_game(track,gameId):
    return track[track['gameId']==gameId]

'''
get_track_play

Input: 
    track --> dataframe consisting of all the tracking data/ can use the weeks too
    playId --> play id of the specific play
Return:
    returns a dataframe of the tracking data collected from the play

'''
def get_track_play(track,playId):
    return track[track['playId']==playId]

'''
get_coord

Input:
    track --> dataframe consisting of all the tracking data/ can use the weeks too
    playId --> play id of the specific play
Return:
    returns a dataframe of the tracking data collected from the play

'''
def get_coord(track):
    c_x = {}
    c_y = {}
    for f in set(track['frameId']):
        c_x[f] = [x for x,x_f in zip(track['x'],track['frameId']) if x_f==f]
        c_x[f] = [y for y,y_f in zip(track['y'],track['frameId']) if y_f==f]

    return c_x,c_y

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

    return animation_gif