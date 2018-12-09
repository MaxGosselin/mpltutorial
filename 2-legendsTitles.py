#%% [markdown]
# # 2 - Legends titles and labels
# 
# Following the matplotlib tutorial by sentdex.
# 
# Link: https://www.youtube.com/watch?v=q7Bo_J8x_dw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

#%%
import matplotlib.pyplot as plt


#%%
# Simple plot with labels and titles
x = [1,2,3]
y = [5,7,4]

plt.plot(x,y)

plt.xlabel('Plot Number')
plt.ylabel('Important Variable')

#%% [markdown]
# You can also add a title.

#%%
plt.plot(x,y)

plt.xlabel('Plot Number')
plt.ylabel('Important Variable')

plt.title('Interesting Graph!\nCheck it out.')
plt.show()

#%% [markdown]
# You can also add a legend if you have multiple series to plot.

#%%
x2, y2 = [7, 2, 4], [7, 9, 2]

plt.plot(x, y, label='Series 1')
plt.plot(x2, y2, label='Series 2')

plt.xlabel('Plot Number')
plt.ylabel('Important Variable')
plt.title('Interesting Graph!\nCheck it out.')

plt.legend()
plt.show()


