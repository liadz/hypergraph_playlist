'''
Created on 19/09/2014

@author: vitor
'''

import cPickle as pickle
import hypergraph
import pprint

if __name__ == "__main__" :
    with open('saida.pickle', 'r') as f:
        output = pickle.load(f)
        f = open('picPrint.txt', 'w')
        pprint.pprint(output, f, 1)
        pass