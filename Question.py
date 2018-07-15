import Dictionary
import random


class Question:
    def __init__(self):
        self.add_dic_to_question()

    def add_dic_to_question(self):
        chose = random.randrange(1, 3)  # 한글 or 영어 문제 골라주는 변수
        if chose == 1:
            kr_words = Dictionary.my_dictionary.get_dictionary(1)  # Dictionary class에서 get_dictionary함수를 통해 kr_list 빼오기
            kr_ask = random.randint(0, kr_words.__len__() -1)  # 문제 낼 kr 단어를 정하기
            print(kr_ask)
        else:
            en_words = Dictionary.my_dictionary.get_dictionary(2)  # Dictionary class에서 get_dictionary함수를 통해 en_list 빼오기
            en_ask = random.randint(0, en_words.__len__() -1)  # 문제 낼 en 단어를 정하기
            print(en_ask)


question_give = Question()  # Question class 의 객체
