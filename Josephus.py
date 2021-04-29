#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Iterative method
def josephus(n,k):
    a=[]
    for i in range(1,n+1):
        a.append(i)
    i=0
    while(len(a)>1):
        print(i)
        print(a)
        i=i+k-1
        print(i)
        if(i>len(a)-1):
            i=i%len(a)
        a.pop(i)
    return a      
        


# In[2]:


#Recursive Method
def josephus(n,k):
    if n==1:
        return 1
    
    else:
        d= josephus(n-1,k)+k-1
        c= d%n + 1
        
    return c    


# In[ ]:




