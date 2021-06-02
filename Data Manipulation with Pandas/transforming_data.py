import pandas as pd
homelessness = pd.read_csv('homelessness.csv')

# Inspecting DataFrame
print(homelessness.head())
print(homelessness.info())
print(homelessness.shape)
print(homelessness.describe())

# Part of DataFrame
print(homelessness.value)
print(homelessness.column)
print(homelessness.index)

# Sorting & subsetting
homelessness_ind = homelessness.sort_values('individual', ascending = True)
print(homelessness_ind.head()) #sorting column

homelessness_fam = homelessness.sort_values('family_members', ascending = False)
print(homelessness_fam.head())

homelessness_reg_fam = homelessness.sort_values(['region', 'family_members'], ascending = [True, False])
print(homelessness_reg_fam.head())

# Create dataframe individuals
individuals = homelessness[['individuals']]
print(individuals.head())

# Create dataframe contains state and family_members
state_fam = homelessness[['state', 'family_members']]
print(state_fam.head())

# Create dataframe contains individuals and state
ind_state = homelessness[['individuals', 'state']]
print(ind_state.head())

