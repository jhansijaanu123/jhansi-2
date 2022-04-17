str="jaanu"
print(len(str))
#method 2
def findlen(str):
    counter=0
    for i in str:
        counter +=1
    return counter
str="jaanu"
print(findlen(str)) 
#method 3
def findlen(str):
    counter=0
    while str[counter:]:
        counter +=1
    return counter
str="jaanu"
print(findlen(str)) 
#method 4
def findlen(str):
    if not str:
        return 0
    else:
        some_random_str='py'
        return ((some_random_str).join(str)).count(some_random_str)+1
str="jaanu"
print(findlen(str))                        
       