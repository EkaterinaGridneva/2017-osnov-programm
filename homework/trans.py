import sys
sent_id=1

table = {'a':'a',
	 'aː':'æ',
	 'bˠ':'bˠ',
	 'bʲ':'bʲ',
	 'c':'c',
	 'ç':'ç',
	 'd̪ˠ''d̪ˠ',
	 'dʲ':'d̠ʲ'
	 

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
