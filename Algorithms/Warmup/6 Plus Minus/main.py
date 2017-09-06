n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

neg = 0
pos = 0
zero = 0

for i in arr:
	if i < 0:
		neg += 1
	elif i > 0:
		pos += 1
	elif i == 0:
		zero += 1		
print("%.6f" % (pos/n))	
print("%.6f" % (neg/n))
print("%.6f" % (zero/n))	
