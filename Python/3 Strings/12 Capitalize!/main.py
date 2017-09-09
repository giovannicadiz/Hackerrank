def capitalize(string):
	return ' '.join((word.capitalize() for word in string.split(' ')))
	
if __name__ == '__main__':
	string = input()
	capitalize_string = capitalize(string)
	print(capitalize_string)