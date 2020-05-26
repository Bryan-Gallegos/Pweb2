def string_splosion(string):
	result=""
	for i in range(1,len(string)+1):
		result+=string[:i]
	return result