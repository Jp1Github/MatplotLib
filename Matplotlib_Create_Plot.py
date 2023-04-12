'''Matplot Creating Plot'''
from matplotlib import pyplot as plt

# Data
'''Age range of Developer'''
ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

'''Developer Salary'''
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

'''Python Developer Salary'''
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

'''JavaScript Developer Salary'''
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

'''Some basic plot. Using the default'''
# plt.plot(ages_x, dev_y, 'gD')  # plot axis x as ages_x and y as dev_y using green diamond markers
# plt.plot(ages_x, dev_y, 'o')   # plot axis x as ages_x and y as dev_y using default color circle markers
# plt.plot(ages_x, dev_y, label='All Developer')
# plt.plot(ages_x, py_dev_y, label='Python Developer')
# plt.plot(ages_x, js_dev_y, label='JavaScript Developer')
# plt.plot(ages_x, js_dev_y, label='JavaScript Developer')

'''Other example of line format pr from the Matplotlib website
'b'    # blue markers with default shape
'or'   # red circles
'-g'   # green solid line
'--'   # dashed line with default color
'^k:'  # black triangle_up markers connected by a dotted line'''


'''Preferred plot as this is more explicit. Longer code but preferred human readability and
will be easier for code maintenance'''
# plt.plot(ages_x, dev_y, color='#002080', linestyle='-', linewidth=3, marker='^', markersize=8, label='All Developer')
# plt.plot(ages_x, py_dev_y,color='red', linestyle='dashdot',linewidth=3, marker='2', markersize=8, label='Python Developer')
# plt.plot(ages_x, js_dev_y,color='grey', linestyle='dotted', linewidth=3, marker='H', markersize=8, linewidth='3', label='JavaScript Developer')

'''Available
color = b, g or blue, green or hex e.g #694873 (lavendar), #002080 (blue shade)
Using hex if want better color control or shade.
linestyle = solid, dashed, dashdot, dotted'''


'''Label the title, x-axis and y-axis'''
plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')


plt.legend()
'''If no label argument specified in plt.plot().
The plt.legend(args list1, list2). However should know the order
of the plot and could be error prone.'''
# plt.plot(age_x, dev_y)
# plt.plot(age_x, py_dev_y)
# plt.legend(['All Developer', 'Python'])

'''Putting padding'''
# plt.tight_layout()

'''Putting a grid'''
# plt.grid()

'''To save as a picture format. Below will save in the current
directory. Or can pass to a different directory'''
# plt.savefig('graph.jpeg')
# plt.savefig(r'C:\\Directory\graph.png')

'''To show the graph'''
plt.show()


'''Format Strings
A format string consist of a part for colorm marker and line.
fmt = '[maker][line][color]
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html'''

'''Plot styles'''
'''To check the available style'''
# print(plt.style.available)

'''To use the available style'''
# plt.style.use('seaborn-v0_8-darkgrid')
# plt.style.use('tableau-colorblind10')
# plt.style.use('fivethirtyeight')
# plt.style.use('seaborn-v0_8-colorblind')
# plt.style.use('seaborn-v0_8-pastel')
# plt.style.use('seaborn-v0_8-dark-palette')
# plt.style.use('seaborn-v0_8-dark')
# plt.style.use('ggplot')
# plt.style.use('classic')
# plt.style.use('seaborn-v0_8-notebook')
# plt.style.use('seaborn-v0_8-talk')
# plt.xkcd() -- Handwritten
'''When using the above remove the formatting in plt.plot()'''
