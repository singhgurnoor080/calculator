# Logan Hirschi, Jon Page, Coolidge B, Deydrien F, Josh S.

def pow(b, e):
	""" This function will raise the number b to the power e """
	total = 1
	for i in range(e):
		total = total * b
	return total
	
	
def ln(x):
	""" This function will give the natural log  """
	return 1