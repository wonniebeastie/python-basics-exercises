# We are given the following list of energy sources.
# Write some code to remove 'fossil' from the list, then add 'geothermal' to 
# the end of the list. 

# Solution 1
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

del energy[0]
energy.append('geothermal')
print(energy) # ['solar', 'wind', 'tidal', 'fusion', 'geothermal']

# Solution 2
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy.pop(0)
energy.extend(['geothermal'])
print(energy) # ['solar', 'wind', 'tidal', 'fusion', 'geothermal']

# Solution 3
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy.remove('fossil')
energy.insert(4, 'geothermal')
print(energy) # ['solar', 'wind', 'tidal', 'fusion', 'geothermal']
