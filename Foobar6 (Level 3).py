x = [[0, 0, 0, 0, 0, 0],
	 [1, 1, 1, 1, 1, 0],
	 [0, 0, 0, 0, 0, 0],
	 [0, 1, 1, 1, 1, 1],
	 [0, 1, 1, 1, 1, 1],
	 [0, 0, 0, 0, 0, 0]]

y = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	 [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
	 [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
	 [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	 [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
	 [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
	 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
	 [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
	 [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
	 [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]]

z = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

k = [[0, 0], 
	 [0, 0]]

def manhatten(start, end):
	return abs(start[0] - end[0]) + abs(start[1] - end[1])

def successors(map, node):
	c = node[0]
	coords = []
	coords.append((c[0] - 1, c[1]))
	coords.append((c[0] + 1, c[1]))
	coords.append((c[0], c[1] - 1))
	coords.append((c[0], c[1] + 1))
	i = 0
	while i < len(coords):
		if coords[i][0] >= len(map) or coords[i][1] >= len(map[0]) or coords[i][0] < 0 or coords[i][1] < 0 or map[coords[i][0]][coords[i][1]] == 1:
			del coords[i]
		else:
			i += 1
			
	return coords

def a_star(map):
	end = (len(map) - 1, len(map[0]) - 1)
	open_list = [((0, 0), manhatten((0, 0), end), 1)]
	closed_list = []

	while open_list:
		open_list.sort(key=lambda a:a[1]+a[2])
		node = open_list[0]
		del open_list[0]
		succ = successors(map, node)
		
		for s in succ:
			if s == end:
				return node[2] + 1

			cost = node[2] + 1
			m = manhatten(s, end)
			new_node = (s, m, cost)

			in_open = False
			in_closed = False

			
			for i in range(len(closed_list)):
				if new_node[0] == closed_list[i][0]:
					in_closed = True
					if new_node[1] + new_node[2] < closed_list[i][1] + closed_list[i][2]:
						open_list.append(new_node)
						del closed_list[i]
						break

			
			for i in range(len(open_list)):
				if new_node[0] == open_list[i][0]:
					in_open = True
					if new_node[1] + new_node[2] < open_list[i][1] + open_list[i][2]:
						open_list.append(new_node)
						del open_list[i]
						break

			if not in_open and not in_closed:
				open_list.append(new_node)
			
		closed_list.append(node)
	return len(map)*len(map[0])

def check_sides(map, c):
	if len(successors(map, (c, None, None))) > 1:
		return True
	return False

def solution(map):
	shortest_possible = manhatten((0, 0), (len(map) - 1, len(map[0]) - 1)) + 1
	walls = []
	for i in range(len(map)):
		for j in range(len(map[0])):
			if map[i][j] == 1:
				if check_sides(map, (i, j)):
					walls.append((i, j))

	shortest = a_star(map)
	if shortest == shortest_possible:
		return shortest

	for wall in walls:
		#print(wall)
		map[wall[0]][wall[1]] = 0
		path = a_star(map)
		if path < shortest:
			shortest = path
		map[wall[0]][wall[1]] = 1
		if shortest == shortest_possible:
			return shortest
	return shortest


print(solution(z))