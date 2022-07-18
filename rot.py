#!/usr/bin/env python3
def rot(text, num, encrypt=False): # The default is decrypting, To encrypt just pass a "True" argument to the function like this example: print(rot('sultan',13,True))
    a=[chr(i) for i in range(97,123)]; A=[chr(i) for i in range(65,91)]; result=""
    if encrypt:
       for i in text:
            if i.islower():
                result+=a[(a.index(i)+num) % 26]
            elif i.isupper():
                result+=A[(A.index(i)+num) % 26]
            else:
                result+=i
    
    else:
        for i in text:
            if i.islower():
                result+=a[(a.index(i)-num) % 26]
            elif i.isupper():
                result+=A[(A.index(i)-num) % 26]
            else:
                result+=i
    return result
