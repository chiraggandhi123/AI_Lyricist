'''
Retrieve all lyrics from available songs for a given artist and train a
Markov model to be able to generate new lyrics
'''

import sys
import pandas
import string
import re
import csv
from textblob import TextBlob
import markovify
import json

artist = str(sys.argv[1]) #double quotes

df = pandas.read_csv("./songlyrics/songdata.csv",
                    encoding = 'unicode_escape')
# len(df['artist'].unique()) #643
# print(df.columns) #['artist', 'song', 'link', 'text']
# print(df['artist'].unique())

f_name = './artists/'+artist+'.txt'
try:
    # artist data exists
    artist_df = df[df['artist'] == artist]
    if artist_df.empty == True:
        raise 'ArtistNotFound'
    lyrics = artist_df['text']
    num_songs = len(lyrics)
    print("Artist found, "+repr(num_songs)+" songs")
    all_lyr = lyrics.str.cat(sep="\n")
    all_lyr.strip(string.punctuation)
    fn = open(f_name,'w')
    fn.write(all_lyr)
    fn.close()
    print("Lyrics compiled")
except:
    print('Artist not found')
    exit()


## Create AI model
# Get raw text as string.
with open(f_name) as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)
model_json = text_model.to_json()
# print(model_json)
m_file = './models/'+artist+'.json'
with open(m_file, 'w') as outfile:
    json.dump(model_json, outfile)

print("Model created")
