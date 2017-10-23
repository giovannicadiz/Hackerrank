n = input()
a = set(input().split())
nc = int(input())

for _ in range(nc):

	command = input().split()
	command = command[0]
	elements = set(input().split())
	
	if command == 'intersection_update':
		a.intersection_update(elements)
	if command == 'update':
		a.update(elements)
	if command == 'symmetric_difference_update':
		a.symmetric_difference_update(elements)
	if command == 'difference_update':
		a.difference_update(elements)
		
print(sum(list(map(int,a))))

