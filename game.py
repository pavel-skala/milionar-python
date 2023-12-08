"""
Gameplay module
"""
import random
import time
import math
import questions
from texts import get_texts
texts = get_texts()

money = [1_000, 2_000, 3_000, 5_000, 10_000, 20_000, 40_000, 80_000, 160_000, 320_000, 640_000, 1_250_000, 2_500_000, 5_000_000, 10_000_000]


alphabet = ["a", "b", "c", "d"]
available_answer = ["yes", "ano", "no", "ne"]
help_answer = ["nápověda", "help"]
yes_answer = ["yes", "ano"]

def play(language):
    """
    play game function
    """
    available_alphabet_answer = ["a", "b", "c", "d", "nápověda", "help"]
    global texts
    help_used = "No"

    all_questions = questions.get_quetions(f'questions_{language}.json')
    for question_number, question in enumerate(all_questions):
        print(f"{texts[language]['question_for']} {money[question_number]:_}Kč".replace("_", " "))
        print()
        print(f"{question_number + 1}. {question['question']}")
        correct_answer = question["answers"][0]
        random.shuffle(question["answers"])

        correct_alphabet = ""

        for i in range(4):
            print(f"{alphabet[i]}) {question['answers'][i]}")
            if question["answers"][i] == correct_answer:
                correct_alphabet = alphabet[i]

        start_time = time.time()
        while True:
            answer = input(texts[language]["your_answer"])
            if answer in available_alphabet_answer:
                break

        end_time = time.time()
        elapsed_time = math.floor(end_time - start_time)

        if elapsed_time > 30:
            print(texts[language]["your_time_info"])
            return 0, help_used

        if answer in help_answer:
            available_alphabet_answer.remove("nápověda")
            available_alphabet_answer.remove("help")
            help_used = "Yes"

            print()
            print(texts[language]["help_picked"])
            correct_index = alphabet.index(correct_alphabet)
            while True:
                number = random.randint(0, 3)
                if correct_index != number:
                    break

            wrong_question = question["answers"][number]
            if correct_index > number:
                print(f"{alphabet[number]}) {wrong_question}")
                print(f"{correct_alphabet}) {correct_answer}")
            else:
                print(f"{correct_alphabet}) {correct_answer}")
                print(f"{alphabet[number]}) {wrong_question}")

            while True:
                answer = input(texts[language]["your_answer"])
                if answer in (correct_alphabet, alphabet[number]):
                    break

        if answer == correct_alphabet:
            print(f"{texts[language]['correct_answer']}")
            print(f"{texts[language]['you_have']}  {money[question_number]:_} Kč".replace("_", " "))

            print()

            if question_number < len(all_questions) - 1:

                print(texts[language]["continue"])
                while True:
                    answer = input(texts[language]["yes_or_no"])
                    if answer in available_answer:
                        break
                if not answer in yes_answer:
                    money_won = money[question_number]
                    print()
                    print(f"{texts[language]['win_info']} {money_won:_} Kč".replace("_", " "))
                    return money_won, help_used

            else:
                money_won = money[question_number]
                print(f"{texts[language]['win_info']} {money_won:_} Kč".replace("_", " "))
                return money_won, help_used

        else:
            print(texts[language]["wrong_answer"])
            print(f"{texts[language]['correct_answer_was']}: {correct_alphabet}) {correct_answer}")
            return 0, help_used

        print()
