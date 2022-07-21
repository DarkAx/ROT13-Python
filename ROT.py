def ROT(text, num, encrypt=False): # where num is 1 - 25
	'''Any shift cipher from ROT 1 to ROT 25
	   
	
		Usage: ROT(text, num)

	   To encrypt just pass to the function a 'True' argument like this one : 

				print(ROT('sultan', 13 ,True))'''

		
	a=[chr(i) for i in range(97,123)]; A=[chr(i) for i in range(65,91)]; result=""

	for i in text:
		if encrypt:
			
			if i.islower():
				result+=a[(a.index(i)-num) % 26]
			elif i.isupper():
				result+=A[(A.index(i)-num) % 26]
			else:
				result+=i
		
		else:

			if i.islower():
				result+=a[(a.index(i)+num) % 26]
			elif i.isupper():
				result+=A[(A.index(i)+num) % 26]
			else:
				 result+=i

	return result
