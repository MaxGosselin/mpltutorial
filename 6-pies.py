#%% [markdown]
# # 6 - Pies
# 
# Following the matplotlib tutorial by sentdex.
# 
# Link: https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

#%%
import matplotlib.pyplot as plt
import numpy as np


#%%
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'orange']

plt.pie(slices, labels=activities, colors=cols)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Pie 1')

plt.show()


#%%
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

# Straighten out the slice with startangle
plt.pie(slices, labels=activities, colors=cols, startangle=90)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Pie 2')

plt.show()


#%%
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'orange']

# Add some shadows and that cool blowout thing
plt.pie(slices, labels=activities, colors=cols, startangle=90,
        shadow=True, explode=(0,0.1,0.175,0))

plt.xlabel('x')
plt.ylabel('y')
plt.title('Pie 3')

plt.show()


#%%
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'olive']

# Add some pct labels to the slices
plt.pie(slices, labels=activities, colors=cols, startangle=90,
        shadow=True, explode=(0,0.1,0.175,0), autopct='%1.1f%%')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Pie 4')

plt.show()


#%%



