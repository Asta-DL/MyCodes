msg=input("enter your message: ")
command=input("1 for code and 0 for decode: ")
if command=="1":
    command= True
else:
    command=False    
words= msg.split(" ")
import random
import string
if (command):
    new_msg=[]
    for word in words:
        if (len(word)>=3):
            v1=''.join(random.choices(string.ascii_letters, k=3))
            v2=''.join(random.choices(string.ascii_letters, k=3))
            code= v1+ word[1:] + word[0] + v2
            new_msg.append(code)
        
        else:
            new_msg.append(word[::-1])
    print(" ".join(new_msg))    
else:
    new_msg=[]
    for word in words:
        if (len(word)>=3):
            code=word[3:-3]
            code= code[-1]+ code[:-1]
            new_msg.append(code)
        else:
            new_msg.append(word[::-1])
    print(" ".join(new_msg))                

    
    
        

