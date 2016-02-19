_author__ = 'tai'

import sys
import numpy as np
from matplotlib import pyplot as plt
file_in = open(sys.argv[1])
data = []
valid_data = []
for line in file_in:
    row = [i for i in line.split()]
    data.append(row)
data.remove(data[0])
for row in data:
    new_row = [float(i) for i in row]
    if new_row[2] == 0:
        valid_data.append(new_row)
array = np.asarray(valid_data)
new_array = array.transpose()
average = sum/len(new_array[1])
std = np.std(new_array[1])
print "max value", max(new_array[1])
print "min value", min(new_array[1])
print "average", average
print "standard deviation", std

def time_control(start_time, duration):
    sub_time = []
    sub_val = []
    end_time = start_time + duration
    for index in range(len(new_array[0])):
        if start_time <= new_array[0][index] <= end_time:
            sub_time.append(new_array[0][index])
            sub_val.append(new_array[1][index])
    return sub_time, sub_val


def find_n(array):
    n = 0
    end_day  = array[0][-1]
    while n*15.0 < end_day:
        n += 1
    return n


def segment(num):
    array = []
    for i in range(num):
        start_time = i*15.0
        time, val = time_control(start_time, 15.0)
        avg = np.sum(val)/len(val)
        array.append(avg)
    return array
n = find_n(new_array)
seg_avg = segment(n)
new_avg = np.sum(seg_avg)/len(seg_avg)
time_array = [i for i in range(n)]
time, val = time_control(3.0, 5.0)
plt.plot(time, val)
plt.title("heartbeat per second")
plt.xlabel("time")
plt.ylabel("beats per second")
plt.show()

patch = plt.hist(new_array[1], bins=100)
plt.title("frequency of number of heartbeat")
plt.xlabel("heartbeat per second")
plt.ylabel("frequency")
plt.show()

plt.plot(time_array, seg_avg)
plt.title("heartbeat per second")
plt.xlabel("time")
plt.ylabel("beats per second")
plt.show()



