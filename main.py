import time
import random
import globalvar
import cmddef
import csv

def start():
    print("Welcome to Dog DOS!")
    time.sleep(3)
    print("THIS IS PROPERTY OF DOG")
    time.sleep(3)
    print("DO NOT BOOT WITHOUT AUTHORIZATION")
    time.sleep(3)
    password = input("INPUT PASSWORD TO CONTINUE: ")
    if password in globalvar.passes:
        if random.randrange(1,100) == 34:
            while True:
                print("ERROR! ERROR! KERNEL PANIC!")
        else:
            print("ACCESS GRANTED")
            return True
    elif "cat" in password.lower() and not password == "CatSUX293":
        print("NO")
        quit()
    else:
        print("ACCESS DENIED")
        time.sleep(3)
        quit()

def command():
    cmd = input("DogDOS> ")
    if cmd.lower() == "help":
        print(cmddef.help())
        return "help"
    elif cmd[:7].lower() == "addpass":
        if len(cmd) < 8:
            print("ERROR 0x01: NO PASSWORD GIVEN")
            return "newpass-0x01"
        else:
            newpass = cmd[8:]
        if "cat" in newpass.lower():
            print("ERROR 0x00: CAT DETECTED")
            return "newpass-0x00"
        else:
            cmddef.addpass(newpass)
            print("Password added.")
            return "addpass"
    elif cmd[:5].lower() == "bark ":
        parts = cmd[5:].split()
        if len(parts) > 1 and parts[0].lower() == "/e":
            text = " ".join(parts[1:])
            for i, char in enumerate(text.upper()):
                print(f"BARK{i}{char}")
            return "bark /e"
        else:
            print(cmd[5:].upper())
            return "bark"
    elif cmd.lower() == "cat":
        temp1 = cmddef.cat()
        if temp1 == None:
            while temp1 == None:
                temp1 = cmddef.cat()
            print(temp1)
        else:
            print(temp1)
            return "cat"
        return "empty"
    elif cmd.lower() == "treat":
        temp2 = random.randrange(1, 5)
        if temp2 == 1:
            print("🦴 DOG GOT ONE TREAT")
            return "treat"
        elif temp2 == 2:
            print("🦴🦴 DOG GOT TWO TREATS")
            return "treat"
        elif temp2 == 3:
            print("🦴🦴🦴 DOG GOT THREE TREATS!!!")
        elif temp2 == 4:
            print("🦴🦴🦴🦴 DOG GOT FOUR TREATS!!!")
            return "treat"
        elif temp2 == 5:
            print("🦴🦴🦴🦴🦴 DOG GOT FIVE TREATS!!!")
            return "treat"
    else:
        print("DOG DOES NOT UNDERSTAND")
        return None

start()

while True:
    command()