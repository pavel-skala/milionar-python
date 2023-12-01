import random
import time
import math
import questions
from texts import get_texts
texts = get_texts()

money = [1_000, 2_000, 3_000, 5_000, 10_000, 20_000, 40_000, 80_000, 160_000, 320_000, 640_000, 1_250_000, 2_500_000, 5_000_000, 10_000_000]



def play(language):
    global texts

    all_questions = questions.get_quetions(f'questions_{language}.json')
    for question_number, question in enumerate(all_questions):
        print(f"{texts[language]['question_for']} {money[question_number]}Kč")
        print(question["question"])
        correct_answer = question["answers"][0]
        random.shuffle(question["answers"])

        alphabet = ["a", "b", "c", "d"]
        correct_alphabet = ""

        for i in range(4):
            print(f"{alphabet[i]}) {question['answers'][i]}")
            if question["answers"][i] == correct_answer:
                correct_alphabet = alphabet[i]

        start_time = time.time()
        while True:
            answer = input(texts[language]["your_answer"])
            if answer in("a" , "b" , "c" , "d"):
                break

        end_time = time.time()
        elapsed_time = math.floor(end_time - start_time)

        if elapsed_time > 30:
            print(texts[language]["your_time_info"])
            return 0

        if answer == correct_alphabet:
            print(f"{texts[language]['correct_answer']}")
            print(f"{texts[language]['you_have']}  {money[question_number]} Kč")

            print()

            if question_number < len(all_questions) - 1:

                answer = input(texts[language]["continue"])
                if not answer in ("yes", "ano"):
                    money_won = money[question_number]
                    print(f"{texts[language]['win_info']} {money_won} Kč")
                    return money_won

            else:
                money_won = money[question_number]
                print(f"{texts[language]['win_info']} {money_won} Kč")
                return money_won
        else:
            print(texts[language]["wrong_answer"])
            print(f"{texts[language]['correct_answer_was']}: {correct_answer}")
            return 0

        print()
