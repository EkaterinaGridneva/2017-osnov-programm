import sys 
stopwords=['die', 'also', 'der', 'Putin','Vladimir','der','wo','gut','darin','Deutsche']
#count=[]
slovar ={}
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
	row =line.split(' ')
	# for each of the tokens
	for token in row:
		if token == '':
			continue
		# check if it is in the english wordlist
		if token in dot:
			#print (token)
		# if it is, take a count
			if token not in slovar:
				slovar [token]=0
			slovar[token]+=1
	
				
				#count.append (token)
					
#print (count)
print (slovar)
for token in slovar:
	if token in stopwords or token.isnumeric() or not token.isalnum():
		continue
	print (token , slovar [token]) 
