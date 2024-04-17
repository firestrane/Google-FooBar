def euclid(a, b):
	u = a
	v = b
	n = 0
	while v > 0:
		r = u%v
		u = v
		v = r
		n+=1
	return u

def solution(M, F):
	m, f = int(M), int(F)
	if euclid(m, f) != 1:
		return 'impossible'
	n = 0
	while True:
		if (m == 1 and f == 1):
			break 
		if m > f:
			qr = divmod(m, f)
			if qr[1] == 0:
				m = 1
				n += qr[0] - 1
			else:
				m = qr[1]
				n += qr[0]
		else:
			qr = divmod(f, m)
			if qr[1] == 0:
				f = 1
				n += qr[0] - 1
			else:
				f = qr[1]
				n += qr[0]
		
	return str(n)


print(solution(2, 1))
