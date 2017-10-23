for _ in range(int(input())):

	a = int(input()); A = set(list(map(int, input().split())))
	b = int(input()); B = set(list(map(int, input().split())))
	
	if A < B:
		print(True)
	else:
		print(False)
	


