
def sub_base(s1, s2, b):
	s = ''
	s1 = list(s1)
	for i in range(len(s1) - 1, -1, -1):
		r = int(s1[i]) - int(s2[i])
		if r < 0:
			r += b
			for j in range(i-1, -1, -1):
				if int(s1[j]) > 0:
					s1[j] = str(int(s1[j])-1)
					break
			for k in range(j+1, i):
				s1[k] = str(b-1)
		s = str(r) + s
	return s

def new_id(n, b):
	i = [int(c) for c in n]
	i.sort(reverse=True)
	x = ''.join([str(c) for c in i])
	i.sort()
	y = ''.join([str(c) for c in i])
	return sub_base(x, y, b)

def solution(n, b):
	seq = []
	z = new_id(n, b)
	while z not in seq:
		seq.append(z)
		z = new_id(z, b)
	return len(seq) - seq.index(z)
	

print(solution('210022', 3))