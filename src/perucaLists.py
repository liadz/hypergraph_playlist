import cPickle as pickle

PLAYLISTS_PATH = "/home/vitor/Dropbox/Mestrado/BrianData/playlists/"

DIALECT_LIST = ['Narrative', 'Single Artist', 'Theme', 'Dance-House', 'Jazz', 'Hip Hop', 'Rock-Pop', 'Hardcore',
                'Rhythm and Blues', 'Electronic Music', 'Break Up', 'Romantic', 'Reggae', 'Country', 'Road Trip',
                'Cover', 'Punk', 'Rock', 'Mixed', 'ALL', 'Indie', 'Alternating DJ', 'Sleep', 'Folk', 'Blues',
                'Depression']

#DIALECT_LIST = ['Punk']

OPTIONS = ['train', 'test']


def playlistToFile(dialect, option):
    with open(PLAYLISTS_PATH + dialect + "_" + option + ".pickle", 'r') as f:
        split = pickle.load(f)[0]
        for playlist in split:
            # print split[0]
            # playlist = split[0]
            playlistOutput = ''
            for song in playlist:
                playlistOutput += ' ' + song
                pass
            outputFile.write(playlistOutput.strip() + '\n')
            pass
        pass
    pass



if __name__ == '__main__':
    for dialect in DIALECT_LIST:
        with open(PLAYLISTS_PATH + dialect + ".txt", 'wb') as outputFile:
            for option in OPTIONS:
                playlistToFile(dialect, option)
                pass
            pass
        pass

    with open(PLAYLISTS_PATH + 'Punk.txt', 'r') as punk:
        print punk.readline()
        pass

    pass

