#!/usr/bin/perl -l
use warnings;
use strict;

my $filename = 'input.txt';

open(FH, '<', $filename) or die $!;
my %music_db = ();
while(<FH>){
    my @line_data = split('/',$_);
    

    my $artist = $line_data[2];
    my $album = $line_data[3];
    my $track = $line_data[-1];

    my %artist_projects = ();
    our @album_tracks = ();
    if(!exists $music_db{$artist}){
        # checking the artist is NOT in the Hash
        push(@album_tracks,$track);
        $music_db{$artist}{$album} = @album_tracks;
        #$music_db{$artist} = {$album=>5};

        #$music_db{$artist} => $artist_projects;
        #push(@album_tracks,$track)
        #%music_db{$artist} = ($album => @album_tracks);
        #%music_db{$artist}{$album} => @album_tracks;
    }
    # elsif(exists $music_db{$artist}){
    #     # checking the artist IS in the Hash
    #     # add the additional album
    #     $music_db{$artist} = ($album =>)
    # }

    # foreach my $i (@line_data)  
    # {
        
    #     print "$i --> "; 
    # }
}

close(FH);