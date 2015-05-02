"""Challenge #212 Animal Guess game"""
import sys
import os
import json

ANIMALSRC = "animals.txt"
QUESTIONSRC = "questions.txt"


class Animal(object):

    def __init__(self, name, animal_has={}, animal_is={}):
        """docstring for __init__"""
        super(Animal, self).__init__()
        self.a_name = name
        self.a_has = animal_has  # animal has
        self.a_is = animal_is  # animal is

    def add_has(self, key, value=True):
        self.a_has.update({key: value})

    def add_is(self, key, value=True):
        self.a_is.update({key: value})

    def get(self):
        data = {"has": self.a_has, "is": self.a_is}
        return {self.a_name: data}


class Game(object):

    def __init__(self):
        """initialize Game"""
        super(Game, self).__init__()
        self.state = None
        self.current = {}
        self.questions = self.load_questions()
        self.animals = self.load_animals()

    def load_questions(self):
        try:
            with open(QUESTIONSRC, "r") as data_file:
                return json.load(data_file)
        except:
            print "Cannot open json file {}".format(QUESTIONSRC)
            return {"has": [], "is": []}

    def load_animals(self):
        try:
            with open(ANIMALSRC, "r") as data_file:
                return json.load(data_file)
        except:
            print "Cannot open json file {}".format(ANIMALSRC)
            return []

    def add_question(self, key, question):
        assert key in ("has", "is")
        self.questions[key].append(question)
        with open(QUESTIONSRC, "w") as data_file:
            json.dump(
                self.questions,
                data_file,
                indent=4,
                sort_keys=True,
                separators=(',', ':'),
            )

    def add_animal(self, animal):
        self.animals.append(animal.get())
        with open(ANIMALSRC, "w") as data_file:
            json.dump(
                self.animals,
                data_file,
                indent=4,
                sort_keys=True,
                separators=(',', ':'),
            )
