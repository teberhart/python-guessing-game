import random

QUESTION_1 = "What is the biggest country in the world ? "
ANSWER_1 = "Russia"
Q1 = [QUESTION_1, ANSWER_1]

QUESTION_2 = "What is the most spoken language in the world ? "
ANSWER_2 = "Chinese"
Q2 = [QUESTION_2, ANSWER_2]

QUESTION_3 = "Paris is known as the city of ... ? "
ANSWER_3 = "Love"
Q3 = [QUESTION_3, ANSWER_3]

QUESTION_4 = "Bacon comes from what animal ? "
ANSWER_4 = "Pig"
Q4 = [QUESTION_4, ANSWER_4]

QUESTIONS = [Q1, Q2, Q3, Q4]

def main():
    correct = 0
    name = input("What's your name, player ? ")
    list = QUESTIONS[:]

    print(f"Hello {name} ! Welcome to our quiz game !")
    print(f"Today, for you, we have {len(list)} questions for you !")

    for i in range(len(list)):
        question = random.choice(list)
        answer = input(question[0])
        if answer.lower() == question[1].lower():
            print("Correct !")
            correct += 1
        else:
            print("Wrong !")
        list.remove(question)
    
    print(f"You had {correct} right answers, out of {len(QUESTIONS)} possible ones.")

main()