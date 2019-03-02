from Dictionary import *
import random


class Question:
    my_dic = Dictionary()

    def __init__(self):
        print('init Question')
        self.my_dic.read_from_dictionary()

    def add_dic_to_question(self):
        print('add_dic_to_question')
        chose = random.randrange(1, 3)  # 한글 or 영어 문제 골라주는 변수

        en_words = self.my_dic.get_dictionary(2)  # Dictionary class에서 get_dictionary함수를 통해 en_list 빼오기
        kr_words = self.my_dic.get_dictionary(1)  # Dictionary class에서 get_dictionary함수를 통해 kr_list 빼오기
        if chose == 1:
            kr_ask = random.randint(0, kr_words.__len__() -1)  # 문제 낼 kr 단어 번호를 정하기
            kr_question = kr_words.pop(kr_ask)  # kr_words에서 pop으로 문제낼 단어를 빼와 kr_question에 저장
            print('[Q]', kr_question, '?')
            answer = input()
            en_answer = en_words.pop(kr_ask)
            test = en_answer.split(",")
            if test.__len__() > 1:
                print("1st :" + test[0] + "2nd: " + test[1])
            is_correct = False
            for i in test:
                if i == answer:
                    is_correct = True
                    break
            if is_correct:
                print('--> good student!!')
            else:
                print('--> study harder!!')

        else:
            en_ask = random.randint(0, en_words.__len__() -1)  # 문제 낼 en 단어 번호를 정하기
            en_question = en_words.pop(en_ask)  # en_words에서 pop으로 문제낼 단어를 빼와 en_question에 저장
            print('[Q]', en_question, '?')
            answer = input()
            kr_answer = kr_words.pop(en_ask)
            test = kr_answer.split(",")
            if test.__len__() > 1:
                print("1st :" + test[0] + "2nd: " + test[1])
            if test.__len__() > 1:
                print("1st :" + test[0] + "2nd: " + test[1])
            is_correct = False
            for i in test:
                if i == answer:
                    is_correct = True
                    break
            if is_correct:
                print('--> good student!!')
            else:
                print('--> study harder!!')
        return is_correct
