# Summary statistics
import pandas as pd
import numpy as np

sales = pd.read_csv('sales.csv')

# Explore new Dataframe
print(sales.head())
print(sales.info())
print(sales['weekly_sales'].mean())
print(sales['weekly_sales'].median())

# Summarizing date
print(sales['date'].min())
print(sales['date'].max())

# Using .agg() method
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

print(sales['temperature_c'].agg(iqr))
print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))
print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg([iqr, np.median]))

# Cumulative statistics
sales_1_1 = pd.read_csv('sales_1_1')
sales_1_1 = sales_1_1.sort_values('date', ascending=True)
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()
print(sales_1_1[['date', 'weekly_sales', 'cum_weekly_sales', 'cum_max_sales']])

# Dropping duplicates
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())

store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates(subset='date')
print(holiday_dates['date'])

# Counting categorical variables
# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize = True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort = True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort= True, normalize= True)
print(dept_props_sorted)