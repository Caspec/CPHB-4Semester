import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import webget
from collections import Counter

url = "https://raw.githubusercontent.com/Gozzah/Dataset/master/airline-safety/airline-safety.csv"
filename = "airline-safety.csv"
#webget.download(url)

# read csv
dd = pd.read_csv(filename)


#Question 1
def question1():
    c_incidents_85_99 = sum(dd['incidents_85_99'])
    print("incidents_85_99:")
    print(c_incidents_85_99)

#Question 2
def question2():
    c_fatalities_85_99 = sum(dd['fatalities_85_99'])
    print("fatalities_85_99:")
    print(c_fatalities_85_99)

#Question 3
def question3():
    c_incidents_00_14 = sum(dd['incidents_00_14'])
    print("incidents_00_14:")
    print(c_incidents_00_14)


#Question 4
def question4():
    c_fatalities_00_14 = sum(dd['fatalities_00_14'])
    print("fatalities_00_14:")
    print(c_fatalities_00_14)


#Question 5
def question5():
    inc_85_99 = sum(dd['incidents_85_99'])
    fat_85_99 = sum(dd['fatalities_85_99'])
    inc_00_14 = sum(dd['incidents_00_14'])
    fat_00_14 = sum(dd['fatalities_00_14'])
    value = [inc_85_99, fat_85_99, inc_00_14, fat_00_14]
    cat = ['incidents_85_99', 'fatalities_85_99', 'incidents_00_14','fatalities_00_14']
    index = np.arange(len(cat))
    plt.bar(index, value)
    plt.xticks(index, cat, fontsize=10, rotation=90)
    plt.title('Question 5: Airline Safety')
    plt.show()
    print("We can conclude that death and incidents decline overall (concorde planes and zeppelins)")
    

question1()
question2()
question3()
question4()
question5()

print('slug slug LARS ;-O')