from progress.bar import Bar
from src import utils
import os, time, random

utils.init()
guesses = 0

while guesses < 5:
    try:
        random_quest = utils.random_quest()
        random_number = random.randint(1, random_quest)
        user_input = int(input(utils.quest[random_quest]))
        guesses += 1
        if user_input == random_number:
            print(f"{utils.prefix}You guessed the number in {str(guesses)}")
            with Bar(f"{utils.prefix}Restarting",max = 20) as bar:
                for i in range(20):
                    time.sleep(0.15)
                    bar.next()
            os.system("clear")
        if user_input == 0:
            break
        else:
            print(f"{utils.prefix}You didn't guess the number! Number was {str(random_number)}")
            with Bar(f"{utils.prefix}Loading",max = guesses) as bar:
                for i in range(guesses):
                    time.sleep(0.15)
                    bar.next()
    except:
        print(f"{utils.prefix}Something went wrong, try again!")

if guesses == 5:
    print(f"{utils.prefix}You're out of guesses! GAME OVER")
