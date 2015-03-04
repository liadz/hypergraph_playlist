#!/usr/bin/env python
'''
CREATED:2011-11-03 10:23:22 by Brian McFee <bmcfee@cs.ucsd.edu>
 
Generate a tag-hopper playlist

Usage:

./sampleTaghopper.py model.pickle songhash.pickle N 

'''

import cPickle as pickle
import sys
import pprint
import hypergraph

def printPlaylist(P, songs):
    for (i, p) in enumerate(P):
        print '%2d. %s' % (i, songs[p])
        print "something aasfafaf"
        print "something aasfafaf"
        print "something aasfafaf"
        print "suba"
    pass


def samplePlaylist(G, N, songs):
    (playlist, tagindex) = G.sample(N)

    #G.unaryConstraintCreator()
    
    for (song_id, tag) in zip(playlist, tagindex):
        print '[%30s] %s' % (G.getEdgeLabel(tag), songs[song_id])
    pass

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        jsd = pickle.load(f)
        G = jsd['G']
    with open(sys.argv[2], 'r') as f:
        songs = pickle.load(f)
    N = int(sys.argv[3])

    G.setWeights({'__UNIFORM': 1e-12})

    samplePlaylist(G, N, songs)

    G.pachetWeightsSetter(N)

    pass
