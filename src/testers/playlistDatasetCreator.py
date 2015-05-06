__author__ = 'vitor'
#this module is going to get songs from the bigger playlist dataset to create a smaller more controlled one.
#if possible Ill use made up songs which Id have more control.

import pprint
import cPickle as pickle

TRAIN_FILE = "/home/vitor/git/hypergraph_playlist/playlists/ALL_train.pickle"
SONG_LIST = "/home/vitor/git/hypergraph_playlist/src/songhash.pickle"

with open(TRAIN_FILE, 'r') as play:
    pl = pickle.load(play)
    #for line in playlists:
        #pprint.pprint(line)
    pprint.pprint(pl[0][1])
    pass

with open(SONG_LIST, 'r') as songs:
    s = pickle.load(songs)
    pass

for song in pl[0][1]:
    pprint.pprint(s[song])
pass