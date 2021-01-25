#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Enter your number:')
n= int(input())


def g_matrix(n):
    if n<0:
        return []
    matrix=[row[:] for row in [[0]*n]*n]
    current=1
    
            
    for r in range(0,n):
        for c in range(0,n):
                    matrix[r][c]=current
                    current+=1
                    #c-=1
    return matrix
    
        
a=g_matrix(n)       
a 



# In[2]:


def spiral_print(n,b):
    #i=1
    for i in range(n):
          print(b[0][i])
    for i in range(1,n):
        print(b[i][n-1])
    #i-=1
    n-=1
    for i in range(n-1,-1,-1):
            print(b[n][i])
    for i in range(n):
        print(b[n-1][i])
    
print(spiral_print(3,a))  


# In[ ]:




