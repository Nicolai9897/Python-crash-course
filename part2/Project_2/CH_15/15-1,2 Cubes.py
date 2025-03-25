import matplotlib.pyplot as plt

x_values = range(1,5000)
y_values = [num**3 for num in x_values]


plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


plt.xlabel("number")
plt.ylabel("numbers cubic value")

ax.axis([0, x_values[-1]*1.1, 0, y_values[-1]*1.1])
ax.ticklabel_format(style='plain')

plt.show()
