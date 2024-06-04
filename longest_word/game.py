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

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found'] == json_response['found']

    def is_valid(self, word: str) -> bool:
        if word is None:
            return False
        if word == "":
            return False
        word_grid = list(word)

        check = all(e in self.grid for e in word_grid)
        return check
