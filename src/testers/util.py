
# shows a user's playlists (need to be authenticated via oauth)

import os
import subprocess
import spotipy.oauth2 as oauth2

def prompt_for_user_token(username, scope=None):
    ''' prompts the user to login if necessary and returns
the user token suitable for use with the spotipy.Spotify
constructor
'''

    client_id = '9016785404b14280bebc54f6faaf46eb'
    client_secret = 'ba0459ab866b45ef9b1c7ce24357ec9e'
    redirect_uri = 'http://localhost:8888/callback'

    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri,
        scope=scope, cache_path=username)

    # try to get a valid token for this user, from the cache,
    # if not in the cache, the create a new (this will send
    # the user to a web page where they can authorize this app)

    token_info = sp_oauth.get_cached_token()

    if not token_info:
        auth_url = sp_oauth.get_authorize_url()
        try:
            subprocess.call(["open", auth_url])
            print "Opening %s in your browser" % auth_url
        except:
            print "Please navigate here: %s" % auth_url
        response = raw_input("Enter the URL you were redirected to: ")
        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)
    # Auth'ed API request
    if token_info:
        return token_info['access_token']
    else:
        return None