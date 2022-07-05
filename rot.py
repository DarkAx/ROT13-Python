#!/usr/bin/env python3
def rot13(text):
	a=[chr(i) for i in range(97,123)]
	A=[chr(i) for i in range(65,91)]
	result=""
	for i in text:
		if i.islower():
			result+=a[(a.index(i)+13) % 26]
		elif i.isupper():
			result+=A[(A.index(i)+13) % 26]
		else:
			result+=i
	return result