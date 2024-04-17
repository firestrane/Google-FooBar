


def convert_base_10(s, b):
	n = 0
	for i in range(len(s)):
		n += int(s[i])*pow(b, len(s)-i-1)
	return n

def convert_base_b(n, b):
	r = 0
	while pow(b, r) < n:
		r += 1
	r -= 1
	s = ''
	a = n
	for i in range(r):
		qr = divmod(a, pow(b, r - i))
		s += str(qr[0])
		a = qr[1]
	s+=str(a)

	return s

def new_id(n, b):
	i = [int(c) for c in n]
	i.sort(reverse=True)
	x = ''.join([str(c) for c in i])
	i.sort()
	y = ''.join([str(c) for c in i])
	return convert_base_b((convert_base_10(x, b)) - convert_base_10(y, b), b)

def solution(n, b):
	seq = []
	z = new_id(n, b)
	print(z)
	

solution('210022', 3)