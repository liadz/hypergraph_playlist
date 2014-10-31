import pprint
import cPickle as pickle

__author__ = 'vitor'

TRAIN_FILE = "/home/vitor/git/hypergraph_playlist/playlists/Indie_train.pickle"
TEST_FILE = "/home/vitor/git/hypergraph_playlist/playlists/Indie_test.pickle"
SONGHASH = "songhash.pickle"

def getPlaylistOfSize(size, playlists):
    for playlist in playlists:
        if len(playlist) >= size:
            return playlist
        pass
    return []

if __name__ == '__main__':
    with open(TRAIN_FILE, 'r') as tf:
        folds = pickle.load(tf)
        pass

    with open(SONGHASH, 'r') as sh:
        sHash = pickle.load(sh)
        pass

    playlist = getPlaylistOfSize(10, folds[0])

    for song in playlist:
        pprint.pprint(sHash[song])
        pass

    pass

