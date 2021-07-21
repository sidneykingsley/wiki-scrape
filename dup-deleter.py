lines_seen = set()
outfile = open('names/oscar-winners-edited.txt', "w")
infile = open('names/oscar-winners.txt', "r")
for line in infile:
    print(line)
    if line not in lines_seen:  
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
for line in open('headings/musician-names/oscar-winners-edited.txt', "r"):
    print(line)