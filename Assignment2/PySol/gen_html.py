import sys
import os
import json
config = {
    'use_input_file' : True,
    'input_file_loc' : 'input.txt',
    'music_loc' : '../Assignment1/Music/',
    'debug_mode' : True
}
# filling the data structure
def read_music(loc):
    """
    Reads input file that contains locations
    to music files and places into a dictionary
    object of the following shape:
    Dict<Str,Dict<Str,Array>>
    {
        Artist : {
            Projects : [
                Track1,
                ...
                TrackN
            ]
        }
    }
    """
    music = {}
    album_data = {}
    with open(loc,'r+') as input_f:
        for line in input_f:
            line_data = line.rstrip().split('/')
            artist,album,track = line_data[2],line_data[3],line_data[-1]
            if(artist not in music):
                # Add the artist if they aren't in the dict already
                music[artist] = {}
                album_data = {}
                album_data[album] = []
                # Add a delimiter to reference the locationn of the track
                album_data[album].append(track+'|'+line.rstrip())
                music[artist] = album_data
            elif(artist in music and album in music[artist]):
                # if they are in the dict and the album is already in, add the song in
                music[artist][album].append(track+'|'+line.rstrip())
            elif(artist in music and album not in music[artist]):
                # if they are in the dict but we find a new album, add the current track as well
                music[artist][album] = []
                music[artist][album].append(track+'|'+line.rstrip())
    return music

# Creating the data structure           
def get_music_dir(loc):
    music = {}
    for genre in os.listdir(loc):
        for artist in os.listdir(loc+genre):
            music[artist] = []
            for album in os.listdir(loc+genre+'/'+artist):

                album_work = {}
                album_work[album] = []
                for item in os.listdir(loc+genre+'/'+ artist+'/'+album):
                    if(os.path.isdir(loc+genre+'/'+ artist+'/'+album+'/'+item)):
                        for song in os.listdir(loc+genre+'/'+ artist+'/'+album+'/'+item):
                            album_work[album].append(song)
                    elif(os.path.isfile(loc+genre+'/'+ artist+'/'+album+'/'+item)):
                        album_work[album].append(item)
                music[artist].append(album_work)
    return music

def create_visualization(music_db):
    """
    DEBUG function to visualize the music DB dictionary object
    """
    json_music_db = json.dumps(music_db,sort_keys=False, indent=4)
    music_db_json_file = open("music_db.json","w+")
    
    sys.stdout = music_db_json_file
    print(json_music_db)
    sys.stdout = sys.__stdout__
    music_db_json_file.close()
    print("[SUCCESS]: Wrote music to JSON file.")

def create_artist_row(output_file,artist,projects):
    # subroutine 
    def create_album_row(output_file,project,project_details):
        output_file.write(f'<td>{project}</td>\n')
        output_file.write('<td>\n<table border="0">\n')
        for track in sorted(project_details):
            track_title = track.split('.')[0]
            path_2_track = track.split('|')[-1]
            output_file.write(f'<tr><td><a href="{path_2_track}">{track_title}</a></td></tr>\n')
        output_file.write('</table>\n</td>\n')

    for idx,(project,project_details) in enumerate(sorted(projects.items())):
        if(idx == 0):
           output_file.write(f'<tr><td rowspan="{len(projects)}">{artist}</td>\n')
           create_album_row(output_file,project,project_details)
           output_file.write('</tr>')
        else:
            output_file.write('<tr>\n')
            create_album_row(output_file,project,project_details)
            output_file.write('</tr>\n')
    #output_file.write('</tr>\n')
    pass

def create_page(music_db):
    # Creates output file, if it exists --> overwrites
    with open('output.html','w+') as out_f:
        out_f.write("<html>\n<body>\n")
        # Create top row headers
        out_f.write('<table border="1"><tr><th>Artist</th><th>Album</th><th>Tracks</th></tr>\n\t')
        # Create Rows for each artist
        for artist,projects in sorted(music_db.items()):
            create_artist_row(out_f,artist,projects)
        # Close table
        out_f.write('</table>\n\t')
        out_f.write("</body>\n</html>")

def main():
    music_db = None
    if(config['use_input_file']):
        music_db = read_music(config['input_file_loc'])
    else:
        music_db = get_music(config['music_loc'])
    
    if(config['debug_mode']):
        create_visualization(music_db)
    
    create_page(music_db)
    pass
    
if __name__ == '__main__':
    main()