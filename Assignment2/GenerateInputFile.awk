#! /usr/bin/gawk -f

find Music -type f | awk -F / '
{data[$3][$4][$NF] = $0}
END {
	for (artist in data) {
		for (album in data[artist]) {
			for (track in data[artist][album]) {
				print "	" data[artist][album][track]
}}}}
'| more > inputFile.txt
