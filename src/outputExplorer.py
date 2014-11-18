
import cPickle as pickle
import hypergraph
import pprint

__author__ = 'vitor'

if __name__ == "__main__":
    with open('saida.pickle', 'r') as f:
        output = pickle.load(f)
        pass

    moi = open('saidatxt.txt', 'w')

    pprint.pprint(output, moi, 1)

    pass