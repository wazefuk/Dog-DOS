import globalvar
import csv
import random

def help():
    with open("DogDOS\HelpMonolouge.txt", "r") as f:
        help_text = f.read()
    return help_text

def addpass(password):
    globalvar.passes.append(password)

def cat():
    with open("DogDOS\CatInsults.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"',)
        for x in csvreader:
            if random.randrange(1,10) == 1:
                return f"DOG FACT: {x[0]}\nCAT FACT: {x[1]}"
            else:
                continue
        else:
            return None