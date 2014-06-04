'''
Created on 03/06/2014

@author: vitor
'''

import cPickle as pickle

#TRAIN_FILE = "D:/git/hypergraph_playlist/playlists/ALL_train.pickle"
#TEST_FILE = "D:/git/hypergraph_playlist/playlists/ALL_test.pickle"

TRAIN_FILE = "/home/vitor/git/hypergraph_playlist/playlists/ALL_train.pickle"
TEST_FILE = "/home/vitor/git/hypergraph_playlist/playlists/ALL_test.pickle"
OUTPUT_PATH = "/home/vitor/git/hypergraph_playlist/src/saida.pickle"

split_train = pickle.load(open(TRAIN_FILE))
split_test = pickle.load(open(TEST_FILE))
evalOutput = pickle.load(open(OUTPUT_PATH, 'rb'))

print evalOutput