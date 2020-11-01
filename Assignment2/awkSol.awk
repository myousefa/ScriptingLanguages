#! /usr/bin/gawk -f
BEGIN {
    FS = "/"

    print "<html>"
    print "<meta http-equiv=\"content-type\" content=\"text/html\"; charset=\"utf-8\"/> "
    print "<table border=\"1\">"
    print "<tr>"
    print "  <th>Artist</th>"
    print "  <th>Album</th>"
    print "  <th>Tracks</th>"
    print "</tr>"
}