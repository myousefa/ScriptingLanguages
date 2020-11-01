#! /usr/bin/gawk -f

find Music -type f | awk -F / '
{data[$3][$4][$NF] = $0}
END {
	for (artist in data) {
		print artist
		for (album in data[artist]) {
			print "	" album
			for (track in data[artist][album]) {
				print "	" track; print "	" data[artist][album][track]
}}}}
'| more
