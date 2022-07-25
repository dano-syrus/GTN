import os

def banner():
    banner = open("./src/banner.txt","r")
    showbanner = banner.read()
    print(showbanner)
    banner.close()
