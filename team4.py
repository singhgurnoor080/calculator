#JP #Taylor #Ceasar #Dane

def log10(x):
	temp = x
	count = 0
	while temp >= 10:
		temp = temp / 10
		count += 1
	return count
	
# def fib(n):
# 	a, b = 0,1
# 	wile b < n:
# 		print b,
# 		a, b = b, a+b
		
def fib(n):
	result = []
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a+b
	return result