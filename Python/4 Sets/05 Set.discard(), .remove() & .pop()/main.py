n = int(input())
s = set(map(int, input().split()))
ran = int(input())

for _ in range(ran):
	x = input().split()


	if len(x) == 1:
		salida = s.pop()
	else:
		k = x[0]
		v = x[1]

		if k == 'remove':
			salida = s.remove(int(v))
			
		if k == 'discard':
			salida = s.discard(int(v))
		
print(sum(s))