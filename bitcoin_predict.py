#coding=utf-8
import csv
from matplotlib import pyplot as plt
from datetime import datetime
import math, copy

filename1 = "cap.csv"
filename2 = "address.csv"
f = open(filename1)
reader = csv.reader(f)
header_row = next(reader)
# print(header_row)

cap = []
date = []
for row in reader:
    cap1 = float(row[1]) / 1000000000
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
# for row1 in reader1:
#     _address = 88 * (math.pow(float(row1[1])/10000, 2))
#     # 将地址的平方改为地址的根号次方，表现出了更强的相关性
#     # _address = 88 * (math.pow(float(row1[1])/10000, 2 ** 0.5))
#     # _date1 = datetime.strptime(row1[0], "%Y/%m/%d")
#     address.append(_address)
#     # date1.append(_date1)

# address.reverse()
# # date1.reverse()
# # print(address)

for row1 in reader1:
    _address = float(row1[1]) / 10000
    address.append(_address)

address.reverse()
# print(len(address))

address1 = copy.deepcopy(address)
for i in range(59,len(address)):
        
        address[i] = (sum(address1[i-59:i+1])) / 60

        address[i] = math.pow(address[i], 2 ** 0.5)
# print(address)
index = []
for i in range(0,len(cap)):
    if(cap[i] == 0 or address[i] == 0):
        index.append(0)
    else:
        index.append(100 * cap[i] / address[i])
# print(len(index))
# print(len(cap))
print(cap)
print(address)
print(index)
file = open('data.txt', 'w')
file.write(str(cap))
file.close()

fig = plt.figure(dpi=128, figsize=(5, 3))
# 总市值（蓝色）
plt.plot(date, cap, c='blue')
# 独立地址数（黑色）
plt.plot(date, address, c='black')
# 泡沫指数（红色）
plt.plot(date, index, c='red')
plt.title("Bitcoin Cap", fontsize=10)
plt.xlabel('', fontsize=8)
fig.autofmt_xdate()
plt.ylabel("Cap", fontsize=8)
plt.tick_params(axis='both', which='major', labelsize=6)
plt.show()
    


