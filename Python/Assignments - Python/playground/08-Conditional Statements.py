
# coding: utf-8

# # A First Example
# Programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python’s `if` statement allows you to examine the current state of a program and respond appropriately to that state.

# In[ ]:


titles = ['moby-dick; or, the whale', 'dracula', 'adventures of huckleberry finn', 
         'the adventures of sherlock holmes', 'alice\'s adventures in wonderland']

for title in titles:
    if 'moby-dick' in title:
        print(title.upper())
    else:
        print(title.title())


# # Conditional Tests
# 
# At the heart of every `if` statement is an **expression** that can be evaluated as `True` or `False` and is called a conditional test. Python uses the values `True` and `False` to decide whether the code in an `if` statement should be executed. If a conditional test evaluates to `True`, Python executes the code following the `if` statement. If the test evaluates to `False`, Python ignores the code following the if statement.
# 
# That is, conditional test are just **Boolean Expressions**.  *"A Boolean expression is an expression in a programming language that produces a Boolean value when evaluated, i.e. one of true or false. A Boolean expression may be composed of a combination of the Boolean constants true or false, Boolean-typed variables, Boolean-valued operators, and Boolean-valued functions."* Gries, David; Schneider, Fred B. (1993), "Chapter 2. Boolean Expressions", A Logical Approach to Discrete Math, Monographs in Computer Science, Springer, p. 25

# In[ ]:


name = 'Ishmael'

# Check for equality
if name == 'Ishmael':
    print('Reading Moby Dick.')
    
# Check for inequality
if name != 'Ishmael':
    print('Reading something else.')


# ## Comparison Operators
# 
# Comparison operators compare two values and evaluate down to a single Boolean value.
# 
# |Operator|Meaning|
# |--|--|
# | `==` | Equal to |
# | `!=` | Not equal to |
# | `<` | Less than |
# | `>` | Greater than |
# | `<=` | Less than or equal to |
# | `>=` | Greater than or equal to |
# 
# 

# In[ ]:


42 == 42


# In[ ]:


42 == 99


# In[ ]:


2 != 3


# In[ ]:


2 != 2


# In[ ]:


'Hej' == 'Hej'


# In[ ]:


'Hej' == 'hej'


# In[ ]:


True == True


# In[ ]:


True != False


# In[1]:


42 == 42.0


# In[3]:


42 == '42'


# ## Boolean operators
# 
# The and and or operators always take two Boolean values or expressions, i.e., they are binary operators. The `and` operator evaluates an expression to `True` if both Boolean values are `True`; otherwise, it evaluates to `False`.
# 
# On the other hand, the or operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False.
# 
# |Expression|Evaluates to...|
# |--|--|
# | `True and True` | `True` |
# | `True and False` | `False` |
# | `False and True` | `False` |
# | `False and False` |`False` |
# 
# |Expression|Evaluates to...|
# |--|--|
# | `True or True` | `True` |
# | `True or False` | `True` |
# | `False or True` | `True` |
# | `False or False` |`False` |
# 
# 
# Unlike and and or, the `not` operator operates on only one Boolean value or expression. The `not` operator simply evaluates to the opposite Boolean value, i.e., its negation.
# 
# |Expression|Evaluates to...|
# |--|--|
# | `not True` | `False` |
# | `not False` | `True` |
# 

# In[ ]:


True and True


# In[ ]:


True and False


# In[ ]:


(5 > 4) and True


# In[ ]:


False or (100 / 2 == 50)


# In[ ]:


not not not not True


# In[ ]:


2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2 and not 'Hej'.startswith('O')


# ## Checking Whether a Value is in a List
# 
# Recall from the session on lists, that you have the `in` operator to check wether a value is a member of a list.

# In[ ]:


1 in [0, 1, 2, 3]


# In[ ]:


1 not in [0, 1, 2, 3]


# # `if` Statements
# 
# ## Simple if Statements
# The simplest kind of if statement has one test and one action:
# 
# ```python 
# if conditional_test: 
#     statements
# ```
# 
# 
# If the conditional test evaluates to `True`, Python executes the code following the `if` statement. If the test evaluates to `False`, Python ignores the code following the `if` statement.

# In[8]:


if 5 > 4:
    print('Yep, right!')
    print('Still, right!')


# **OBS!** Remember intendation to match your intents.

# In[ ]:


if 5 < 4:
    print('Yep, right!')
print('Still, right!')


# ## `if`-`else` Statements
# 
# An if-else block is similar to a simple if statement, but the else statement allows you to de ne an action or set of actions that are executed when the conditional test fails.

# In[ ]:


title = 'Moby-Dick; or, the Whale'

if 'Moby-Dick' in title:
    print('by Herman Melville')
else:
    print('hmm, I do not know the author.')


# ## The if-elif-else Chain
# 
# Often, you’ll need to test more than two possible situations, and to evaluate these you can use Python’s `if`-`elif`-`else` syntax. Python executes only one block in an if-elif-else chain. It runs each conditional test in order until one passes. When a test passes, the code following that test is executed and subsequent tests are skipped. You can use as many elif blocks in your code as you like.
# 
# Python does not require an else block at the end of an `if`-`elif` chain. Sometimes an else block is useful; sometimes it is clearer to use an additional `elif` statement that catches the specific condition of interest.
# 
# The `else` block is a catchall statement. It matches any condition that was not matched by a specific if or `elif` test, and that can sometimes include invalid or even malicious data. If you have a specific  nal condition you are testing for, consider using a  final `elif` block and omit the else block. As a result, you will gain extra confidence that your code will run only under the correct conditions.

# In[ ]:


year = 1871

if year == 1851:
    message = 'First print.'
elif year == 1855:
    message = 'Second print.'
elif year == 1863:
    message = 'Third print.'
elif year == 1871:
    message = 'Fourth print.'
else:
    message = 'Hmm, I do not know this year...'
    
print(message)


# ## Testing Multiple Conditions
# 
# The `if`-`elif`-`else` chain is powerful, but it is only appropriate to use when you just need one test to pass. As soon as Python finds one test that passes, it skips the rest of the tests. This behavior is beneficial, because it is efficient and allows you to test for one specific condition.
# 
# However, sometimes it is important to check all of the conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks. This technique makes sense when more than one condition could be `True`, and you want to act on every condition that is `True`.
# 

# In[ ]:


authors = ['Herman Melville', 'Arthur Conan Doyle'] # , 'Mark Twain']

books_a = ['Moby Dick; Or, The Whale', 'The Apple-Tree Table and Other Sketches', 
           'Bartleby, the Scrivener: A Story of Wall-Street', 'The Piazza Tales',
           'The Confidence-Man: His Masquerade']

books_b = ['The Adventures of Sherlock Holmes', 'A Study in Scarlet', 
           'The Hound of the Baskervilles', 'The Sign of the Four',
           'The Return of Sherlock Holmes']
           
books_c = ['Adventures of Huckleberry Finn', 'The Adventures of Tom Sawyer',
           'The Mysterious Stranger, and Other Stories', 
           'A Connecticut Yankee in King Arthur\'s Court', 'The Innocents Abroad']
         
library = []
         
if 'Herman Melville' in authors: 
    library += books_a
if 'Arthur Conan Doyle' in authors:
    library += books_b           
if 'Mark Twain' in authors: 
    library += books_c

print('Your library contains:')
print(library)


# ## Checking that a List is not Empty
# 
# Since lists are "truthy" values they can be used as boolean expressions. That is,
# 
# ```python
# library = []
# 
# if library:
#     pass
# ```
# 
# is equivalent to:
# 
# ```python
# if library != []:
#     pass
# ```
# 
# However, the former is more pythonic.

# In[ ]:


library = []

if library:
    print('List is not empty.')
else:
    print('List is empty.')


# # Exercises!!!
# 
# ![image](http://i.imgur.com/kvUU7.gif)
# 
# 
#   1. Extend your program from the exercises in `05-Loops.ipynb` to not only produce correct but also well-formed sentences. That is, the sentence `A insect fly.` is not well-formed but `An insect flies.` is. To do so, use of conditional statements for your modification.

# In[5]:


# https://www.espressoenglish.net/100-common-adjectives-in-english/ 
adjectives = ["other", "new", "good", "high", "old", "great", "big", "American",
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

# len(adj) * len(articles) * len(nouns) * len(verbs)
sentences = []
for article in articles:
    for adjective in adjectives:
        for noun in nouns:
            for verb in verbs:
                sentences.append((' '.join([article, adjective, noun, verb])))
                
print(len(sentences))

