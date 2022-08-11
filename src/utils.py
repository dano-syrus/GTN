from progress.bar import Bar
import os, time, random

prefix = "[GTN] "
quest = { 100: f"{prefix}Enter a number between 1-100: ", 200: f"{prefix}Enter a number between 1-200: ", 300: f"{prefix}Enter a number between 1-300: ", 400: f"{prefix}Enter a number between 1-400: ", 500: f"{prefix}Enter a number between 1-500: "}

def init():
    with Bar(f"{prefix}Starting",max = 20) as bar:
        for i in range(20):
            time.sleep(0.15)
            bar.next()

    os.system("clear")
    banner = open("./src/banner.txt","r")
    showbanner = banner.read()
    print(showbanner)
    banner.close()

def random_quest():
    array = [100,200,300,400,500]
    var = random.randint(0, 4)
    return array[var]
