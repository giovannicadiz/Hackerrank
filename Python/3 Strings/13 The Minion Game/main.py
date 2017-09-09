def minion_game(string):

	stuart = 0
	kevin = 0

	for i in range(len(s)):
		if s[i] in ('AEIOU'):
			kevin += len(s) - i
		else:
			stuart += len(s) - i

	if kevin > stuart:
		print('Kevin', kevin) 
	elif kevin < stuart:
		print('Stuart', stuart) 
	else:
		print('Draw')
	
if __name__ == '__main__':
	s = input().upper()
	minion_game(s)







