
# coding: utf-8

# # My First Python Program
# 
# As you learn speaking by continiously repeating what others say, as you learn writing by continiously rewriting chars, words and sentences that are presented to you, you can learn programming by typing, executing and modifying other people's programs.
# 
# This is what we will do now.
# 
# Type in the program that is handed out on paper in the field below. Copy exactly what is written on the paper. Note, that the intendation in the beginning of lines are created by pressing the tabulator (tab) key. On your keyboard this key looks something like: ⇥.
# 
# Tell the Python interpreter that you are done by hitting `CTRL+Return`.

# In[47]:


import re
import random
import eliza_language as lang


def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in lang.REFLECTIONS:
            tokens[i] = lang.REFLECTIONS[token]
    return ' '.join(tokens)


def analyze(statement):
    for pattern, responses in lang.PSYCHOBABBLE:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])


def talk_to_me():
    print("Wtf are you talking about!!?")

    while True:
        statement = input("> ")
        print(analyze(statement))
        if statement in "Stop!":
         print("Terminating...")   
         break


if __name__ == "__main__":
    talk_to_me()

# Describe what a computer is and what is its purpose
# Input og output

# What is a program?
# Et sæt af instruktioner, Det er noget som er gemt på computeren, Det er noget på computeren som er interativt. 

# What is the role of humans in relation to computers?
# Personer kan kommunikere med hinanden tæt og langt fra hinanden, Studerende kan studere og søge på information via en computer, Man kan bestille online, Virtuelle kontormøder er en mulighed.

# What is a programming language?
# Det er en formel eller sæt af instruktioner til computeren der giver forskellige outputs, Det kan blive brugt til at lave forskellige programmer der bruger en bestemt algoritme, Stort set hvert sprog har deres egen form for syntax


# Now, that you are done typing in the program, run the following code cell.

# In[ ]:


talk_to_me()


# # What is a computer program?

# # What is a computer?

# # Data Input
# 
# In Python you can get input from the user via the keyboard with the help if the `input` statement.

# # Data Output
# 
# 
# In Python you can display information to the user with the help if the `print` statement.

# # Data Processing
# 
# ## Assigning Input to a Variable
# 
# If you want to keep what user inputs to a program via the keyboard, you have to assign the return value of the input statement to a variable.

# ## Converting Input
# 
# A Python program treats all input that it receives from the keyboard as a string. That is, as a sequence of textual characters. Even when you give enter numbers, such as `1`, `2`, `3`, etc.
# 
# If you wanted to input numbers and treat them as numbers and not as strings, you have to tell your program to convert the data type of your input into an integer (`int`).

# # Write a small program... 
# 
# Write a small program that combines everything that you learned so far.
# 
#   * Get a number between 1 to 10 from the user, which is entered via the keyboard. 
#   * Make sure that the number is realy an integer.
#   * Use that number to repeat a string as many times as the number says.
#   
# For example:
# 
#   * The program asks: `How important is it on a scale from 1 to 10?`
#   * The user enters `8`
#   * The program returns: `It is really really really really really really really really important!`.

# # Assignment at home
# 
#   * Watch the video under: https://archive.org/details/ComputerAndTheMindOfManP3TheUniversalMachine
#     - Describe what a computer is and what is its purpose.
#     - What is a program?
#     - What is the role of humans in relation to computers?
#     - What is a programming language?
# 
#   * Modify your first ELIZA program, so that it starts the conversation with a different question than `Hello. How are you feeling today?`.
#   * Modify your first ELIZA program to exit when the user types: `Stop it! I have enough!`
#     - Hint: use an `if` condition in the very end of your program in the while loop. Encode a line that says _if statement equals `"Stop it! I have enough!"` then break out of the loop._ 
#   * Try to figure out where your ELIZA program gets the sentences from, which it prints when interacting with you.
# 
