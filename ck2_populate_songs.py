import os

outfile = open("songs.txt", "w")

indir = '.'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        outfile.write("song = {\n")
        outfile.write("\tname = \"" + f + "\"\n")
        outfile.write("\n")
        outfile.write("\tchance = {\n")
        outfile.write("\t\tfactor = 1\n")
        outfile.write("\t}\n")
        outfile.write("}\n\n")