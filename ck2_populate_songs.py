import os
import re
import fnmatch

outfile = open("songs.txt", "w")

#Setup ogg inclusion
includes = ['*.ogg']
includes = r'|'.join([fnmatch.translate(x) for x in includes])

#Step through the directory
for root, dirs, filenames in os.walk('.'):
	#Filter out everything but ogg files
    filenames = [f for f in filenames if re.match(includes, f)]

    #Write all entries
    for f in filenames:
        outfile.write("song = {\n")
        outfile.write("\tname = \"" + f + "\"\n")
        outfile.write("\n")
        outfile.write("\tchance = {\n")
        outfile.write("\t\tfactor = 1\n")
        outfile.write("\t}\n")
        outfile.write("}\n\n")

outfile.close()
