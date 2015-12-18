#!/usr/bin/env python
'''
CREATED:2011-11-03 10:23:22 by Brian McFee <bmcfee@cs.ucsd.edu>
 
Generate a tag-hopper playlist

Usage:

./sampleTaghopper.py model.pickle songhash.pickle N

for multi sampling:
./samplePlaylist my_trained_list.pickle songhash.pickle N

'''

import cPickle as pickle
import sys
import pprint
import hypergraph

PLAYLIST_PER_DIALECT = 3

def printPlaylist(P, songs):
    for (i, p) in enumerate(P):
        print '%2d. %s' % (i, songs[p])
        print "something aasfafaf"
        print "something aasfafaf"
        print "something aasfafaf"
        print "suba"
    pass


def samplePlaylist(G, N, songs):
    # (playlist, tagindex) = G.pachet_sample(N)
    (playlist, tagindex) = G.sample(N)

    # G.unaryConstraintCreator()

    for (song_id, tag) in zip(playlist, tagindex):
        print '[%30s] %s' % (G.getEdgeLabel(tag), songs[song_id])
    pass


# I used this to decide which dialect I would use in my research by taking a general look at many playlists
def sampleManyPlaylists(hypergraphList, N, songs, playlistQuantity):
    with open('dialectEvaluationList.txt', 'wb') as deList:
        count = 1
        for key, hg in hypergraphList.iteritems():
            hg.setWeights({'__UNIFORM': 1e-12})
            deList.write("Dialect: " + key + "\n")
            print "Vai, Safadaum!" + str(count)
            count+=1
            for i in range(playlistQuantity):
                print str(i)
                (playlist, tagindex) = hg.sample(N)

                deList.write("Playlist " + str(i+1) + "\n")

                for (song_id, tag) in zip(playlist, tagindex):
                    #deList.write(u"[%30s] %s".format(hg.getEdgeLabel(tag), songs[song_id]))
                    songItem = '[' + hg.getEdgeLabel(tag) + '] ' + songs[song_id].decode("ascii", "ignore")
                    deList.write(songItem)
                    pass
                deList.write("\n")
                pass
            deList.write("\n")
            pass
        deList.write("\n")
        pass
    pass


"""if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        jsd = pickle.load(f)
        G = jsd['G']
    with open(sys.argv[2], 'r') as f:
        songs = pickle.load(f)
    N = int(sys.argv[3])

    G.setWeights({'__UNIFORM': 1e-12})

    # G.pachetWeightsSetter(N)
    # G.unaryConstraintCreator('rock', 7)
    # G.unaryConstraintCreator('electronic', 8)
    # G.unaryConstraintCreator('alternative', 9)

    samplePlaylist(G, N, songs)

    pass"""

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        hypergraphsList = pickle.load(f)
    with open(sys.argv[2], 'r') as f:
        songs = pickle.load(f)
    nSongsPlaylist = int(sys.argv[3]) - 1

    #print hypergraphsList

    sampleManyPlaylists(hypergraphsList, nSongsPlaylist, songs, PLAYLIST_PER_DIALECT)

    print 'Canxa!'
    pass

