from progress.bar import Bar
from src import utils
import random, os, time

utils.banner()
score = 0
difficulty = "easy"

def select_difficulty():
    global difficulty, random_number
    user_input = input("[GTN] Select Difficulty: ")
    if user_input.lower() == "easy":
        difficulty = "easy"
        random_number = random.randint(1, 100)
    elif user_input.lower() == "medium":
        difficulty = "medium"
        random_number = random.randint(1, 300)
    elif user_input.lower() == "hard":
        difficulty = "hard"
        random_number = random.randint(1, 500)

select_difficulty()
while True:
    try:
        user_input = int(input(utils.questions[difficulty]))
        if user_input == random_number:
            print("[GTN] You just won!")
            score += 1
            print(f"[GTN] Score: {score}")
            with Bar(f"[GTN] Loading", max = 20) as bar:
                for i in range(20):
                    time.sleep(0.20)
                    bar.next()
            os.system("clear")
        elif user_input == 0:
            break
        else:
            print(f"[GTN] You lose! Number was {random_number}")
            if score >= 1:
                score -= 1
            else: 
                score = 0
            print(f"[GTN] Score: {score}")
            with Bar("[GTN] Restarting", max = 20) as bar:
                for i in range(20):
                    time.sleep(0.20)
                    bar.next()
    except:
        print("[GTN]: Something went wrong, try again!")
        os.system("exit")
