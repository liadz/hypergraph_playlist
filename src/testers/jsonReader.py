'''
Created on 22/04/2014

@author: vitor
'''

import cjson, gzip


with gzip.open("aotm2011_playlists.json.gz", "r") as f:
    P = cjson.decode(f.read())
    
print str(P[299])