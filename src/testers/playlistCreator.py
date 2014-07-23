'''
Created on 02/07/2014

@author: vitor
'''

import pprint
import sys
import os
import subprocess

import spotipy

import util
import spotipy.oauth2 as oauth2

username = "liadzv"
playlist_name = "teste 1"

token = util.prompt_for_user_token(username)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(username, playlist_name)
    pprint.pprint(playlists)
else:
    print "Can't get token for", username