n = int(input().strip())
sumL = 0
sumR = 0
for i in range(n):
	matrix = input().split()
	sumL += int(matrix[i])
	sumR += int(matrix[-(i + 1)])
print(abs(sumL - sumR))	