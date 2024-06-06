# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random
import requests

class Game:
    def __init__(self) -> list:
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        word_grid = list(word)
        new_list = len([letter for letter in word_grid if letter not in list(self.grid)])
        #check = all(e in self.grid for e in word_grid)
        if word is None:
            return False
        elif word == "":
            return False
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        exists_dict = json_response['found']
        if new_list == 0 and exists_dict == True:
            return True
        else:
            return False
