#coding=utf-8
import csv
from matplotlib import pyplot as plt
from datetime import datetime
import math

filename1 = "cap.csv"
filename2 = "address.csv"
f = open(filename1)
reader = csv.reader(f)
header_row = next(reader)
# print(header_row)

cap = []
date = []
for row in reader:
    cap1 = int(float(row[1]) / 1000000000)
    _date = datetime.strptime(row[0], "%Y-%m-%d")
    cap.append(cap1)
    date.append(_date)

cap.reverse()
# print(cap)
date.reverse()
# print(date)

f1 = open(filename2)
reader1 = csv.reader(f1)
header_row1 = next(reader1)
# print(header_row)

address = []
# date1 = []
for row1 in reader1:
    _address = 88 * (math.pow(float(row1[1])/10000, 2))
    # _date1 = datetime.strptime(row1[0], "%Y/%m/%d")
    address.append(_address)
    # date1.append(_date1)

address.reverse()
# date1.reverse()
print(address)

fig = plt.figure(dpi=128, figsize=(5, 3))
plt.plot(date, cap, c='blue')
plt.plot(date, address, c='black')
plt.title("Bitcoin Cap", fontsize=10)
plt.xlabel('', fontsize=8)
fig.autofmt_xdate()
plt.ylabel("Cap", fontsize=8)
plt.tick_params(axis='both', which='major', labelsize=6)
plt.show()
    


