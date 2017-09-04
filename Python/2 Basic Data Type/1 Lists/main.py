if __name__ == '__main__':

	N = int(input())
	lista = []
	for x in range(N):
		s = input().split()
		cmd = s[0]
		args = s[1:]
		if cmd !="print":
			cmd += "("+ ",".join(args) +")"
			eval("lista."+cmd)
		else:
			print (lista)