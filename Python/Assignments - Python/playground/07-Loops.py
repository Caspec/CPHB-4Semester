
# coding: utf-8

# # `for` Loops
# 
# ## Iterating over Lists and Sequences

# In[1]:


for i in [0, 1, 2, 3]:
    print(i)


# In[2]:


for i in range(4):
    print(i)


# ## Iterating over Lists and Sequences with Indices
# 
# In case you want to iterate over a list or sequence of values in and you need to have access to the index of each element, you could do the following:

# In[3]:


values = range(4, 0, -1)
for idx in range(len(values)):
    print(idx, values[idx])


# However, **do not do it as shown above**! First, it is more complicated and second, it is not "Pythonic". Instead do the following:

# In[4]:


for idx, value in enumerate(range(4, 0, -1)):
    print(idx, value)


# ## Checking Lists for Element Containment

# In[5]:


1 in [0, 1, 2, 3]


# In[6]:


1 in range(4, 0, -1)


# In[7]:


'Hej' in [0, 1, 2, 3]


# In[8]:


1 in ['Call', 'me', 'Ishmael']


# In[9]:


'Hej' in ['Call', 'me', 'Ishmael']


# In[10]:


get_ipython().run_line_magic('timeit', '55000 in range(1000000)')


# In[11]:


def is_in(el, values):
    for value in values:
        if el == value:
            return True
        
get_ipython().run_line_magic('timeit', 'is_in(55000, range(1000000))')


# # `while` Loops
# 
# The `for` loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the `while` loop runs as long as, or while, a certain condition is `True`.
# 
# It has the syntax:
# 
# ```python
# while boolean_expression:
#     pass
# ```
# 

# In[12]:


# counting to five
current_number = 0

while current_number <= 5:
    print(current_number)
    current_number += 1


# A computer program's main loop, such as the one of this notebook, is very likely implemented via a `while` loop.
# 
# To exit a `while` loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement. The `break` statement directs the  ow of your program; you can use it to control which lines of code are executed and which are not, so the program only executes code that you want it to, when you want it to.
# 
# Note, you can use the `break` statement in any of Python’s loops. For example, you could use break to quit a for loop that is working through a list or a dictionary.

# In[16]:


while True:
    expression = input()
    if expression == 'quit!':
        break
    print(eval(expression))


# Rather than breaking out of a loop entirely without executing the rest of its code, you can use the `continue` statement to return to the beginning of the loop based on the result of a conditional test.

# In[15]:


while True:
    expression = input()
    if expression == 'quit!':
        break
    if expression == 'nop!':
        continue
    print(eval(expression))


# In[ ]:


get_ipython().run_line_magic('pinfo', 'eval')


# # Exercises!!!
# 
# ![image](https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif)
# 
#   1. Write a program that creates gramatically valid English sentences.
#     * Here, we consider a sentence to be gramatically correct when it follows the simple English grammar of the form: `Article Adjective Noun Verb.` That is, even the sentence `A insect fly.` is, for the moment, considered correct.
#     * Create additionally to the exercise above, a list of definite and indefinite articles and verbs from an online resource.
#   2. Extend the above program to generate all possible sentences with the given words.

# # Student Solutions

# In[13]:


import random

adject = ['Adamant', 'unyielding', 'a very hard substance', 'Adroit', 'clever', 
          'resourceful', 'Amatory', 'sexual', 'Animistic', 'Antic', 'clownish', 
          'frolicsome', 'Arcadian', 'serene', 'Baleful', 'deadly', 'foreboding',
          'Bellicose', 'quarrelsome', 'Bilious', 'unpleasant', 'peevish',
          'Boorish', 'crude', 'insensitive', 'Calamitous', 'disastrous',
          'Caustic', 'corrosive', 'sarcastic', 'Cerulean', 'sky blue',]

noun = ["time", "year", "people", "way", "day", "man", "thing", "woman",
        "life", "child", "world", "school", "state", "family", "student", 
        "group", "country", "problem", "hand", "part", "place", "case", 
        "week", "company", "system", "program", "question", "work", 
        "government", "number", "night", "point", "home", "water", "room", 
        "mother", "area", "money", "story", "fact", "month", "lot", "right", 
        "study", "book", "eye", "job", "word", "business", "issue", "side", 
        "kind", "head", "house", "service", "friend", "father", "power", 
        "hour", "game", "line", "end", "member", "law", "car", "city", 
        "community", "name", "president", "team", "minute", "idea", "kid", 
        "body", "information", "back", "parent", "face", "others", "level", 
        "office", "door", "health", "person", "art", "war", "history", 
        "party", "result", "change", "morning", "reason", "research", "girl", 
        "guy", "moment", "air", "teacher", "force", "education"]

randomAdjec = random.choice(adject)
randomNoun = random.choice(noun)
print((' ').join([randomAdjec, randomNoun]))


# In[12]:


import random
# https://www.espressoenglish.net/100-common-adjectives-in-english/ 
adj = ["other", "new", "good", "high", "old", "great", "big", "American",
       "small", "large", "national", "young", "different", "black", "long", 
       "little", "important", "political", "bad", "white", "real", "best", 
       "right", "social", "only", "public", "sure", "low", "early", "able", 
       "human", "local", "late", "hard", "major", "better", "economic", 
       "strong", "possible", "whole", "free", "military", "true", "federal", 
       "international", "full", "special", "easy", "clear", "recent", 
       "certain", "personal", "open", "red", "difficult", "available", 
       "likely", "short", "single", "medical", "current", "wrong", "private", 
       "past", "foreign", "fine", "common", "poor", "natural", "significant", 
       "similar", "hot", "dead", "central", "happy", "serious", "ready", 
       "simple", "left", "physical", "general", "environmental", "financial", 
       "blue", "democratic", "dark", "various", "entire", "close", "legal", 
       "religious", "cold", "final", "main", "green", "nice", "huge", 
       "popular", "traditional", "cultural"] 

articles = ["the", "a", "an"] 

# https://www.espressoenglish.net/100-common-nouns-in-english/ 
nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman",
         "life", "child", "world", "school", "state", "family", "student", 
         "group", "country", "problem", "hand", "part", "place", "case", 
         "week", "company", "system", "program", "question", "work", 
         "government", "number", "night", "point", "home", "water", "room", 
         "mother", "area", "money", "story", "fact", "month", "lot", "right", 
         "study", "book", "eye", "job", "word", "business", "issue", "side", 
         "kind", "head", "house", "service", "friend", "father", "power", 
         "hour", "game", "line", "end", "member", "law", "car", "city", 
         "community", "name", "president", "team", "minute", "idea", "kid", 
         "body", "information", "back", "parent", "face", "others", "level", 
         "office", "door", "health", "person", "art", "war", "history", 
         "party", "result", "change", "morning", "reason", "research", "girl", 
         "guy", "moment", "air", "teacher", "force", "education"] 

# https://www.espressoenglish.net/100-most-common-english-verbs/ 
verbs = ["be", "have", "do", "say", "go", "can", "get", "would", "make",        
         "know", "will", "think", "take", "see", "come", "could", "want", 
         "look", "use", "find", "give", "tell", "work", "may", "should", 
         "call", "try", "ask", "need", "feel", "become", "leave", "put", 
         "mean", "keep", "let", "begin", "seem", "help", "talk", "turn", 
         "start", "might", "show", "hear", "play", "run", "move", "like", 
         "live", "believe", "hold", "bring", "happen", "must", "write", 
         "provide", "sit", "stand", "lose", "pay", "meet", "include", 
         "continue", "set", "learn", "change", "lead", "understand", "watch", 
         "follow", "stop", "create", "speak", "read", "allow", "add", "spend", 
         "grow", "open", "walk", "win", "offer", "remember", "love", 
         "consider", "appear", "buy", "wait", "serve", "die", "send", "expect", 
         "build", "stay", "fall", "cut", "reach", "kill", "remain"]

for x in articles:
    for v in adj:
        for y in nouns:
            for z in verbs:
                print(' '.join([x, v, y, z]))

lst = []
for art in articles:
    for adjec in adj:
        for noun in nouns:
            for verb in verbs:
                lst.append(art + " " + adjec + " " + noun + " " + verb)
            
print(len(lst))


# In[16]:


import random

sentences = []
for a in range(len(articles)):
    for b in range(len(nouns)):
        for c in range(len(verbs)):
            sentences.append(articles[a] + " " + nouns[b] + " " + verbs[c])

amount_of_sentences = len(articles) * len(nouns) * len(verbs)
print('There are {} possible sentences. I just print ten of them...'.format(
    amount_of_sentences))

for sentence in range(0, 20):
    print(random.choice(sentences))

