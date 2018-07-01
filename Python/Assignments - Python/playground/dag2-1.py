
# coding: utf-8

# In[8]:


lst = [1, 3, 'ahh', 2.4, [1, 2, 3], True, None, False]
type(lst)
print(lst)





# In[15]:


print(lst[0])
print(lst[len(lst) -1])
print(lst[-1])
print(lst[-4])


# In[19]:


lst[2:6]
lst[2:7:2]
lst[::2]


# In[21]:


len(lst)
print(len("hejhejhej"))


# In[24]:


lst[2] = "hello"
lst


# In[31]:


fst_sen = ["Call", "me", "later"]
numbers = [1, 2, 3, 4, 5]

', '.join(fst_sen) # , numbers)
fst_sen + numbers

fst_sen * 3


# In[29]:


del fst_sen[2]


# In[32]:


print(fst_sen)


# In[35]:


snd_sen = fst_sen[:]
print(snd_sen)


# In[38]:


a = sorted(fst_sen)
b = fst_sen.sort()
print(a)
print(b)


# In[42]:


lst = list(range(30, 15, -2))
range(5)


# In[43]:


20 in lst # not in or in, and keyword


# In[44]:


get_ipython().run_line_magic('timeit', '55000 in range(1000000)')


# In[46]:


def is_in(el, values):
    for value in values:
        if el == value:
            return True

get_ipython().run_line_magic('timeit', 'is_in(55000, range(1000000))')


# In[47]:


max(lst) # sum, min


# In[48]:


fst_word, snd_word, thr_word = fst_sen # _, snd_word, _ = fst_sen
print(fst_word, snd_word, thr_word)


# In[50]:


fst_sen = ["Test", "Test2", "test3"]

[el.lower() for el in fst_sen] # list comprehensive


# In[51]:


[value**2 for value in range(0, 21)]


# In[55]:


fst_sen = ["Test", "Test2", "Test3"] # list
fst_end = ("Test", "Test2", "Test3") # tuple

fst_sen[1] = "Test"
a,b,c = fst_end
tuple(fst_sen)


# In[56]:


set(["hej", 1, 2, 3, 4, 5, "hej"])

