import sys 

dot=[] # list of english words
fd=open('dot', 'r')
# read in list of english words
for line in fd.readlines():
         line=line.strip()
         dot.append (line)

# for line in the german corpus
	# tokenise the line
	# for each of the tokens
		# check if it is in the english wordlist
		# if it is, take a count
