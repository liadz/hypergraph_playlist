import cPickle as pickle

if __name__ == "__main__":
    graphList = {}

    with open('full_saida.pickle', 'r') as f:
        output = pickle.load(f)
        pass

    for score in output['params'].iteritems():
        print score
        pass

    """with open('my_trained_list.pickle', 'wb') as t:
        pickle.dump(graphList, t)
        pass"""

    print 'every little thing is gonna be alright'

    pass