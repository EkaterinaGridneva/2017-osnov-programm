dot=[] # list of english words
fd=open('dot', 'r')
# read in list of english words
for line in fd.readlines():
         line=line.strip()
         dot.append (line)

