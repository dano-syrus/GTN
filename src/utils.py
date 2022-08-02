import os
questions = { "easy":"[GTN] Enter a number between 1-100: ", "medium":"[GTN] Enter a number between 1-300: ", "hard":"[GTN] Enter a number between 1-500: " }

def banner():
    os.system("clear")
    banner = open("./src/banner.txt","r")
    showbanner = banner.read()
    print(showbanner)
    banner.close()
