def ROT(text, encrypt=False):

		
a=[chr(i) for i in range(97,123)]; A=[chr(i) for i in range(65,91)]; result=""

if encrypt: num = 13
else: num = -13
	
	for i in text:
	    
		
			
		if i.islower():
				result+=a[(a.index(i)+num) % 26]
		elif i.isupper():
				result+=A[(A.index(i)+num) % 26]
		else:
				result+=i
				
	return result
