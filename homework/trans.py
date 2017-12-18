import sys
sent_id=1

table = {'b':'bˠ',
	 'd':'d̪ˠ',
	 'f':'fˠ',
	 'g':'ɡ',
	 'dh':'ɣ',
	 'sh':'h',
	 'c':'k',
	 'l':'l̪ˠ',
	 'm':'mˠ',
	 'n':'nˠ',
	 'ng':'ŋ',
	 'p':'pˠ',
	 'rr':'ɾˠ',
	 's':'sˠ',
	 't':'t̪ˠ',
	 'bh':'w',
	 'ch':'x',
	 'e':'ɛ',
	 'a':'a',
	 'i':'ɪ',
	 'o':'ɔ',
	 'u':'ʊ',
	 'ia':'iə',
	 'ua':'uə',
	 'agha':'əi',
	 'eabha':'əu',
	 'á':'aː',
	 'é':'eː',
	 'í':'iː',
	 'ó':'oː',
	 'ú':'uː'}

    #read through lines
for line in sys.stdin.readlines():
	line = line.strip('\n') #remove newlines
	if line == '':  #if the line is blank (sentence boundary)
		print()
		continue
	if line[0] == '#': # if the line is a comment
		print(line)
		continue

	row = line.split('\t')
  	# take the wordform (col 2)
	transliterated = row[1]

	  # transliterate!!!!
  
	row[9] = ('Tr=' + transliterated)

	  #print out line (separated by tabs)
	print('\t'.join(row))
