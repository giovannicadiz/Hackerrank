def count_substring(string, sub_string):
    counter = 0
    sub_len = len(sub_string)
    for i in range(0, len(string)):
        if string[i] == sub_string[0]:
            if string[i:(i + sub_len)] == sub_string:
                counter = counter + 1
    return counter
	
if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()
	
	count = count_substring(string, sub_string)
	print(count)