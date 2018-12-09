#%% [markdown]
# # 4 - Scatter Plots
# 
# Following the matplotlib tutorial by sentdex.
# 
# Link: https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

#%%

import matplotlib.pyplot as plt
import numpy as np


#%%
x, y = [1,2,3,4,5,6,7,8], [5,2,4,2,1,4,5,2]

plt.scatter(x, y, label='skitscat', color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter 1')

plt.show()


#%%
# We can change the marker too

plt.scatter(x, y, label='skitscat', color='k', marker='x')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter 1')
plt.legend()
plt.show()


#%%
# We can change the marker size too

plt.scatter(x, y, label='skitscat', color='k', marker='*', s=250)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter 1')
plt.legend()
plt.show()


