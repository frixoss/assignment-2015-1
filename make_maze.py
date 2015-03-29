import sys
import random

n = int(sys.argv[1])
start_x = int(sys.argv[2])
start_y = int(sys.argv[3])
input_seed = sys.argv[4]
output_file = sys.argv[5]
random.seed(input_seed)

graph = {}

for i in range(0, n*n):
    neighbours = []
    if i==0 :
        neighbours.append(i+1)
        neighbours.append(i+n)
        graph[i] = random.sample(neighbours, len(neighbours))
    elif i==n-1:
        neighbours.append(i-1)
        neighbours.append(i+n)
        graph[i] = random.sample(neighbours, len(neighbours))
    elif i==(n-1)*n:
        neighbours.append(i+1)
        neighbours.append(i-n)
        graph[i] = random.sample(neighbours, len(neighbours))
    elif i==n*n-1 :
        neighbours.append(i-1)
        neighbours.append(i-n)
        graph[i] = random.sample(neighbours, len(neighbours))
    elif i<n:
        neighbours.append(i-1)
        neighbours.append(i+1)
        neighbours.append(i+n)
        graph[i] = random.sample(neighbours, len(neighbours))
    elif i%n==0: 
        neighbours.append(i-n)
        neighbours.append(i+n)
        neighbours.append(i+1)
        graph[i] = random.sample(neighbours, len(neighbours))
    elif (i+1)%n==0:
        neighbours.append(i-n)
        neighbours.append(i+n)
        neighbours.append(i-1)
        graph[i] = random.sample(neighbours, len(neighbours))
    elif i>(n*n)-n:
        neighbours.append(i-1)
        neighbours.append(i+1)
        neighbours.append(i-n)
        graph[i] = random.sample(neighbours, len(neighbours))
    else:
        neighbours.append(i-1)
        neighbours.append(i+1)
        neighbours.append(i+n)
        neighbours.append(i-n)
        graph[i] = random.sample(neighbours, len(neighbours))
   
start= start_x*n + start_y       

print (start)
def recursive_dfs(graph, start, path=[]):
  path.append(start)
  for node in graph[start]:    
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path


path=recursive_dfs(graph, start, path=[])
print(path)
def filec(path):
    file = open(output_file, "w")
    for i in range (0,n*n-1):
        x=path[i]/n
        y=path[i]%n
        x2=path[i+1]/n
        y2=path[i+1]%n
        file.write('(')
        file.write(str(x))
        file.write(',')
        file.write(str(y))
        file.write(')')
        file.write(', ')
        file.write('(')
        file.write(str(x2))
        file.write(',')
        file.write(str(y2))
        file.write(')')
        file.write('\n')
    file.close()
filec(path)
