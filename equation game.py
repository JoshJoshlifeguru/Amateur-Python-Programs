"""selects random math questions every level. and you lose and gain tokens depending
if you answer wrong or right"""

import random
questions = [ #the place where the questions are stored, in a advanced list. each unit has the correct answer by adding numbers together, and the question text asking what the question is
    (2 * 3, "What is 2 x 3?"), (4 * 4, "What is 4 x 4?"), (5 * 5, "What is 5 x 5?"),
    (10 * 12, "What is 10 x 12?"), (3 * 3, "What is 3 x 3?"), (3 * 4, "What is 3 x 4?"),
    (4 * 12, "What is 4 x 12?"), (50 * 3, "What is 50 x 3?"), (50 * 36, "What is 50 x 36?"),
    (60 / 15, "What is 60 ÷ 15?"), (30 / 5, "What is 30 ÷ 5?"), (40 / 10, "What is 40 ÷ 10?"),
    (60 / 3, "What is 60 ÷ 3?"), (70 / 7, "What is 70 ÷ 7?"), (56 / 7, "What is 56 ÷ 7?"),
    (49 / 7, "What is 49 ÷ 7?"), (42 / 6, "What is 42 ÷ 6?"), (36 / 6, "What is 36 ÷ 6?"),
    (35 / 5, "What is 35 ÷ 5?"), (75 / 25, "What is 75 ÷ 25?"), (80 / 20, "What is 80 ÷ 20?")
]
#The function responsible for the reward system of subtracting/adding tokens, as well as judging if answer is correct
def solve_equation(answers, correct_answers, tokens = 50): #parameters, for storing correct answers
    tokens_lost = 5 #the unit tokens are lost at a time
    tokens_won = 10 #the unit tokens are gained at a time
    win_definition = (f"congrats, you won {tokens_won} tokens!") #just the message of winning
    lose_definition = (f"wrong answer, you lost {tokens_lost} tokens :(") #likewise, but the message of losing
    for i in range(3):  # make this game play for each of the 3 questions selected at a time (complicated phat man!🥵)
        if answers[i] == correct_answers[i]:
            tokens += tokens_won #the main body of tokens has the ability to fluctuate according to what is won and lost
            print(f"{win_definition} You now have {tokens} tokens.🥳")
        else:
            tokens -= tokens_lost
            print(f"{lose_definition} You now have {tokens} tokens.👎")
    

    return tokens

tokens = 50  #while the previous block was responsible for saying you're right or wrong, this manages the main game function in selecting questions and making actual correct answers
while True: # keeps restarting the game but gives you a way out via exiting.
    print("\n--- New Round ---")

    selected_questions = random.sample(questions, 3) # Randomly select 3 unique math questions with the random module
    correct_answers = [q[0] for q in selected_questions]  # Extract correct answers. the 0 is part 1 of each question tuple,
    question_texts = [q[1] for q in selected_questions]  # Extract question text. the 1 is part two of each question tuple. which is the question text.🤓

    try:
        # Ask the user the three randomly chosen questions
        answers = []
        for i in range(3):
            user_input = input(f"{question_texts[i]} (or type 'exit' to quit): ")
            if user_input.lower() == "exit":
                print("Thanks for playing!")
                exit()
            answers.append(float(user_input))  # this makes the user input the answer. Convert answer to float to handle division results

        # Play a round (call the solve equation function)
        tokens = solve_equation(answers, correct_answers, tokens)

        # Check if tokens are gone
        if tokens <= 0:
            print("Game over💀 You ran out of tokens.")
            break

    except ValueError:
        print("Invalid input! Please enter a number or 'exit'.")


