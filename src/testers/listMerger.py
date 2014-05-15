'''
Created on 14/05/2014

@author: Vitor
'''

import cPickle as pickle

TRAIN_FILE = "D:/git/hypergraph_playlist/playlists/ALL_train.pickle"
TEST_FILE = "D:/git/hypergraph_playlist/playlists/ALL_test.pickle"

split_train = pickle.load(open(TRAIN_FILE))
split_test = pickle.load(open(TEST_FILE))

# Combine the first train and test split to recover the full collection of playlists
all_playlists = split_train[0] + split_test[0]

# Merge all playlists into a set to get the list of all songs
all_songs = set()
for pl in all_playlists:
    all_songs.update(pl)

print len(all_playlists)
print len(all_songs)

pickle.dump(all_songs, open("all_my_songs.pickle", "wb"))

