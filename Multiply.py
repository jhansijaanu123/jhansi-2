a=[[7,3,6],
  [5,6,8], 
  [8,9,8]]
b=[[8,1,2],
  [6,3,0], 
  [4,5,1]]
result=[[0,0,0],
      [0,0,0], 
      [0,0,0]]  
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j]+=a[i][k] *b[k][j]
for r in result:
    print(r)