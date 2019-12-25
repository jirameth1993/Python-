#!/usr/bin/env python
# coding: utf-8

# In[17]:



import csv 
with open('tennis1.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    
print(data)    


# In[21]:


h = ['0','0','0','0','0','0']

for row in data:
    if row[-1] == 'TRUE' : 
        j = 0         
        for col in row:
            if col != 'TRUE' :
                if col != h[j]  and h[j] == '0' :
                    h[j] = col
                elif col != h[j] and h[j] != '0':
                    h[j] = '?'
                    
            j = j + 1 
print('Maximally Specific Hypothesis: ' , h)            
            
                
        


# In[ ]:





# In[ ]:




