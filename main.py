"""
millionaire game
"""
import time
import math
from datetime import datetime
from game import play
from results import Results
from texts import get_texts

texts = get_texts()

available_language = ["cs", "en"]
available_answer = ["yes", "ano", "no", "ne"]
yes_answer = ["yes", "ano"]

while True:
    language = input("Pick language - cs/en: ")
    if language in available_language:
        break

print()
print(texts[language]["welcome"])
print()

player_name = input(texts[language]["enter_nickname"])

date = datetime.now()

print()

print(texts[language]["time_info"])
print(texts[language]["answer_info"])
print(texts[language]["help_info"])
print()
print(texts[language]["good_luck"])
print()

while True:
    start_time = time.time()
    money_won, help_used = play(language)
    end_time = time.time()
    elapsed_time = math.floor(end_time - start_time)
    Results(player_name, money_won, elapsed_time, date, help_used)

    print()
    print(texts[language]["play_again"])
    while True:
        answer = input(texts[language]["yes_or_no"])
        if answer in available_answer:
            break
    if not answer in yes_answer:
        break
    print()

print()
print(texts[language]["ending_text"])
