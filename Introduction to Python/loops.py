# Initialize offset
offset = 8

# Code the while loop
while offset != 0 : 
    print('correcting...')
    offset = offset - 1
    print(offset)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else : 
      offset = offset + 1   
    print(offset)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for elements in areas :
    print(elements)

# Change for loop to use enumerate() and update print()
for index, elements in enumerate(areas) :
    print('"' + 'room' + str(index) + ':' + ' ' + str(elements) + '"')

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for a in house :
    print('the' + ' ' + a[0] + ' ' + 'is' + ' ' + str(a[1]) + ' ' + 'sqm')

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items() : 
    print('the capital of ' + str(key) + ' is ' + str(value))

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np.nditer(np_height) : 
    print(str(x) + ' inches')

# For loop over np_baseball
for y in np.nditer(np_baseball) : 
    print(y)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(str(lab) + ': ' + str(row['cars_per_cap']))

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()

# Print cars
print(cars)

# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)