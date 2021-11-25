# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import string
import random
import requests


class Game():
    def __init__ (self):
        self.grid = list()
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if len(word) == 0:
            return False
        tempgrid = self.grid.copy()

        for letter in word:
            if letter not in tempgrid:
                return False
            tempgrid.pop(tempgrid.index(letter))
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
