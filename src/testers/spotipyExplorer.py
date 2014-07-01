'''
Created on 01/07/2014

@author: vitor
'''

import spotipy

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
if __name__ == '__main__' :
    sp = spotipy.Spotify()
    search = sp.search(q='artist:opeth', type='artist')
    items = search['artists']['items']
    print items[0]['name']
    print items[0]['uri']
    print items[0]['genres']