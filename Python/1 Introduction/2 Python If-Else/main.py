if __name__ == '__main__':
	n = int(input())
	
	num = n % 2
	if n > 20:
		if num == 0:
			print("Not Weird")
		elif num == 1:
			print("Weird")
		
	elif num == 0:
		if (n >= 2) and (n <=5):
			print("Not Weird")
		elif (n >= 6) and (n <= 20):
			print("Weird")
		
	elif num == 1:
		print("Weird")	