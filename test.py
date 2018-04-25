import copy
a = [1, 2,5,8,6,8,9,7,4,2,3,5,6,4,2,3]
len = len(a)
# print(range(3,len))
# for i in range(3,len-1):
#     a[i] = (sum(a[i-3:i+1])) / 4
#     print(a[i])
# print(a)
# print(a[17])
b = copy.deepcopy(a)
print(b[12:16])
print (b)
for i in range(3, len):
    a[i] = (sum(b[i-3:i+1])) / 4
    # print (a[i])
print(a)
