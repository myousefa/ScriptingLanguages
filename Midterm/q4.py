import os
import sys
import subprocess

def recover(dir_loc):
    artist_name = None
    album_name = None
    track_number = None
    track_name = None
    
    for artist in os.listdir(dir_loc):
        # Artist names here are in their checksum form
        for album in os.listdir(dir_loc+artist):
            # Album names here are in their checksum form
            for track in os.listdir(dir_loc + artist+'/'+album):
                # Tracks here will be in their checksum name
                
                # Running exiftool in terminal and capturing stdout into variable
                sb = subprocess.run(
                    ['exiftool',dir_loc+artist+'/'+album+'/'+track],
                    stdout=subprocess.PIPE
                    )
                out = str(sb.stdout.decode("utf-8")).rstrip()

                # -- Parsing Metadata --
                # Parse Artist Name
                artist_name = out.split("Artist")[1].split(': ')[1].split('\n')[0]
                # Parse Album Name
                album_name = out.split("Album")[1].split(': ')[1].split('\n')[0]
                # Parse Song Name & Track num
                track_number = out.split("Track Number")[1].split(': ')[1].split('\n')[0]
                track_name = out.split("Title")[1].split(': ')[1].split('\n')[0]
                
                new_file_name = track_number + "_" + track_name + '.ogg'
                # Start by renaming all the tracks
                os.rename(dir_loc+artist+'/'+album+'/'+track , dir_loc+artist+'/'+album+'/'+new_file_name)
            # Now rename the album directory
            os.rename(dir_loc+artist+'/'+album , dir_loc+artist+'/'+album_name)
        # Now rename the artist directory
        os.rename(dir_loc+artist , dir_loc+artist_name)

def main():
    music_dir_location = 'data/music/'
    recover(music_dir_location)

main()