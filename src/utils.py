import os
prefix = "[GTN] "
quest = {100: f"{prefix}Enter a number between 1-100: "}

def banner():
    os.system("clear")
    banner = open("./src/banner.txt","r")
    showbanner = banner.read()
    print(showbanner)
    banner.close()
