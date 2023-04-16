from matplotlib import pyplot as plt
import numpy as np

# plt.style.use('tableau-colorblind10')
# plt.style.use('seaborn-v0_8-pastel')
# plt.style.use('seaborn-v0_8-dark')
# plt.style.use('fivethirtyeight')
plt.style.use('ggplot')


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

'''Basic Bar'''
# plt.bar(ages_x, dev_y, color='#002080', linestyle='-', linewidth=3, label='All Developer')
# plt.bar(ages_x, dev_y, color='orange', label='All Developer')

'''Bar and plot (line)'''
# plt.bar(ages_x, dev_y, color='orange', label='All Developer')
# plt.plot(ages_x, py_dev_y,color='red', label='Python Developer')
# plt.plot(ages_x, js_dev_y,color='blue', label='JavaScript Developer')

'''Below code will overlap each other'''
# plt.bar(ages_x, dev_y, color='orange', label='All Developer')
# plt.bar(ages_x, py_dev_y,color='red', label='Python Developer')
# plt.bar(ages_x, js_dev_y,color='blue', label='JavaScript Developer')

'''A workaround for the overlapping is to import numpy then grab a range of values for x-axis'''
x_index = np.arange(len(ages_x)) # An array of values number. Similar to list with index 

''' Shift with the exact width of the bar. Create a variable width to be explicit.
Rather than relying on the default value of 0.8 '''

bar_width = 0.28

# plt.bar(x_index - bar_width, dev_y, width=bar_width, color='orange', label='All Developer')
# plt.bar(x_index + bar_width, js_dev_y, width=bar_width, color='blue', label='JavaScript Developer')
# plt.bar(x_index, py_dev_y, width=bar_width,color='red', label='Python Developer')

plt.bar(x_index - bar_width, dev_y, width=bar_width, color='#424549', label='All Developer')
plt.bar(x_index + bar_width, js_dev_y, width=bar_width, color='#ffcf40', label='JavaScript Developer')
plt.bar(x_index, py_dev_y, width=bar_width, color='#189ad3', label='Python Developer')


# plt.style.use('classic') 

'''Label the title, x-axis and y-axis'''
plt.xticks(ticks=x_index, labels=ages_x) # - To show the label in age rather than the index

plt.xlabel('Age')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()

plt.show()