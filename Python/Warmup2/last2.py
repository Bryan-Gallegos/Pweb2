def last2(string):
	count=0
	for i in range(0,len(string)-2):
		if string[i:i+2]==string[-2:]:
			count+=1
	return count