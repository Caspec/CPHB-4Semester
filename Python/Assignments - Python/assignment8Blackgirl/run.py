import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import webget
import statistics
from collections import Counter

url = "https://github.com/mathiasjepsen/PythonDatasetAssignment/raw/master/ks-projects-201801.csv"
filename = "ks-projects-201801.csv"
#webget.download(url)

dd = pd.read_csv(filename)

suc = dd[dd.state == 'successful']

#Question 1
main_c = Counter(suc['main_category'])

tu = main_c.most_common(4)
cat_main = []
val_main = []
for el in tu:
    cat_main.append(el[0])
    val_main.append(el[1])
print('\n Question 1: What main-category of project has the highest success rate?')
print(cat_main)
print(val_main)

y_pos = np.arange(len(cat_main))

plt.bar(y_pos, val_main, align='center', alpha=0.5)
plt.xticks(y_pos, cat_main)
plt.title('Question 1')
#plt.axis([0, 4, 10000, 26000])
plt.show()

print('slug slug LARS ;-O')

print("\n")

#Question 2
#Makes a list named "cat" containing all the categories in our dataset, and counts how many times they occur
cat = Counter(suc['category'])
#makes a tuple containing the 4 most common categories and how often they occur
tu_cat = cat.most_common(4)
#makes two empty lists that will contain the category, and the value of our tuple
val_cat = []
cat = []
#Loops through the tuple and inserts the category in our "cat" list and its frequency in "val_cat" list.
for el in tu_cat:
    cat.append(el[0])
    val_cat.append(el[1])
print('\n Question 2: What is the category with the highest number of project proposals?')
print(cat)
print(val_cat)
#makes a variable that represents our y position in the bar diagram made below using numpy
y_pos_cat = np.arange(len(cat))

#makes and shows a bar diagram of the data
plt.bar(y_pos_cat, val_cat, align='center', alpha=0.5)
plt.xticks(y_pos_cat, cat)
plt.title('Question 2')
#plt.axis([0, 4, 10000, 26000])
plt.show()

print("\n")

#Question 3
#Makes a list "usd" that contains the usd pledged real column in our dataset sorted.
usd = sorted(suc['usd_pledged_real'])
print('\n Question 3: What is the median pledged amount (usd_pledged_real) of successfully funded projects?')
print(statistics.median(usd))

print("\n")

#Question 4
#counts the amount of items in our "usd" list that are above 5000
value = sum(i > 5000 for i in usd)
print('\n Question 4: What is the number of successfully funded projects with more than 5.000$ pledged (usd_pledged_real) per category?')
print(value)