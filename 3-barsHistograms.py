#%% [markdown]
# # 3 - Bars and histograms
# 
# Following the matplotlib tutorial by sentdex.
# 
# Link: https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

#%%

import matplotlib.pyplot as plt
import numpy as np


#%%
x, y = [2, 4, 6, 8, 10], [6, 2, 8, 5, 8]

plt.bar(x, y, label='Bars1')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Bars Graph 1')
plt.legend()
plt.show()


#%%
x, y = [2, 4, 6, 8, 10], [6, 2, 8, 5, 8]
x2, y2 = [1,3,5,7,9], [7,8,2,4,2]

plt.bar(x, y, label='Bars1', color='red')
plt.bar(x2, y2, label='Bars2', color='g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Merry Christmas!')
plt.legend()
plt.show()


#%%
# Population Utopiaville

pop_ages = abs(np.random.normal(45, 20, 142))
ids = [x for x in range(len(pop_ages))]
pop_ages


#%%
# Now we plot
plt.bar(ids, pop_ages)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Population Utopiaville')
plt.show()

#%% [markdown]
# This calls for a histogram

#%%
# Make bins

plt.bar(ids, pop_ages)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Population Utopiaville')
plt.show()


#%%
bins = [i for i in range(1, 150, 10)]

plt.hist(pop_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Population Utopiaville')
plt.show()


#%%



