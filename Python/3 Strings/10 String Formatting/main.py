def print_formatted(number):	

	w = len("{0:b}".format(n))
	for i in range(1, n + 1):
		#print(i, oct(i), hex(i), bin(i))
		print("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width = w).upper())
	
if __name__ == '__main__':

	n = int(input())
	print_formatted(n)