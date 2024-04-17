import random
entrances = [0]
exits = [3]
path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

def solution(entrances, exits, path):
	path = make_net(entrances, exits, path)
	max_flow = ford_fulkerson(path)
	return max_flow

	

def make_net(entrances, exits, path):
	#add super source/sink
	for p in path:
		p.append(0)
		p.append(0)

	super_src = [0 for i in range(len(path[0]))]
	super_snk = [0 for i in range(len(path[0]))]

	path.append(super_src)
	path.append(super_snk)
	for i in entrances:
		path[-2][i] = float('inf')

	for i in exits:
		path[i][-1] = float('inf')


	return path

def bfs(residual):
	#start is always second last node in matrix
	#end is always last node in matrix
	active_queue = []
	start = len(residual) - 2
	end = len(residual) - 1
	active_queue.append([start])
	while active_queue:
		path = active_queue.pop(0)
		neigh = neighbours(residual, path[-1])
		for n in neigh:
			if n == end:
				path.append(n)
				return path
			if n not in path:
				path.append(n)
			else:
				continue
			active_queue.append([i for i in path])
			del path[-1]
	return False

def neighbours(residual, n):
	neigh = []
	for i in range(len(residual[n])):
		if residual[n][i] > 0:
			neigh.append(i)
	return neigh

def make_residual(flow, capacties):
	residual = []
	for i in range(len(flow)):
		x = []
		for j in range(len(flow[i])):
			x.append(0)
		residual.append(x)

	for i in range(len(flow)):
		for j in range(len(flow[i])):
			if flow[i][j] <= capacties[i][j]:
				residual[i][j] = capacties[i][j] - flow[i][j]
			if flow[i][j] > 0:
				residual[j][i] = flow[i][j]

	return residual

def ford_fulkerson(capacties):
	flow = []
	for p in capacties:
		flow.append([0 for i in range(len(capacties))])
	while True:
		res = make_residual(flow, capacties)
		#find path in residual
		path = bfs(res)
		
		if path:
			b_neck = float('inf')
			for i in range(len(path) - 1):
				if capacties[path[i]][path[i+1]] > 0:
					new = res[path[i]][path[i+1]]
					if new < b_neck:
						b_neck = new

			for i in range(len(path) - 1):
				if capacties[path[i]][path[i+1]] > 0:
					flow[path[i]][path[i+1]] += b_neck
				else:
					flow[path[i]][path[i+1]] -= b_neck
		else:
			break
	

	return sum(flow[-2])

#print(solution(entrances, exits, path))
x = [[0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0]]


print(solution(entrances, exits, path))