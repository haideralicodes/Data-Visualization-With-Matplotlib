import matplotlib.pyplot as plt

# The number of views a Youtube Channel got
views  = [534, 689, 258, 401, 724, 689, 350] 

# In last 7 days
days = range(1, 8)	#using the range function.This function creates a list whose starting value is from 1 to 7.(8 is excluded)..


# plt.plot(x, y)

plt.plot(days, views)	# passing the views and days list in plot() method
plt.show()