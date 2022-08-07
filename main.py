from progress.bar import Bar
from src import utils
import os, time, random

utils.banner()
score = 1

running = True
while running:
    try:
        random_number = random.randint(1, 100)
        user_input = int(input(utils.quest[100]))
        if user_input == random_number:
            print(f"{utils.prefix}You just won!")
            score += 1
            print(f"{utils.prefix}Score: {score}")
            with Bar(f"{utils.prefix}Loading", max = 20) as bar:
                for i in range(20):
                    time.sleep(0.15)
                    bar.next()
            os.system("clear")
        elif user_input == 0:
            break
        else:
            print(f"{utils.prefix}You lose! Number was {random_number}")
            if score >= 1:
                score -= 1
            else: 
                score = 0
            print(f"{utils.prefix}Score: {score}")
            with Bar(f"{utils.prefix}Restarting", max = 20) as bar:
                for i in range(20):
                    time.sleep(0.15)
                    bar.next()
    except:
        print(f"{utils.prefix}Something went wrong, try again!")
        running = False
