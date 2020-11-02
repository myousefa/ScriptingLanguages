# Generate input.txt file
import os

config = {
    'music_loc' : '../Assignment1/Music/',
}

def create_input_file(loc):
    with open("input.txt","w+") as out_f:
        for genre in os.listdir(loc):
            for artist in os.listdir(loc+genre):
                for album in os.listdir(loc+genre+'/'+artist):
                    for item in os.listdir(loc+genre+'/'+ artist+'/'+album):
                        if(os.path.isdir(loc+genre+'/'+ artist+'/'+album+'/'+item)):
                            for song in os.listdir(loc+genre+'/'+ artist+'/'+album+'/'+item):
                                out_f.write('Music' + '/' + genre + '/' + artist + '/' + album + '/' + item + '/' + song + '\n')
                        elif(os.path.isfile(loc+genre+'/'+ artist+'/'+album+'/'+item)):
                            out_f.write('Music' + '/' + genre + '/' + artist + '/' + album + '/' + item + '\n')

def main():
    create_input_file(config['music_loc'])

if __name__ == '__main__':
    main()