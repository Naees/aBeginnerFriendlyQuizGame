
ans = {
    "What is the rarest M&M color? ":"Brown", 
    "What is the common name for dried plums? ":"Prunes",
    "Which country consumes the most chocolate per capita? ":"Switzerland",
    "What is the name given to Indian food cooked over charcoal in a clay oven? ":"Tandoori",
    "What was the first soft drink in space? ":"Coca-cola",
    }

qns = [
    ["A. Red", "B. Green", "C. Blue", "D. Brown"], 
    ["A. Damsons", "B. Prunes", "C. Victoria", "D. Mirabelles"],
    ["A. United States", "B. Australia", "C. China", "D. Switzerland"],
    ["A. Tandoori", "B. Vindaloo", "C. Pakora", "D. Kofta"],
    ["A. Pepsi", "B. Coca-cola", "C. Sprite", "D. A&W"],
    ]

def new_game():
    guesses = []
    correct = 0
    wrong = 0
    counter = 1

    for key in ans:
        print("\n\n\n")
        print(f"Question {counter}.\n {key}")
        for options in qns[counter-1]:
            print(f"    {options}")
        playerinput = input("   Type out the answer: ").lower()
        # while True:
        #     playerinput = input("   Type out the answer: ").lower()
        #     from itertools import chain
        #     if playerinput.lower() in chain(*qns[counter]).lower():
        #         break
        guesses.append(playerinput.capitalize())

        correct += check_answer(ans.get(key),playerinput)
        counter += 1

    display_score(correct,wrong,guesses)
    #play_again()
    pass

def check_answer(answer, guess):
    if answer.lower() == guess.lower():
        print("You have gotten the RIGHT answer!")
        return 1
    else:
        print("You have gotten the WRONG answer!")
        return 0

def display_score(correctscore, wrongscore, guesseslist):
    print(f"\n\n\nCongratulations, you have completed the quiz!!\nHere are the results, lets go throught the answers first! \n")
    for y in ans:
        print(f"{y}\n Answer: {ans[y]}\n\n")
    print("\nNow lets look at your attempt!\n")
    for x in guesseslist:
        print(x)
    finalscore = int((correctscore/len(ans))*100)
    print(f"Your score is: {finalscore}%", end="")

def play_again():
    new_game()
    pass

new_game()


# format display score by showing the displays correctly
# new_game ??
# validation for user inputs making sure that users are not able to add inputs that are not in the options listed