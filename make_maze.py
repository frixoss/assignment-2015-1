import sys
import random

n = int(sys.argv[1])
start_x = int(sys.argv[2])
start_y = int(sys.argv[3])
seed = sys.argv[4]
output_file = sys.argv[5]

graph = {}

for i in range(0, n*n):
    neighbours = []
    if i==0 :
        neighbours.append(i+1)
        neighbours.append(i+n)
        graph[i] = neighbours
    elif i==n-1:
        neighbours.append(i-1)
        neighbours.append(i+n)
        graph[i] = neighbours
    elif i==(n-1)*n:
        neighbours.append(i+1)
        neighbours.append(i-n)
        graph[i] = neighbours
    elif i==n*n-1 :
        neighbours.append(i-1)
        neighbours.append(i-n)
        graph[i] = neighbours
    elif i<n:
        neighbours.append(i-1)
        neighbours.append(i+1)
        neighbours.append(i+n)
        graph[i] = neighbours
    elif i%n==0: 
        neighbours.append(i-n)
        neighbours.append(i+n)
        neighbours.append(i+1)
        graph[i] = neighbours
    elif (i+1)%n==0:
        neighbours.append(i-n)
        neighbours.append(i+n)
        neighbours.append(i-1)
        graph[i] = neighbours
    elif i>(n*n)-n:
        neighbours.append(i-1)
        neighbours.append(i+1)
        neighbours.append(i-n)
        graph[i] = neighbours
    else:
        neighbours.append(i-1)
        neighbours.append(i+1)
        neighbours.append(i+n)
        neighbours.append(i-n)
        graph[i] = neighbours
   
print(graph)


