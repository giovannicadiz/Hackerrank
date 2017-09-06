n = int(input().strip())
sL = 0
sR = 0
for i in range(n):
	matrix = input().split()
	sL += int(matrix[i])
	sR += int(matrix[-(i + 1)])
print(abs(sL - sR))	