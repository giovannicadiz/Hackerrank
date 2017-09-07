def timeConversion(s):
	
	night = 0
	if 'PM' in s:
		night = 12

	s = s[:8].split(':')

	if s[0] == '12':
		s[0] = 0

	s[0] = str(int(s[0]) + night)

	newtime = str()
	for x in s:
		newtime += x + ':'

	if len(newtime) < 9:
		newtime = '0' + newtime

	return(newtime[:8])

s = input().strip()
result = timeConversion(s)
print(result)

