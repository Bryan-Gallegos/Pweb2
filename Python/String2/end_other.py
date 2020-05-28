def end_other(a,b):
	long_s, short_s = (a,b) if len(a) >= len(b) else (b,a)
	return long_s.lower().endswith(short_s.lower())
	def xyz_there(str):
		i=0
		while "xyz" in str[i:]:
			if str[i-1+str[i:].index("xyz")] != ".":
				return True
			i += str[i:].index("xyz")+2
		return False