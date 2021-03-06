# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(x = 'size', y = 'nb_sold_by_size', kind = 'bar', rot = 45)

# Show the plot
plt.show()

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x = 'date', y = 'nb_sold_by_date', kind = 'line')

# Show the plot
plt.show()

# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x = 'nb_sold', y = 'avg_price', kind = 'scatter', title = 'Number of avocados sold vs. average price')

# Show the plot
plt.show()

# Histogram of conventional avg_price 
avocados[avocados['type'] == 'conventional']['avg_price'].hist(alpha=0.5, bins=20)

# Histogram of organic avg_price
avocados[avocados['type'] == 'organic']['avg_price'].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(['conventional', 'organic'])

# Show the plot
plt.show()