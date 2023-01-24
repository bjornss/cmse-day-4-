""""
To use this notebook for your in-class assignment, you will need these 
files, which you shoujld have downloaded:
* mhu.csv -- Lake Michigan and Lake Huron
* sup.csv -- Lake Superior
* eri.csv -- Lake Erie
* ont.csv -- Lake Ontario

As instructed in the in-class activity notebook for today, you are 
only expected to complete one PART below. Do not worry if your group 
is not big enough to finish all parts below, but if you have extra 
time, you're welcome to do so.
""""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


erie = pd.read_csv("eri.csv")
ont = pd.read_csv("ont.csv")
sup = pd.read_csv("sup.csv")
mhu = pd.read_csv('mhu.csv')

plt.figure(figsize=(20,8))
plt.suptitle('Plotting the Great Lakes')

# PART 1
# Using the Michigan/Huron Dataset, plot the Water Level, the second 
# column, as a function of time years

plt.subplot(3,3,1) # Generate the 1st subplot of a 3x3 set of plots
plt.plot(mhu['time'], mhu['lake average'], color = 'black', label = "Lake Michigan/Huron")
plt.xlabel('Year')
plt.ylabel('Water Level')
plt.title("Lake Michigan's Water Level Over Time")
plt.grid(color='grey', linestyle='-', linewidth=0.1)


# PART 2
# Using the Superior Dataset, plot the Water Level, the second column, 
# as a function of time years

plt.subplot(3,3,2) # Generate the 1st subplot of a 3x3 set of plots
plt.plot(sup['year'], sup['lake levels'], color = 'black', label = 'Lake Superior')
plt.xlabel('Year')
plt.ylabel('Water Level')
plt.title("Lake Superior's Water Level Over Time")
plt.grid(color='grey', linestyle='-', linewidth=0.1)

# PART 3
# Using the Erie Dataset, plot the Water Level, the second column, 
# as a function of time years

plt.subplot(3,3,3) # Generate the 1st subplot of a 3x3 set of plots
plt.plot(erie['time'], erie['water level'], color = 'black', label = 'Lake Erie')
plt.xlabel('Year')
plt.ylabel('Water Level')
plt.title("Lake Erie's Water Level Over Time")
plt.grid(color='grey', linestyle='-', linewidth=0.1)

# PART 4
# Using the Ontario Dataset, plot the Water Level, the second column, 
# as a function of time years

plt.subplot(3,3,4) # Generate the 1st subplot of a 3x3 set of plots
plt.plot(ont['year'], ont['Lake Ontario annual averages'], color = 'black', label = "Lake Ontario")
plt.xlabel('Year')
plt.ylabel('Water Level')
plt.title("Lake Ontario's Water Level Over Time")
plt.grid(color='grey', linestyle='-', linewidth=0.1)

# PART 5
# Using the Michigan/Huron and Superior Datasets, plot the 
# Michigan/Hurion Water Level vs Superior Water Level to see if there 
# is any correlation between the water levels.

plt.subplot(3,3,5) # Generate the 1st subplot of a 3x3 set of plots
plt.plot(mhu['time'], mhu['lake average'], color = 'green', label = "Lake Michigan/Huron")
plt.plot(sup['year'], sup['lake levels'], color = 'red', label = 'Lake Superior')
plt.xlabel('Year')
plt.ylabel('Water Level')
plt.title("Lake Michigan/Huron and Superior's Water Level Over Time")
plt.grid(color='grey', linestyle='-', linewidth=0.1)

# PART 6
# Using the Michigan/Hurion and Erie Datasets, plot the 
# Michigan/Huron Water Level vs Erie Water Level to see if there is 
# any correlation between the water levels.

plt.subplot(3,3,6) # Generate the 1st subplot of a 3x3 set of plots
plt.plot(mhu['time'], mhu['lake average'], color = 'green', label = "Lake Michigan/Huron")
plt.plot(erie['time'], erie['water level'], color = 'yellow', label = 'Lake Erie')
plt.xlabel('Year')
plt.ylabel('Water Level')
plt.title("Lake Michigan/Huron and Erie's Water Level Over Time")
plt.grid(color='grey', linestyle='-', linewidth=0.1)

# PART 7
#Using the Superior and Ontario Datasets, plot the Superior Water 
# Level vs Ontario Water Level to see if there is any correlation 
# between the water levels.

plt.subplot(3,3,7) # Generate the 1st subplot of a 3x3 set of plots
plt.plot(sup['year'], sup['lake levels'], color = 'red', label = 'Lake Superior')
plt.plot(ont['year'], ont['Lake Ontario annual averages'], color = 'blue', label = "Lake Ontario")
plt.xlabel('Year')
plt.ylabel('Water Level')
plt.title("Lake Michigan/Huron and Erie's Water Level Over Time")
plt.grid(color='grey', linestyle='-', linewidth=0.1)

plt.legend()
plt.tight_layout()


