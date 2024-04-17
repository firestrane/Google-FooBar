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

z = ([[0, 1, 1, 1, 1, 1, 1],
	  [1, 0, 1, 1, 1, 1, 1],
	  [1, 1, 0, 1, 1, 1, 1],
	  [1, 1, 1, 0, 1, 1, 1],
	  [1, 1, 1, 1, 0, 1, 1],
	  [1, 1, 1, 1, 1, 0, 1],
	  [1, 1, 1, 1, 1, 1, 0]], 2)

d = ([[0, 1, 1], 
	  [1, 0, 1], 
	  [1, 1, 0]], 0)

def floyd_warshall(times):
	n = len(times)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if times[i][j] > times[i][k] + times[k][j]:
					times[i][j] = times[i][k] + times[k][j]
	return times

def negative_cycles(fw):
	for i in range(len(fw)):
		if fw[i][i] < 0:
			return True
	return False

def combinations(numbers, n=[], combs=[]):
	new_n = [x for x in n]
	for i in range(len(numbers)):
		nums = [x for x in numbers]
		del nums[i]
		new_n.append(numbers[i])
		combinations(nums, new_n, combs)
		combs.append([x for x in new_n])
		del new_n[-1]
	return combs

def check_path(p, fw):
	p.insert(0, 0)
	p.append(len(fw)-1)
	cost = 0
	for i in range(len(p)-1):
		cost += fw[p[i]][p[i+1]]
	return cost

def solution(times, time_limit):
	fw = floyd_warshall(times)
	if negative_cycles(fw):
		return [i-1 for i in range(1, len(fw)-1)]
	all_paths = combinations([i for i in range(1, len(fw) - 1)])
	all_paths.sort(reverse=True, key=len)
	for path in all_paths:
		if check_path(path, fw) <= time_limit:
			del path[0]
			del path[-1]
			path = [i-1 for i in path]
			path.sort()
			return path
	return []


print(solution(x[0], x[1]))