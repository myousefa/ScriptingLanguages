#! /usr/bin/gawk -f

# BEGIN {
#     FS = "/"
#     # boiler plate code for
#     # Creating the HTML table format
#     print "<html>"
#     print "<meta http-equiv=\"content-type\" content=\"text/html\"; charset=\"utf-8\"/> "
#     print "<table border=\"1\">"
#     print "<tr>"
#     print "  <th>Artist</th>"
#     print "  <th>Album</th>"
#     print "  <th>Tracks</th>"
#     print "</tr>"
# }

#Set up the data structure
#find Music -type f | awk -F / '
awk -F /'
{data[$3][$4][$NF] = $0}
END {
    for(artists in data) {
        print artists
        for(album in data[artists]) { 
            print "     " album
            for (track in data[artist][album]) {
                print "         " track ; print "                " data[artist][album]
            }
        }
    }
}'
# Run loop to add information into the data structure created

# It will also print the HTML code


