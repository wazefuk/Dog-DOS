import time
import random
import globalvar
import cmddef

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
        newpass = cmd[8:]
        if "cat" in newpass.lower():
            print("ERROR 0x00: CAT DETECTED")
            return "newpass-0x00"
        else:
            cmddef.addpass(newpass)
            print("Password added.")
            return "addpass"
    else:
        print("DOG DOES NOT UNDERSTAND")
        return None

start()

while True:
    command()