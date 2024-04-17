import math

def factor(n):
	factors = []
	odd = (n%2)
	for i in range(1, math.ceil(math.sqrt(n)) + odd, pow(2,odd)):
		if not n%i:
			factors.append((i, int(n/i)))
			factors.append((int(n/i), i))
	return factors

def solution(s):
	l = len(s)
	factors = factor(l)

	sequences = []
	for fact in factors:
		seq_l = fact[0]
		slyce = s[:seq_l]
		is_seq = True
		for i in range(seq_l, l, seq_l):
			if not slyce == s[i:i+seq_l]:
				is_seq = False
				break
		if is_seq:
			sequences.append(fact)
	
	sequences.sort(key=lambda a:a[1], reverse=True)
	return sequences[0][1]

test = "abccbaabccba"
test_2 = "abcabcabcabc"

print(solution(test))
print(solution(test_2))

