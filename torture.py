import sys 
count=[]
dot=[] # list of english words
fd=open('dot', 'r')
# read in list of english words
for line in fd.readlines():
         line=line.strip()
         dot.append (line)

# for line in the german corpus
Corpusde=[]
fd=open ('Corpus.de.txt.txt','r')
# read in list of german words
for line in fd.readlines():
	line=line.strip()
	Corpusde.append (line)
	# tokenise the line
	row = newline.split(' ')
	# for each of the tokens
	for token in row:
		if token != '':
		# check if it is in the english wordlist
		if token in dot:
			print (token)
		# if it is, take a count

			count.append (token)
					
print (count)
