import matplotlib.pyplot as plt

youtube_views = [534, 698, 401, 724, 689, 543, 545, 435, 423, 789, 905, 561, 621, 548]

days = range(1, 15)

# plt.plot(days, youtube_views, label = 'Youtube Views')

plt.scatter(days, youtube_views, label = 'Youtube Views')

plt.xlabel('Day')
plt.ylabel('Views')

plt.legend(loc = 'upper right')



plt.grid(True, linewidth = 1, linestyle = '-.')

plt.title('Marketting for youtube Videos')

plt.show()