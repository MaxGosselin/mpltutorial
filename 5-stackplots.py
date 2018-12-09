#%% [markdown]
# # 5 - Stack Plots
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

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','g'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack 1')

plt.show()


#%%
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# We can add a legend by ploting some empty sets
plt.plot([], [], color='m', label='sleeping', linewidth=4)
plt.plot([], [], color='c', label='eating', linewidth=4)
plt.plot([], [], color='r', label='working', linewidth=4)
plt.plot([], [], color='k', label='playing', linewidth=4)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','g'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack 2')
plt.legend()

plt.show()


#%%



