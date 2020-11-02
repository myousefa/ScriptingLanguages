#!/usr/bin/perl -l
use warnings;
use strict;
use Data::Dumper;

# Path to the file goes here
my $filename = 'input.txt';

sub read_file {
    open(FH, '<', $filename) or die $!;
    my %music_db = ();
    my @album_tracks = ();
    while(<FH>){
        my @line_data = split('/',$_);
        my $artist = $line_data[2];
        my $album = $line_data[3];
        my $track = $line_data[-1];
        my %artist_projects = ();
        
        if(!exists $music_db{$artist}){
            # checking the artist is NOT in the Hash
            push(@album_tracks,$track);
            $music_db{$artist}{$album} = [@album_tracks];
        }
        elsif(exists $music_db{$artist} && exists $music_db{$artist}{$album}){
            # checking the artist IS in the Hash
            # add the current track to the existing album
            push(@album_tracks,$track);
            $music_db{$artist}{$album} = [ @album_tracks ];
        }
        elsif($music_db{$artist} && !exists $music_db{$artist}{$album}){
            # checking the artist IS in the Hash
            # add the current track to the new album
            @album_tracks = ();
            push(@album_tracks,$track);
            $music_db{$artist}{$album} =  [@album_tracks];
        }
    }
    close(FH);
    return %music_db
}

sub get_row_span {

    # [Depracated]: This is a subroutine 
    # that gets the size of the inner Hash
    # i.e. Number of projects which is the same
    # as the row span for the Artist in the table

    my %music_db = %{$_[0]};
    my $artist = $_[1];
    my $num_projects = 0;
    while ((my $album, my $album_details) = each %{$music_db{$artist}} ){
        $num_projects+=1;
    }
    return $num_projects;
}

sub create_album_row {

    # This subroutine creates the inner 3rd column
    # which lists out the tracks for the project
    # It also sorts they keys

    my $album_details = $_[0];
    my $album = $_[1];
    print('<td>',$album,'</td>');
    print('<td><table border="0">');
    foreach my $track (sort @$album_details ){
        print('<tr><td><a href="{path_2_track}">',$track,'</a></td></tr>');
    }
    print('</table></td>');
}

# From the file, read the contents and get the datastructure
my %music_db = read_file();

# Uncomment this to visualize the datastructure in STDOUT
#print Dumper(\%music_db);

# Print the top of the HTML
print('<html><body>');
print('<table border="1"><tr><th>Artist</th><th>Album</th><th>Tracks</th></tr>');
foreach my $artist (sort keys %music_db){
    # Get the row span
    my $num_projects = 0;
    while ((my $album, my $album_details) = each %{$music_db{$artist}} ){
        $num_projects+=1;
    }
    
    # counter for the HTML because we only mention the Artist once for each project
    # thus, we need to do a unique format
    my $project_counter = 0;
    while ((my $album, my $album_details) = each %{$music_db{$artist}} ){

        if($project_counter == 0){
            print('<tr><td rowspan="',$num_projects,'">',$artist,'</td>');
            create_album_row($album_details,$album);
            print('</tr>');
        }
        else{
            print('<tr>');
            create_album_row($album_details,$album);
            print('</tr>')
        }
        $project_counter += 1;
    }
}
print('</table>');
print('</body></html>');