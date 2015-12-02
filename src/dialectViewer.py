import cPickle as pickle

if __name__ == "__main__":
    with open('my_trained_list.pickle', 'r') as f:
        output = pickle.load(f)
        pass

    print output['Narrative']
    pass
