
# coding: utf-8

# # What, a list?
# 
# A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list do not have to be related in any particular way. 
# 
# Guideline:
#   * name of your lists in plural, such as `letters`, `digits`, or `names`
# 
# 
# Square brackets (`[]`) indicate a list, and individual elements in the list are separated by commas.

# In[2]:


[1, 2, 3, 1 , 2]


# In[4]:


numbers = [1, 2, 3]
type(numbers)


# In[1]:


words = ['cat', 'bat', 'rat', 'elephant']
words


# In[2]:


mixed_elements = ['hello', 3.1415, True, None, 42]
mixed_elements


# In[3]:


empty_list = []
empty_list


# ## Accessing Elements

# In[4]:


animals = ['cat', 'bat', 'rat', 'elephant']


# In[24]:


animals[3]


# In[6]:


animals[0] + 'woman and ' + animals[1] + 'man'


# ### Negative Indexes
# 
# How to get the last element of a list?

# In[7]:


animals[-1]


# In[8]:


animals[-3]


# ### Getting Sublists with Slices
# 
#   * `animals[2]`is a list with an index (one integer)
#   * `animals[1:4]` is a list with a slice (two integers)
#   
# In a slice, the  rst integer is the index where the slice starts. The second integer is the index where the slice ends. A slice goes up to, but will not include, the value at the second index. A slice evaluates to a new list value.
# 

# In[9]:


animals[1:4]


# In[10]:


animals[0:-1]


# In[11]:


animals[-2:-1]


# As a shortcut, you can leave out one or both of the indexes on either side of the colon in the slice. Leaving out the  rst index is the same as using 0, or the beginning of the list. Leaving out the second index is the same as using the length of the list, which will slice to the end of the list.

# In[12]:


animals[:3]


# In[25]:


animals[::2]


# ### Getting a List’s Length with `len()`
# 

# In[13]:


fst_sentence = ['Call', 'me', 'Ishmael']
len(fst_sentence)


# ### Changing Values in a List with Indexes

# In[14]:


fst_sentence = ['Call', 'me', 'Ishmael']

fst_sentence[1] = 'him'
fst_sentence


# In[15]:


fst_sentence[0] = fst_sentence[1]
fst_sentence


# In[16]:


fst_sentence[-1] = 1000
fst_sentence


# ### List Concatenation and List Replication
# 
#   * `+` operator combines two lists to create a new list value
#   * `*` operator can also be used with a list and an integer value to replicate the list

# In[18]:


fst_sentence = ['Call', 'me', 'Ishmael']
numbers = [1, 2, 3, 4]

concat = fst_sentence + numbers
concat


# In[19]:


fst_sentence * 3


# ### Removing Values from Lists with del Statements
# 
# The `del` statement will delete values at an index in a list. All of the values
# in the list after the deleted value will be moved up one index.

# In[20]:


fst_sentence = ['Call', 'me', 'Ishmael']

del fst_sentence[1]
fst_sentence


# ### Copying a List

# In[21]:


fst_sentence = ['Call', 'me', 'Ishmael']

new_sentence = fst_sentence[:]
new_sentence[1] = 'him'

print(fst_sentence)
print(new_sentence)


# ### Sorting the Values of a List with `sorted()`
# 
# The `sorted()` function returns a sorted **copy** of the corresponding list.

# In[31]:


fst_sentence = ['Call', 'me', 'Ishmael']
sorted_sentence = sorted(fst_sentence)
print(sorted_sentence)
print(fst_sentence)


# In[32]:


numbers = [2, 3, 1, -5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)


# # Sequences
# 
# In this course we consider sequences to be "list like". Technically, they are something different but this is beyound the scope of this course.
# 
# `range` returns a sequence of numbers from start to stop by a given step.

# In[33]:


range(5)


# In[34]:


list(range(5))


# In[36]:


list(range(3, 10))


# In[37]:


list(range(3, 20, 4))


# In[38]:


list(range(30, 10, -2))


# ### Checking Lists for Element Containment
# 
# You can determine whether a value is or isn’t in a list with the `in` and `not in` operators. Like other operators, in and not in are used in expressions and connect two values: a value to look for in a list and the list where it may be found.

# In[39]:


1 in [0, 1, 2, 3]


# In[40]:


1 in range(4, 0, -1)


# In[41]:


'Hej' in [0, 1, 2, 3]


# In[42]:


1 in ['Call', 'me', 'Ishmael']


# In[48]:


'Hej' in ['Call', 'me', 'Ishmael']


# In[44]:


1 not in ['Call', 'me', 'Ishmael']


# In[45]:


1 not in [0, 1, 2, 3]


# Make use of the operator instead of iterating through lists. It is way more performant. See the following meassurements:

# In[49]:


get_ipython().run_line_magic('timeit', '55000 in range(1000000)')


# In[50]:


def is_in(el, values):
    for value in values:
        if el == value:
            return True
        
get_ipython().run_line_magic('timeit', 'is_in(55000, range(1000000))')


# ### Simple Statistics with a List of Numbers
# 
# A few Python functions are specific to lists of numbers. For example, you can easily find the minimum, maximum, and sum of a list of numbers.

# In[51]:


values = list(range(10))

print(min(values))
print(max(values))
print(sum(values))


# ### Multiple Assignments
# 
# The multiple assignment trick is a shortcut that lets you assign multiple variables with the values in a list in one line of code.

# In[52]:


fst_sentence = ['Call', 'me', 'Ishmael']

fst_word = fst_sentence[0]
snd_word = fst_sentence[1]
thrd_word = fst_sentence[2]

print(fst_word, snd_word, thrd_word)


# In[59]:


fst_sentence = ['Call', 'me', 'Ishmael']

fst_word, snd_word, thrd_word = fst_sentence
print(fst_sentence)


# ## Methods
# 
# A method is the same thing as a function, except it is “called on” a value.
# For example, if a list value were stored in `fst_sentence`, you would call the `index()` list method on that list like so: `fst_sentence.index('hello')`. The method part comes after the value, separated by a period.
# Each data type has its own set of methods. The list data type, for example, has several useful methods for  finding, adding, removing, and otherwise manipulating values in a list.
# 
# ### Finding a Value in a List with the `index()` Method
# 
# List values have an `index()` method that can be passed a value.
# 
#   * If that value exists in the list, the index of the value is returned. 
#   * If the value isn’t in the list, then Python produces a `ValueError` error.
#   * When there are duplicates of the value in the list, the index of its  first appearance is returned.

# In[62]:


fst_sentence = ['Call', 'me', 'Ishmael']

fst_sentence.index('me')


# In[63]:


fst_sentence.index('hello')


# In[64]:


new_sentence = ['Call', 'me', 'me', 'Ishmael']

fst_sentence.index('me')


# ### Adding Values to Lists with the `append()` and `insert()` Methods
# 
# To add new values to a list, use the `append()` and `insert()` methods. The `append()` method call adds the argument to the end of the list. The `insert()` method can insert a value at any index in the list. The first argument to `insert()` is the index for the new value, and the second argument is the new value to be inserted.
# 
# **OBS!** `append()` and `insert()` modify the given list inplace. That is, no copy is generated.

# In[65]:


fst_sentence = ['Call', 'me', 'Ishmael']
fst_sentence.append('Holgerson')
fst_sentence


# In[66]:


fst_sentence = ['Call', 'me', 'Ishmael']
result = fst_sentence.append('Holgerson')
result


# In[67]:


fst_sentence = ['Call', 'me', 'Ishmael']
fst_sentence.insert(0, 'Please')
fst_sentence


# ### Removing Values from Lists with `remove()`
# 
# The `remove()` method is passed the value to be removed from the list it is called on. Attempting to delete a value that does not exist in the list will result in a `ValueError` error.

# In[68]:


fst_sentence = ['Call', 'me', 'Ishmael']
fst_sentence.remove('Niels')


# In[69]:


fst_sentence = ['Call', 'me', 'Ishmael']
fst_sentence.remove('Ishmael')
fst_sentence


# ### Sorting the Values of a List with the `sort()` Method
# 
# Lists of number values or lists of strings can be sorted with the `sort()` method.
# You can also pass `True` for the reverse keyword argument to have `sort()` sort the values in reverse order.
# 
# There are three things you should note about the `sort()` method. First, the `sort()` method sorts the list in place; do not try to capture the return value by writing code like 
# 
# ```python
# result = values.sort()
# ```
# 

# In[70]:


values = [2, 5, 3.14, 1, -7]
values.sort()
values


# In[71]:


fst_sentence = ['Call', 'me', 'Ishmael']
fst_sentence.sort()
fst_sentence


# In[72]:


values = [2, 5, 3.14, 1, -7]
values.sort(reverse=True)
values


# You cannot sort lists that have both number values *and* string values in them, since Python does not know how to compare these values.

# In[73]:


values = ['Call', 'me', 'Ishmael', 2, 5, 3.14, 1, -7]
values.sort()
values


# `sort()` uses "ASCIIbetical order" rather than actual alphabetical order for sorting strings. This means uppercase letters come before lower- case letters. Therefore, the lowercase a is sorted so that it comes after the uppercase Z.

# In[ ]:


fst_sentence = ['Call', 'call', 'me', 'Me', 'ishmael', 'Ishmael']
fst_sentence.sort()
fst_sentence


# If you need to sort the values in regular alphabetical order, pass `str.lower` for the `key` keyword argument in the `sort()` method call, causes the `sort()` function to treat all the items in the list as if they were lowercase without actually changing the values in the list.

# In[74]:


fst_sentence = ['a', 'z', 'A', 'Z']
fst_sentence.sort(key=str.lower)
fst_sentence


# ### Joining a List into a String
# 
# Actually, `join` is a methond on strings. But you will see it often to join the values of a list into a single string.

# In[77]:


fst_sentence = ['Call', 'me', 'Ishmael']
(';').join(fst_sentence)


# ### Reversing a List

# In[78]:


fst_sentence = ['Call', 'me', 'Ishmael']
fst_sentence.reverse()
fst_sentence


# ## List Comprehensions
# 
# A list comprehension allows you to generate arbitrary lists in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. List comprehensions are not always presented to beginners, but I have included them here because you’ll most likely see them as soon as you start looking at other people’s code, they may make your code more concise, and they have a better performance than normal loops.

# In[79]:


squares = [value**2 for value in range(0, 21)]
squares


# # List-like Types: Strings, Tuples, and Sets
# 
# Lists are not the only data types that represent ordered sequences of values. For example, strings and lists are actually similar, if you consider a string to be a "list" of single text characters. Many of the things you can do with lists can also be done with strings: indexing; slicing; and using them with for loops, with `len()`, and with the `in` and `not in` operators.

# In[ ]:


name = 'Ishmael'
print(name[0])
print(name[-2])

print(name[0:4])
print('Me' in name)
print('s' in name)
print('p' not in name)

for i in name:
    print('* * * ' + i + ' * * *')


# ## Mutable and Immutable Data Types
# 
# Lists and strings are different in an important way. A list value is a *mutable* data type: It can have values added, removed, or changed. However, a string is *immutable*: It cannot be changed. Trying to reassign a single character in a string results in a `TypeError` error.
# 
# Consequently, the proper way to "mutate" a string is to use slicing and concatenation to build a new string by copying from parts of the old string.

# In[ ]:


name = 'Ishmael'
name[3] = 'x'


# In[ ]:


sentence = 'Ishmael a whaler'

new_sentence = sentence[0:8] + 'the' + sentence[9:]
print(new_sentence)


# We used `[0:8]` and `[9:]` to refer to the characters that we do not wish to replace. Notice that the original `'Ishmael a whaler'` string is not modified because strings are *immutable*.
# 
# ## The Tuple Data Type
# 
# The tuple data type is almost identical to the list data type, except in two ways. First, tuples are typed with parentheses, `(` and `)`, instead of square brackets, `[` and `]`.
# 
# The main way that tuples are different from lists is that tuples, like strings, are immutable. Tuples cannot have their values modified, appended, or removed.
# 
# If you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses. Otherwise, Python will think you’ve just typed a value inside regular parentheses. The comma is what lets Python know this is a tuple value. (Unlike some other programming languages, in Python it is  ne to have a trailing comma after the last item in a list or tuple.)

# In[80]:


earnings = ('Moby Dick', 150, 556)
earnings[1] = 300


# In[81]:


earnings = ('Moby Dick',)
earnings


# ### Looping Through All Values in a Tuple
# 
# You can loop over all the values in a tuple using a for loop, just as you did with a list.

# In[82]:


earnings = ('Moby Dick', 150, 556)

for element in earnings:
    print(element)


# ### Converting Types with the `list()` and `tuple()` Functions
# 
# Just like how `str(42)` will return `'42'`, the string representation of the integer 42, the functions `list()` and `tuple()` will return list and tuple versions of the values passed to them. 

# In[ ]:


earnings = ('Moby Dick', 150, 556)
earnings_list = list(earnings)

fst_sentence = ['Call', 'me', 'Ishmael']
fst_sentence_tuple = tuple(fst_sentence)

print(earnings_list)
print(fst_sentence_tuple)

print(list('Ishmael'))


# ## References
# 
# You assign `'Ishmael'` to the `name` variable, and then you copy the value in `name` and assign it to the variable `other_name`. When you later change the value in `name` to `Ahab`, this does not affect the value in `other_name`. This is because `name` and `other_name` are different variables that store different values.
# 
# 
# But lists do not work this way! When you assign a list to a variable, you are actually assigning a list reference to the variable. A reference is a value that points to some bit of data, and a list reference is a value that points to a list.
# 
# We can illustrate the different behaviour of the following two programs here:
# http://www.pythontutor.com/visualize.html

# In[83]:


name = 'Ishmael'
other_name = name
name = 'Ahab'
print(name)
print(other_name)


# In[ ]:


fst_sentence = ['Call', 'me', 'Ishmael']

new_sentence = fst_sentence
new_sentence[1] = 'him'

print(fst_sentence)


# ### Passing References
# 
# References are particularly important for understanding how arguments get passed to functions. When a function is called, the values of the arguments are copied to the parameter variables. For lists (and dictionaries, see next notebook), this means a copy of the reference is used for the parameter.
# 
# Notice that when `rate(list_arg)` is called, a return value is not used to assign a new value to `fst_sentence`. Instead, it modifies the list in place, directly. When run, this program produces the following output:
# 
# ```python
# ['Call', 'me', 'Ishmael', '... Nice!']
# ```
# 
# Even though `fst_sentence` and `list_arg` contain separate references, they both refer to the same list. This is why the `append('... Nice!')` method call inside the function affects the list even after the function call has returned.
# Keep this behavior in mind. Forgetting that Python handles list and dictionary variables this way can lead to confusing bug!
# 
# 

# In[ ]:


def rate(list_arg):
    list_arg.append('... Nice!')
    
fst_sentence = ['Call', 'me', 'Ishmael']

rate(fst_sentence)
print(fst_sentence)


# ### The copy Module’s `copy()` and `deepcopy()` Functions
# 
# Although passing around references is often the handiest way to deal with lists and dictionaries, if the function modifies the list or dictionary that is passed, you may not want these changes in the original list or dictionary value. For this, Python provides a module named copy that provides both the `copy()` and `deepcopy()` functions. The  first of these, `copy.copy()`, can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.
# 
# If the list you need to copy contains lists, then use the `copy.deepcopy()` function instead of `copy.copy()`. The `deepcopy()` function will copy these inner lists as well.

# In[ ]:


import copy

fst_sentence = ['Call', 'me', 'Ishmael']

new_sentence = copy.copy(fst_sentence)
new_sentence[1] = 'him'

print(fst_sentence)
print(new_sentence)


# ## Sets
# 
# Sets are like lists, only that every element is unique.

# In[84]:


set(['Hej', 1, 2, 3, 4, 4, 'Hej',])


# # Exercises
# 
# ![get_started](https://s-media-cache-ak0.pinimg.com/originals/9f/73/e3/9f73e3f8a958dbe03b0f76f8811a54a1.gif)
# 
#   1. Create a list with the integer values from one to one million. Use `min()` and `max()` to make sure your list actually starts at one and ends at one million. Also, use the `sum()` function to compute the sum of all values and `%timeit`'s execution time.
#   2. Write a single line program that computes the sum of a range of integer values without using the `sum()` function and without using a loop.
#   3. Use the `range()` function to make a list of the odd numbers from 1 to 20. **Hint** in ipython and this notebooks you can see a functions help text by executing for example `range?`
#   4. Create a list of the multiples of 3 from 3 to 30. **HINT: USE A LIST COMPREHENSION**
#   5. A number raised to the third power is called a cube. For example, the cube of 2 is written as `2**3` in Python. Create a list of the first 10 cubes (that is, the cube of each integer from 1 through 10).
# 

# ### Using `timeit` from within scripts/programs
# 
# In your file `<my_prg>.py` import the `timeit` module and call the `timeit` function on a string with the python code to time.
# 
# 
# ```python
# import timeit
# 
# cmd = '"-".join(str(n) for n in range(100))'
# print(timeit.timeit(cmd, number=10))
# ```

# ***References:*** Almost everything in this notebook, text and exercises, is based on chapter four of the book "Python Crash Course: A Hands-On, Project-Based Introduction to Programming" by Eric Matthes (https://www.nostarch.com/pythoncrashcourse/).

# # Student Solutions

# In[33]:


lst = range(1, 1000001)
min(lst), max(lst)
# sum(lst)
#%timeit(sum(lst))

my_sum1 = (max(lst) * (max(lst) +  min(lst)) / 2)
(lst[-1] * (lst[-1] +  lst[0]) / 2)


# In[ ]:


# 1
lst = range(1, 1000001)
min(lst), max(lst)
sum(lst)
get_ipython().run_line_magic('timeit', '(lst)')

#2
lst = (2 + 3 + 4)
lst


#3
lst = list(range(1, 20, 2))
lst

#4
[value*3 for value in range(3, 30)]

#5
[value**3 for value in range(1, 10)]


# krb
# 1
from_1_to_1_million = list(range(1,100001))
# 2
# line intentionally left blank
# 3 
odd_1_to_20 = list(range(1,21,2))
# 4
# nvm, wrong -- multiple_3_to_30 = [x*3 for x in range(3,31)]
# 5
cubes_1_to_10 = [z**3 for z in range(1,11)]


# another solutions
numbers = range(1, 1000001)
print("max:", max(numbers))
print("min:", min(numbers))

print("sum:", reduce(lambda accumulator, next_element: accumulator + next_element, numbers))

odd_numbers = list(range(1, 21, 2))
print("odd numbers:", odd_numbers)

multipliers = list(range(3, 31, 3))
print("multipliers of three:", multipliers)

cubes = [x ** 3 for x in range(1, 11)]
print("cubes:", cubes)


#solution to sum
my_sum1 = (maximum * (maximum+  minimum) / 2)








# In[5]:


# 2. exercise
a = list(range(1, 1000001))
sum_result = (a[0] + a[-1]) * len(a) / 2

# 3. exercise
list(range(1, 20, 2))

# 4. exercise
[i * 3 for i in range(3, 30)]

# 5. exercise
[value ** 3 for value in range(1, 10)]

