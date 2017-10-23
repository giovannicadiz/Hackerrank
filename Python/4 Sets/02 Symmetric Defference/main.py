m=int(input()) 
a= set(int(x) for x in input().split()) 
n=int(input()) 
b=set(int(x) for x in input().split()) 
for i in sorted(a.difference(b).union(b.difference(a))): 
	print(i)