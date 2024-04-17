import time
x = ([[0, 2, 2, 2, -1],  
 	[9, 0, 2, 2, -1],  
	[9, 3, 0, 2, -1],  
 	[9, 3, 2, 0, -1],  
	[9, 3, 2, 2,  0]], 12)

y = ([[0, 1, 1, 1, 1],  
 	[1, 0, 1, 1, 1],  
	[1, 1, 0, 1, 1],  
 	[1, 1, 1, 0, 1],  
	[1, 1, 1, 1,  0]], 0)

z = ([[0, -1, -1, -1, -1, -1, -1],
	  [-1, 0, -1, -1, -1, -1, -1],
	  [-1, -1, 0, -1, -1, -1, -1],
	  [-1, -1, -1, 0, -1, -1, -1],
	  [-1, -1, -1, -1, 0, -1, -1],
	  [-1, -1, -1, -1, -1, 0, -1],
	  [-1, -1, -1, -1, -1, -1, 0]], 5)

def successors(node, fw):
	succ = []
	for i in range(len(fw[node[0]])):
		succ.append((i, node[1] + fw[node[0]][i]))
	del succ[node[0]]
	return succ

def floyd_warshall(times):
	n = len(times)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if times[i][j] > times[i][k] + times[k][j]:
					times[i][j] = times[i][k] + times[k][j]
	return times

def check_full(l, length):
	return len(set([x[0] for x in l])) == length

def search(fw, time_limit):
	open_paths = [[(0, 0)]]
	closed_paths = []
	end = len(fw) - 1
	while open_paths:
		open_paths.sort(key=lambda a:a[-1][1])
		path = open_paths[0]
		del open_paths[0]

		node = path[-1]
		succ = successors(node, fw)

		for s in succ:
			x = [i for i in path]
			x.append(s)
			if s[1] + fw[s[0]][end] <= time_limit:
				open_paths.append(x)
				if s[0] == end:
					closed_paths.append(x)
					if check_full(x, len(fw)):
						return [x]

	return closed_paths	

def negative_cycles(fw):
	for i in range(len(fw)):
		if fw[i][i] < 0:
			return True
	return False

def solution(times, time_limit):
	fw = floyd_warshall(times)
	if negative_cycles(fw):
		return [i-1 for i in range(1, len(fw)-1)]
	paths = search(fw, time_limit)
	if not paths:
		return paths
	paths = [set(x[0] for x in z if x[0] > 0 and x[0] < len(fw)-1) for z in paths]
	paths = [list(k) for k in set([tuple(x) for x in paths if len(x) == len(max(paths, key=len))])]
	for p in paths:
		p.sort()
	paths.sort()
	return [x-1 for x in paths[0]]

print(solution(y[0], y[1]))