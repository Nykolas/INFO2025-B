
x = 54278

def fun(n,ant):
	if n == 0:
		return True
	else:
		if ant == 0:
			if (n%2)==0:
				return False
			else:
				return fun(n//10,1)
		else:
			if (n%2)==0:
				return fun(n//10,0)
			else:
				return False

print(fun(x,1))