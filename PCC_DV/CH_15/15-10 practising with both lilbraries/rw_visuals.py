import matplotlib.pyplot as plt

from random_walk import RandomWalk
import plotly.express as px

# Keep makin gnew walks, as long as the program is actvive.

rw = RandomWalk(5_000)
rw.fill_walk()
print(rw.x_values)
print(rw.y_values)


# Visualize the results.
title = "Results of Rolling a D6 Dice and a D10  50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
df = rw
fig = px.scatter(rw.x_values, rw.y_values, title=title)
fig.show()

# Plot the point in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)
ax.set_aspect("equal")

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
           s=100)

# Remove axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
#plt.show()
