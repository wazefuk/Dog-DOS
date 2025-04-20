import globalvar

def help():
    with open("DogDOS\HelpMonolouge.txt", "r") as f:
        help_text = f.read()
    return help_text

def addpass(password):
    globalvar.passes.append(password)