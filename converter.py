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
        basefrom=raw_input(colors.BLUE+"From base:\n"+colors.ENDC)
        basefrom=int(basefrom)
        if basefrom<len(chars) and basefrom>0:
            try:
                baseto=raw_input(colors.BLUE+"To base:\n"+colors.ENDC)
                baseto=int(baseto)
                if baseto<len(chars) and baseto>0:
                    try:
                        number=raw_input(colors.BLUE+"Number:\n"+colors.ENDC)
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
                    except:
                        print colors.FAIL+"Unable to convert!\n"+colors.WARNING+"Make sure not to use characters of higher value than your base!"+colors.ENDC
                else:
                    print colors.WARNING+"Invalid base '"+str(baseto)+"' to convert into! Bases go from 1 to 62, nothing other than that!"+colors.ENDC
            except:
                print colors.FAIL+"Invalid base '"+str(baseto)+"' to convert into, use only decimal numbers!"+colors.ENDC
        else:
            print colors.WARNING+"Invalid base '"+str(basefrom)+"' to convert from! Bases go from 1 to 62, nothing other than that!"+colors.ENDC
    except:
        print colors.FAIL+"Invalid base '"+str(basefrom)+"' to convert from, use only decimal numbers!"+colors.ENDC