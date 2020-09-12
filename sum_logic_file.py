a = [[1,2,3],[4,5,6],[7,8,9]]
c = [] 

for index, value in enumerate(a): 
    b = 0 
    for idx, val in enumerate(a):
        b += a[idx][index]
    c.append(b)
         
print(c)
    
        
        

    
        
