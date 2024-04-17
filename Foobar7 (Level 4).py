import time
x = ([[0, 2, 2, 2, -1],  
 	[9, 0, 2, 2, -1],  
	[9, 3, 0, 2, -1],  
 	[9, 3, 2, 0, -1],  
	[9, 3, 2, 2,  0]], 1)

y = ([[0, 1, 1, 1, 1],  
 	[1, 0, 1, 1, 1],  
	[1, 1, 0, 1, 1],  
 	[1, 1, 1, 0, 1],  
	[1, 1, 1, 1,  0]], 3)

def successors(node, times):
	succ = []
	for i in range(len(times[node[0]])):
		succ.append((i, times[node[0]][i]))
	del succ[node[0]]
	return succ

def search(times, time_limit):

	end = len(times) - 1
	open_paths = [[(0, 0)]]
	closed_paths = []

	while open_paths:
		print(f'open: {open_paths}\nclosed: {closed_paths}')
		open_paths.sort(key=lambda a:a[-1][1])
		path = open_paths[0]
		del open_paths[0]
		node = path[-1]

		succ = successors(node, times)
		for s in succ:
			x = []
			new_node = (s[0], s[1] + node[1])

			x = [i for i in path]
			x.append(new_node)

			if x not in closed_paths:
				open_paths.append(x)

		i = 0
		while i < len(open_paths):
			if open_paths[i] in closed_paths:
				del open_paths[i]

			if open_paths[i][-1][0] == end:
				if open_paths[i][-1][1] <= time_limit:
					closed_paths.append(open_paths[i])
			i += 1
				
	

	return closed_paths





		


def solution(times, time_limit):
	search(times, time_limit)

print(search(y[0], y[1]))
