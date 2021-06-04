import math
import csv

with open('data.csv',newline = '')as f :
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)

def mean(d):
    n = len(d)
    total = 0
    for i in d :
        total = total+int(i[0])
    mean = total/n
    return mean

square_list = []
for num in data:
 
    a = int(num[0])-mean(data)
    a = a**2
    square_list.append(a)
sum = 0

for i in square_list:
    sum = sum + i
    
print("sum", sum)
result = sum/(len(data)-1)
STDEV = math.sqrt(result)
print(float(STDEV))
