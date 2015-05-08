"""Challenge #212 Animal Guess game

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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

    @classmethod
    def loadjs(cls, a_data):
        """Used for loading animal from dict"""
        cls.a_has = a_data.items()[0][1]["has"]
        cls.a_is = a_data.items()[0][1]["is"]
        cls.a_name = a_data.items()[0][0]
        return cls

    def add_has(self, key, value=True):
        self.a_has.update({key: value})

    def add_is(self, key, value=True):
        self.a_is.update({key: value})

    def get(self):
        data = {"has": self.a_has, "is": self.a_is}
        return {self.a_name: data}


class GuessAnimal(Animal):

    """Class for the animal that is guessed"""

    def __init__(self):
        super(GuessAnimal, self).__init__("Guess")
        self.state = False
        self.matches = {}

    def get_matches(self):
        with open(ANIMALSRC, "r") as data_file:
            data = json.load(data_file)
        print data
        matching = {}
        for animal in data:
            animal = Animal.loadjs(animal)
            # Elements matches
            has_match = dict(set(animal.a_has.items()) & set(self.a_has.items()))
            is_match = dict(set(animal.a_is.items()) & set(self.a_is.items()))
            matching[animal.a_name] = {"has": has_match, "is": is_match}
        return matching


class Game(object):

    def __init__(self):
        """initialize Game"""
        super(Game, self).__init__()
        self.filestate = [None,None]
        self.current = {}
        self.questions = self.load_questions()
        self.animals = self.load_animals()

    def load_questions(self):
        try:
            with open(QUESTIONSRC, "r") as data_file:
                self.filestate[0] == True
                return json.load(data_file)
        except:
            print "Cannot open json file {}".format(QUESTIONSRC)
            self.filestate[0] = False
            return {"has": {}, "is": {}}

    def load_animals(self):
        try:
            with open(ANIMALSRC, "r") as data_file:
                self.filestate[1] = True
                return json.load(data_file)
        except:
            print "Cannot open json file {}".format(ANIMALSRC)
            self.filestate[1] = False
            return []

    def add_question(self, key, question):
        assert key in ("has", "is")
        self.questions[key].append(question)
        if not self.filestate[0]:
            return
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
        if not self.filestate[1]:
            return
        with open(ANIMALSRC, "w") as data_file:
            json.dump(
                self.animals,
                data_file,
                indent=4,
                sort_keys=True,
                separators=(',', ':'),
            )

    def gameLoop(self):
        pass

if __name__ == "__main__":
    g = Game()
    dog = Animal("rat")
    print("dog name: {}".format(dog.a_name))
    print("dog has:\n{}".format(dog.a_has))
    print("dog is:\n{}".format(dog.a_is))
    g.add_animal(dog)
    cat = g.animals["cat"]
    print("cat name: {}".format(cat.a_has))
    guess = GuessAnimal() # Cat
    guess.add_has("tail")
    guess.add_has("paws")
    guess.add_is("curious")
    print("matches:\n{}".format(guess.get_matches))

