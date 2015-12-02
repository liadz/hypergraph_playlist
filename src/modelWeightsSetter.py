'''
Created on 19/09/2014

@author: vitor
'''

import cPickle as pickle
import hypergraph
import pprint

DIALECT_LIST = ['Narrative', 'Single Artist', 'Theme', 'Dance-House', 'Jazz', 'Hip Hop', 'Rock-Pop', 'Hardcore',
                'Rhythm and Blues', 'Electronic Music', 'Break Up', 'Romantic', 'Reggae', 'Country', 'Road Trip',
                'Cover', 'Punk', 'Rock', 'Mixed', 'ALL', 'Indie', 'Alternating DJ', 'Sleep', 'Folk', 'Blues',
                'Depression']

if __name__ == "__main__":
    graphList = {}

    with open('full_saida.pickle', 'r') as f:
        output = pickle.load(f)
        pass

    with open('full_model.pickle', 'r') as mm:
        graph = pickle.load(mm)['G']
        pass

    for dialect in DIALECT_LIST:
        trainedWeights = output['weights'][dialect][0]

        graph.setWeights(trainedWeights)

        graphList[dialect] = graph

        #pprint.pprint('toba!')
        #pprint.pprint(graph.getWeights())
        #pprint.pprint('toba!')
        pass

    with open('my_trained_list.pickle', 'wb') as t:
        pickle.dump(graphList, t)
        pass

    print 'every little thing is gonna be alright'

    pass