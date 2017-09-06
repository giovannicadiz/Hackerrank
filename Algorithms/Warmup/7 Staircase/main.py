num = int(input().strip())
for i in range(1, num + 1):
    print (' ' * (num - i) + '#' * i)