def quad_seq(n, a, b, c):
	return int((a*pow(n,2)) + (b*n) + c)

def solution(x, y):
	return str(quad_seq(x+y, 0.5, -0.5, -y+1))

print(solution(5, 10))