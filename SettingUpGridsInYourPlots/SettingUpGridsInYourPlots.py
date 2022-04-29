import matplotlib.pyplot as plt

youtube_views =  [534, 689, 258, 401, 724, 689, 4045]
facebook_views = [123, 342, 700, 304, 405, 650, 6543]
twitter_views =  [202, 209, 176, 415, 824, 389, 3987]
days = range(1, 8)


plt.plot(days, youtube_views, label = 'Youtube Views', marker = 'o', markerfacecolor = 'b')
plt.plot(days, facebook_views, label = 'Facebook Views', marker = 'o', markerfacecolor = 'orange')
plt.plot(days, twitter_views, label = 'Twitter Views', marker = 'o', markerfacecolor = 'g')


plt.xlabel('Days')
plt.ylabel('Views')

plt.legend(loc = 'upper left')

plt.title('Daily Views for Marketting Channel')

plt.xlim(1, 5)	#this include the scale of graph from  1 to 5 on x axis
plt.ylim(100, 900)

plt.grid(True, linewidth = 3)	#the line width method is used to increaase the width of grids in the graph

plt.show()