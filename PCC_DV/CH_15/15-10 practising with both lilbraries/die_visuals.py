import plotly.express as px
import pandas
import matplotlib.pyplot as plt

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for result in range(10000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [results.count(x) for x in poss_results]


# Visualize the results.
title = "Results of Rolling a D6 Dice and a D10  50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
plt.bar(poss_results, frequencies, color='maroon', width = 0.4)
plt.show()
#fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
#fig.write_html('dice_visual_d6d10.html')