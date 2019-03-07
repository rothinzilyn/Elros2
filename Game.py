from Question import *


class Game:
    def __init__(self):
        print('initialize Game')

    def play(self):
        print('--- start game ---')
        my_quest = Question()

        chance = 3
        score = 0
        while chance > 0:
            if my_quest.add_dic_to_question():
                score = score + 1
            else:
                chance = chance - 1
            print('--- chance: ', chance, ', score: ', score, ' ---\n')

        print('--------------------')
        print('| FINAL SCORE : ', score, '|')
        print('--------------------')
