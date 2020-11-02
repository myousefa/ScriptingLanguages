#!/usr/bin/perl -l
use warnings;
use strict;
use Data::Dumper;

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



my %music_db = read_file();
#print Dumper(\%music_db);
# #print(%music_db);
foreach my $artist (keys %music_db){
    while ((my $album, my @album_details) = each %{$music_db{$artist}} ){
        print($artist,"--> ",@album_details," --> ", @album_details[0]);
        foreach my $track ( @album_details ){
            print($track);
        }
    }
}