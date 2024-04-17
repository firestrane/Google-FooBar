def get_xor(n):
	m = n % 4
	if m == 0:
		return n
	if m == 1:
		return 1
	if m == 2:
		return n + 1
	if m == 3:
		return 0


def solution(start, length):
	x = 0
	for i in range(length):
		x = x ^ (get_xor(start - 1) ^ get_xor(start + length - i - 1))
		start += length
	return x


print(solution(0, 20000000))