import math
arr={}
chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in range(len(chars)):
    arr[chars[i-1]]=i-1

class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def convert():
    try:
        basefrom=raw_input("From base:\n")
        basefrom=int(basefrom)
        if basefrom<len(chars) and basefrom>0:
            baseto=raw_input("To base:\n")
            baseto=int(baseto)
            if baseto<len(chars) and baseto>0:
                number=raw_input("Number:\n")
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
                print colors.GREEN+s+colors.ENDC
            else:
                print colors.WARNING+"Invalid base '"+str(baseto)+"' to convert into!"+colors.ENDC
        else:
            print colors.WARNING+"Invalid base '"+str(basefrom)+"' to convert from!"+colors.ENDC
    except:
        print colors.FAIL+"There was an error during conversion!"+colors.ENDC