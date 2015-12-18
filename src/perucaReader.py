import cPickle as pickle
import sys

'''
Usage:
./perucaReader.py songhash.pickle
'''

LIST_PATH = "D:\Dropbox\Mestrado\Peruca Lists\\"

DIALECTS = ["Rhythm and Blues", "Road Trip", "Rock", "Rock-Pop"]

def idsToSongNames(songHash):
    for dialect in DIALECTS:
        with open(LIST_PATH + dialect + ".txt", 'r') as playlists:
            with open(LIST_PATH + dialect + " Songs.txt", 'w') as outputFile:
                for i in range(0, 5):
                    playlist = playlists.readline().split()
                    for song in playlist:
                        outputFile.write(songHash[song].decode("ascii", "ignore"))
                        pass
                    outputFile.write("\n\n")
                    pass
                pass
            pass
        pass
    pass



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        songHash = pickle.load(f)
        pass

    idsToSongNames(songHash)

    pass
