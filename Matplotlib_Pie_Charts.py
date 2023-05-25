
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt -- Alternative
# from colorspacious import cspace_converter

plt.style.use('tableau-colorblind10')

# slices = [15, 35, 50]
# labels = ['Twenty', 'Thirty', 'Fifty']

slices = [42, 18, 26, 35, 10]
labels = ['A', 'B', 'C', 'D', 'E']

# colors = ['Orange', 'Brown', 'Grey']
colors = ['#146C94', '#F45050', '#FFD717','#867070', '#F97B22'  ] 
# Light Blue, Light Red, Light Yellow, Beige, Orange

explode =[0, 0, 0.06, 0, 0]

# plt.pie(slices)

plt.title('A Pie Chart Sample')


'''
# plt.pie(slices)
# plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'green'})
# plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'#867070'})
'''

'''
# plt.pie(slices, labels=labels,colors=colors, explode=explode, wedgeprops={'edgecolor':'#810CA8'}) #Edge Purple
# plt.pie(slices, labels=labels,colors=colors, explode=explode, shadow=True, 
#         wedgeprops={'edgecolor':'#810CA8'})

plt.pie(slices, labels=labels,colors=colors, explode=explode, shadow=True, autopct=' %1.1f%%',
        wedgeprops={'edgecolor':'#810CA8'}, startangle=90)
'''

# plt.tight_layout()
# plt.show()

# Swap label and autopct text positions
# Use the labeldistance and pctdistance parameters to position the labels and autopct text respectively
plt.pie(slices, labels=labels,colors=colors, explode=explode, shadow=True, 
        wedgeprops={'edgecolor':'#810CA8', 'linewidth':1.5}, startangle=-56, autopct=' %1.1f%%', pctdistance=1.20, labeldistance=.6)
plt.tight_layout()
plt.show()


'''Use help to show how to use the parameters'''
help(plt.pie)

# Color Hex
# Light Blue #146C94
# Light Red #F45050
# Light Orange #F97B22
# Light Yellow #F7D060
# Light Yellow #FFD717
# Light Green #1B9C85
# Light Green #A7D129
# Mint Green #C6DE41
# Light Beige #867070

# Dark Brown #483434
# Violet/Purple #810CA8
# Dark Grey #404258
# Medium Red #DA0037