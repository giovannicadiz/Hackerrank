i = input()
ni = set(input().split())

f = input()
nf = set(input().split())

print(len(ni.symmetric_difference(nf)))