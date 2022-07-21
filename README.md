# ROT-Python
Simple and readable python code that encrypt or decrypt for any ROT cipher (ROT 1 to ROT 25).


### ``ROT("text", num)`` where num is 1 - 25

### After downloading the file, create a new python file and write:
    from ROT import *
     
    print(ROT("text", num))

###  To encrypt just pass True argument to the function call; such as this:
		
    print(ROT("sultan", 13, True)) 
### This will encrypt the text to ROT13 cipher.
