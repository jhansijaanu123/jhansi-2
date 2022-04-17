s="jaanu jhansi raj"
words=s.split(' ') 
string=[]
for word in words:
    string.insert(0,word) 
print("reversed string:") 
print(" ".join (string))    