'''
Created on 19/09/2014

@author: vitor
'''

import cPickle as pickle
import hypergraph
import pprint

if __name__ == "__main__":
    with open('saida.pickle', 'r') as f:
        output = pickle.load(f)
        pass

    #fil = open('picPrint.txt', 'w')
    #pprint.pprint(output, fil, 1)

    trainedWeights = output['weights']['Depression'][0]
    pprint.pprint(trainedWeights)

    with open('my_model.pickle', 'r') as mm:
        graph = pickle.load(mm)['G']
        pass

    graph.setWeights(trainedWeights)

    pprint.pprint('toba!')
    pprint.pprint(graph.getWeights())
    pprint.pprint('toba!')

    with open('my_trained_model.pickle', 'wb') as t:
        pickle.dump({'G': graph}, t)
        pass

    pass