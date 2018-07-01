
# coding: utf-8

# In[7]:


lst = list(range(0, 1000001))
max(lst)




# In[8]:


min(lst)


# In[18]:


#%timeit sum((lst))
mysum1 = (max(lst) * (max(lst) + min(lst)) / 2 )
get_ipython().run_line_magic('timeit', '(mysum1)')


# In[20]:


for i in [0, 1, 2, 3]:
    print(i)

for i in "Hallo, i am here!".split():
    print(i)


# In[ ]:


sum(lst)


# In[24]:


#values = range(4, 0, -1)
#list(range(len(values)))

#for idx in range(len(values)):
#    print(idx, values[idx])

for idx, el in enumerate(values):
    print(idx, el)


# In[26]:


number = 0
while number <= 5:
    print(number)
    number += 1


# In[28]:


while True:
    expression = input()
    if expression == "quit!":
        break
    if expression == "nop!":
        continue
    print(eval(expression))

