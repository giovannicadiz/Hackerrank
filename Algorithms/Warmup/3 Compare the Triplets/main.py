def solve(a0, a1, a2, b0, b1, b2):
	a = (1 if a0 > b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0)
	b = (1 if b0 > a0 else 0) + (1 if b1 > a1 else 0) + (1 if b2 > a2 else 0)
	print(a, b)
	
a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

result = solve(a0, a1, a2, b0, b1, b2)