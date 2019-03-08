'''
Incomplete but would ideally play the mp3 files that were generated
'''
import sys
from pygame import mixer

song_name = sys.argv[1]
# TODO: play mp3
s_name = './mp3_files/'+song_name+'.mp3'
mixer.init()
mixer.music.load(s_name)
mixer.music.play()

# TODO: incorporate background music library
