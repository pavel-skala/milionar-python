"""
Module for writing results to txt
"""
class Results():
    """
    class to write result
    """
    def __init__(self, player_name,  money_won, elapsed_time, date, help_used):
        self.player_name = player_name
        self.money_won = money_won
        self.elapsed_time = elapsed_time
        self.date = date
        self.help_used = help_used
        self.write_to_file()

    def write_to_file(self):
        "method to write results"
        with open("results.txt", "a", encoding= "utf8") as file:
        # file = open('results.txt', 'a', encoding= "utf8")
            file.write(f"Nickname: {self.player_name}\n")
            file.write(f"Money won: {self.money_won:_}Kč\n".replace("_", " "))
            file.write(f"{self.player_name}`s time: {self.elapsed_time}s\n")
            file.write(f"Date: {self.date.strftime('%d.%m. %Y, %H:%M')}\n")
            file.write(f"{self.player_name} used help 50/50: {self.help_used}\n\n")
