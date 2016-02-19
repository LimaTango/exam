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
std = np.std(new_array[1])
average = np.sum(new_array[1])/len(new_array[1])


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
    end_day = array[0][-1]
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
time_array = np.array([i*15.0 for i in range(n)])
time, val = time_control(3.0, 5.0)
unique_array = np.unique(new_array[1])
identity = float(len(unique_array))
total = float(len(new_array[1]))
hist_avg = total/identity
avg_list = [hist_avg, hist_avg]
time_list = [new_array[0][0], new_array[0][-1]]

if __name__ == "__main__":
    print "max value", max(new_array[1])
    print "min value", min(new_array[1])
    print "average", average
    print "standard deviation", std

    plt.figure(1)
    plt.plot(time, val)
    plt.title("heartbeat per second from minute 3-8")
    plt.xlabel("time")
    plt.ylabel("beats per second")

    plt.figure(2)
    hist_array = plt.hist(new_array[1], bins=100)
    plt.plot(time_list, avg_list)
    list(hist_array)
    str_max = "max:" + str(max(hist_array[0]))
    str_avg = "average:" + str(hist_avg)
    plt.annotate(str_max, xy=(650, 7500), xytext=(200, 7500),
            arrowprops=dict(facecolor='black'))
    plt.annotate('min:1', xy=(20, 20), xytext=(50, 550),
            arrowprops=dict(facecolor='black'))
    plt.annotate(str_avg, xy=(200, 600), xytext=(200, 1000),
            arrowprops=dict(facecolor='black'))
    plt.title("frequency of number of heartbeat")
    plt.xlabel("heartbeat per second")
    plt.ylabel("frequency")

    plt.figure(3)
    plt.plot(time_array, seg_avg)
    plt.title("function time heartbeat")
    plt.xlabel("time")
    plt.ylabel("average heartbeat")
    plt.show()



