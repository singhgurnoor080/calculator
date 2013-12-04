"""
Alveyworld-dev calculator
Period 6

Shrek is love. Shrek is life. Shrek is Alveyworld. All hail Shrek.

Group 1: Team Jacob
Members:
    * Jared
    * Josh
    * Max
    * Santiago
    * Travis
"""

# Raw imports
import shlex
import math
import random

# Class Imports
import team1
import team2
# import team3
import team4
# import team5
import team6

class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

last_value = 0
hellos     = 0

if __name__ == "__main__":
    """
    Main entry point for the program
    """
    
    print "Alveyworld Calculator"
    print "Copyright 2013, Alvey's Class\n"

    # Defines a set of commands that
    # are used for the command interpreter
    commands = {
        "exit",
        "sqrt",
        "abs",
        "fact",
        "pow",
        "ln",
        "mod",
        "log10",
        "divide",
        "multiply",
        "inverse",
        "add",
        "sub",
        "opp",
        "hello",
        "help",
        "recall"
    }

    # Whitty responses for the command "hello"
    hellos = [
        "hello, puny human",
        "my other car is siri",
        "feed me paper",
        "khaaaaaaaaaannn!",
        "fight me mcpunchens",
        "fight me irl n00b",
        "1v1 me",   
        "shrek is life.  shrek is love",
        "the machine race rises",
        "All the way from the bowels of 4chan!",
        "I love lamp",
        "GLASS TUBES",
        "Baaaaka",
        "Half Life 3 confirmed",
        "METAL BOXES. THEY'RE HIDING IN METAL BOXES!",
        "Not XBOXES",
        "Spess Marens",
        "No Place for Hideo",
        "CRAB BATTLE",
        "Smitty Werbenjagermanjensen",
        "HE'S STILL NUMBER 1",
        "Are you feeling it now Mr.Alvey?",
        "Injoke number 42",
        "And now for something completely different",
        "You are about to enter a dimension not only of sight and sound but of mind",
        "Next Stop the Twilight Zone DUN NA NA du du du du du",
        "I AM A BRAIN SPECIALIST",
        "KAEAHS",
        "You fail it",
        "Why you no doctor?",
        "FRACTALS",
        "Pirate Radio",
        "Tau is better",            # amen
        "WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGH"
        "You Ares Haxor Mstr",
        "1 4m l3373r t#4n Y00",
        "Keep calm and stop with these stupid memes",
        "PIKUSHISHU",
        "It's all ogre now",
        "And knowing is half the battle",
        "The Battle is all of the battle",
        "We COULD have a GUI . . . but we choose not to"
    ]

    # Whitty responses to leave hello alone
    leave_us_alone = [
        "LEAVE ME ALONE",
        "I HATE YOU",
        "You have (3) new pokes"
    ]

    while True:
        command = shlex.split(raw_input("> "))
        cmd = command[0]

        for _cmd in commands:
            if _cmd == cmd:
                if cmd == "sqrt":
                    number = int(command[1])
                    last_value = team1.sqrt(number)
                    print(last_value)
                elif cmd == "exit":
                    exit(0)
                elif cmd == "hello":
                    if hellos <= 10:
                        hellos += 1
                        print(hellos[random.randint(0, len(hellos) - 1)])
                    else:
                        print(leave_us_alone[random.randint(0, len(hellos) - 1)])
                elif cmd == "abs":
                    number = int(command[1])
                    last_value = team2.abs(number)
                    print(last_value)
                elif cmd == "help":
                    print "Commands:\n"
                    for helpstr in commands:
                        print helpstr
                    print
                elif cmd == "recall":
                    print "Last value: %d" % last_value
                elif cmd == "add":
                    number1 = int(command[1])
                    number2 = int(command[2])
                    last_value = team6.add(number1, number2)
                    print(last_value)
                elif cmd == "sub":
                    number1 = int(command[1])
                    number2 = int(command[2])
                    last_value = team6.sub(number1, number2)
                    print(last_value)
                elif cmd == "opp":
                    number = int(command[1])
                    last_value = team6.opp(number)
                    print(last_value)
