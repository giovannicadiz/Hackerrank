def swap_case(cadena):
	return cadena.swapcase()

if __name__ == '__main__':

	cadena = input().strip()
	result = swap_case(cadena)
	print(result)