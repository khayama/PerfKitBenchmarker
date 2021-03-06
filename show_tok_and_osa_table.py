import json
import sys
from sys import argv

file_path = sys.argv[1]
print file_path

result = []
for line in open(file_path, 'r'):
    result.append(json.loads(line))

#for i in range(len(result)):
#    print result[i]['metric']

avg=[]
for i in range(len(result)/9):
    avg.append(result[i*9+1])

for i in range(len(result)/9):
    avg.append(result[i*9+5])

#print avg

#for i in range(len(avg)):
#    print avg[i]['metric']

#for i in range(len(avg)):
#    print avg[i]['labels'][422:440] # sending_zone:aaa00
#    print avg[i]['labels'][344:364] # receiving_zone:aaa00

for i in range(len(avg)):
    sending_zone = avg[i]['labels'][435:440]
    receiving_zone = avg[i]['labels'][359:364]
    latency = avg[i]['value']
    print(str(i) + " : " + sending_zone + " --> " + receiving_zone + " : " + str(latency) + " ms")

zones = ['(ms)', 'tok02', 'tok04', 'tok05', 'osa21', 'osa22', 'osa23']
n = len(zones)-1
array = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            data = [x['value'] for x in avg if x['labels'][435:440] == zones[i+1] and x['labels'][359:364] == zones[j+1] ]
            array[i][j] = data[0]

from prettytable import PrettyTable 

table = PrettyTable(zones)
for i in range(len(array)):
    array[i].insert(0, zones[i+1])
    table.add_row(array[i])

print table
