import requests,json
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib 
import matplotlib.font_manager
import datetime
import os
import time
import discord
import io
import constants
from matplotlib.patches import Rectangle
matplotlib.use('agg')

def plot_rating(data,handle,date_ub,date_lb):
    data_list_x=[]
    data_list_y=[]
    for row in data:
        temp = datetime.datetime.fromtimestamp(row["ratingUpdateTimeSeconds"])
        if(temp<date_lb or temp>=date_ub):
            continue
        data_list_x.append(temp)
        data_list_y.append(row["newRating"])
    if(len(data_list_x)==0):
        return None
    latest_rating = data[-1]["newRating"]
    handle_mod = handle.replace('_','-')
    extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0) 
    plt.plot(data_list_x,data_list_y,marker="o",markersize=3,markeredgewidth=0.5,markerfacecolor='black',color='white')
    ymin,ymax = plt.gca().get_ylim()
    bgcolor = plt.gca().get_facecolor()
    plt.axhspan(0,1200,facecolor="#b3b3b3",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.axhspan(1200,1400,facecolor="#33ff33",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.axhspan(1400,1600,facecolor="#5cd6d6",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.axhspan(1600,1900,facecolor="#1a53ff",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.axhspan(1900,2100,facecolor="#ff33cc",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.axhspan(2100,2300,facecolor="#ffb84d",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.axhspan(2300,2400,facecolor="#ff6600",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.axhspan(2400,2600,facecolor="#ff6666",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.axhspan(2600,3000,facecolor="#ff0000",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.axhspan(3000,4000,facecolor="#660000",alpha=0.8,edgecolor=bgcolor,linewidth=0.5)
    plt.ylim(ymin,ymax)
    plt.gcf().autofmt_xdate()
    plt.legend([extra],[f'{handle_mod} ({latest_rating})'],loc='upper left')
    filename = os.path.join(constants.TEMP_DIR,f'tempplot_{time.time()}.png')
    plt.savefig(filename,facecolor=plt.gca().get_facecolor(), bbox_inches='tight', pad_inches=0.25)
    plt.close()
    with open(filename, 'rb') as file:
        discord_file = discord.File(io.BytesIO(file.read()), filename='plot.png')
    os.remove(filename)
    return discord_file
