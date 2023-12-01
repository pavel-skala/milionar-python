import time
import math
from datetime import datetime
from game import play
from results import Results

from texts import get_texts
texts = get_texts()

while True:
    language = input("Pick language - cs/en: ")
    if language in ("cs", "en"):
        break

player_name = input(texts[language]["enter_nickname"])

date = datetime.now()

print()

print(texts[language]["enter_nickname"])

while True:
    start_time = time.time()
    money_won = play(language)
    end_time = time.time()
    elapsed_time = math.floor(end_time - start_time)
    Results(player_name, money_won, elapsed_time, date)

    print()
    print(texts[language]["play_again"])
    answer = input(texts[language]["yes_or_no"])
    if not answer in ("yes", "ano"):
        break
    print()
