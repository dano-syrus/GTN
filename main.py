from progress.bar import Bar
from src import utils
import random, os, time

os.system("clear")
utils.banner()
score = 0
level = 1

while True:
    try:
        random_number = 97
        user_input = int(input("[GTN] Enter a number between 10-100: "))

        if user_input == random_number:
            level += 1
            print("[GTN] You just won!")
            score += 1
            print(f"[GTN] Score: {score}")
            with Bar(f"[GTN] Loading Level {level}", max = 20) as bar:
                for i in range(20):
                    time.sleep(0.20)
                    bar.next()
            os.system("clear")
        elif user_input == 0:
            break
        else:
            print("[GTN] You lose! Number was", random_number)
            score -= 1
            print(f"[GTN] Score: {score}")
            with Bar("[GTN] Restarting", max = 20) as bar:
                for i in range(20):
                    time.sleep(0.20)
                    bar.next()
    except:
        print("[GTN]: Something went wrong, try again! Type 0 to exit from the game.")
        os.system("exit")
