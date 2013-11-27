import math
last=None
helpfile=[
	"Type a standard Parenthetical statement and the calculator will tell you the answer.",
	"Type 'A' to use the last answer. Type % to find the remainder of a problem. Also use 'P' to represent Pi.\n",
	"Note that you should ALWAYS use multiplication signs (*) in between multiplying statements or it will result in an error.",
	"R converts a number into Radians, and D converts a number into Degrees.",
	"'AT', 'AS', and 'AC' represent Arc Tangent, Arc Sine, and Arc Cosine. 'T, 'S', and 'C' represent Tangent, Sine, and Cosine.",
	"'TH', 'SH', and 'Ch' represent Hyperbolic Tangent, Hyperbolic Sine, and Hyperbolic Cosine.",
	"'ATH', 'ASH', and 'ACH' represent Arc Hyperbolic Tangent, Arc Hyperbolic Sine, and Arc Hyperbolic Cosine.",
	"All of the previous methods require parenthesis after them to work properly, with the contributer inside.\n",
	"Type a lowercase letter to use that variable.",
	"    commands:",
	"        store",
	"            stores the last answer into a variable",
	"        vars",
	"            shows a list of current variables",
	"        help",
	"            displays this message",
	"        convert",
	"            converts numbers between bases, from base 1 to base 62"
]
variables={
	"a":0,
	"b":0,
	"c":0,
	"d":0,
	"e":0,
	"f":0,
	"g":0,
	"h":0,
	"i":0,
	"j":0,
	"k":0,
	"l":0,
	"m":0,
	"n":0,
	"o":0,
	"p":0,
	"q":0,
	"r":0,
	"s":0,
	"t":0,
	"u":0,
	"v":0,
	"w":0,
	"x":0,
	"y":0,
	"z":0
}
arr={}
chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
bases=len(chars)
for i in range(len(chars)):
    arr[chars[i-1]]=i-1

for v in helpfile:
	print v
while True:
	command=raw_input(">")
	if command=="store":
		if not last is None:
			print "    What variable would you like to store it to?"
			var=raw_input("    >")
			if len(var)==1:
				valid=False
				for v in variables.keys():
					if v==var:
						valid=True
				if valid:
					variables[var]=last
				else:
					print("    That variable is not found. Please use a single, lowercase letter variable.")
			else:
				print("    That variable is not found. Please use a single, lowercase letter variable.")
		else:
			print "    There is nothing to store."
	elif command=="vars":
		for i,v in variables.iteritems():
			print "    "+str(i)+" : "+str(v)
	elif command=="help":
		for v in helpfile:
			print "    "+v
	elif command=="convert":
		try:
			print "    What base is the number you would like to convert?"
			basefrom=raw_input("    >")
			print "    What base will it be converted to?"
			baseto=raw_input("    >")
			basefrom=int(basefrom)
			baseto=int(baseto)
			if baseto>0 and baseto<=bases:
				if basefrom>0 and basefrom<=bases:
					print "    What is the number?"
					number=raw_input("    >")
					number=number
					n=0
					if not basefrom==10:
					    for i in range(len(number)):
					        char=arr[number[i-1]]
					        l=len(number)
					        ex=basefrom**(l-i-1)
					        n=n+(char*ex)
					else:
					    n=int(number)	        
					s=""
					while n>0:
					    su=math.floor(n%baseto)
					    for i,v in arr.iteritems():
					        if v==su:
					            s=i+s
					    n=math.floor(n/baseto)
					print "        "+s
					if baseto==10:
						last=int(s)
		except:
			print "There was a problem."
			pass
	else:
		s=command.replace("^","**")
		for i,v in variables.iteritems():
			s=s.replace(i,str(v))
		s=s.replace("ASH","math.asinh")
		s=s.replace("ATH","math.atanh")
		s=s.replace("ACH","math.acosh")
		s=s.replace("AC","math.acos")
		s=s.replace("AS","math.asin")
		s=s.replace("AT","math.atan")
		s=s.replace("TH","math.tanh")
		s=s.replace("SH","math.sinh")
		s=s.replace("CH","math.cosh")
		if not last is None:
			s=s.replace("A",str(last))
		s=s.replace("P","math.pi")
		s=s.replace("T","math.tan")
		s=s.replace("C","math.cos")
		s=s.replace("S","math.sin")
		s=s.replace("R","math.radians")
		s=s.replace("D","math.degrees")
		s="print str("+s+")\nlast="+s
		try:
			exec s
		except:
			print "There was a problem."
			pass
		#exec s
