import pandas as pd

df = pd.read_csv('data.csv')
df.head()

x = df['x']
y = df ['y']

from matplotlib import pyplot as plt

import numpy as py 


# extract the x and y data from the DataFrame
x = df['x'].to_numpy()
y = df['y'].to_numpy()

# add a new dimension to the x and y arrays
x = x[:, None]
y = y[:, None]

# create a scatter plot of x vs y
plt.scatter(x, y)

# set the axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('X vs Y')

# show the plot
plt.show()
