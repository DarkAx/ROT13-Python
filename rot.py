#!/usr/bin/env python3
def rot(text, num, encrypt=False): # The default is decrypting, If you want to encrypt just pass to the function a 'True' value, like this one: print(rot('sultan',13,True))
    if encrypt:
        a=[chr(i) for i in range(97,123)]; A=[chr(i) for i in range(65,91)]; result=""
        for i in text:
            if i.islower():
                result+=a[(a.index(i)-num) % 26]
            elif i.isupper():
                result+=A[(A.index(i)-num) % 26]
            else:
                result+=i
        return result
    
    else:

        a=[chr(i) for i in range(97,123)]; A=[chr(i) for i in range(65,91)]; result=""
        for i in text:
            if i.islower():
                result+=a[(a.index(i)+num) % 26]
            elif i.isupper():
                result+=A[(A.index(i)+num) % 26]
            else:
                result+=i
        return result
