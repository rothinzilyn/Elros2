# coding=utf-8
import random


class Dictionary:
    en_list = []
    kr_list = []

    # __init__는 무조건 아래에 쓴 함수들을 실행시켜주는 class 의 기본 함수이다.
    def __init__(self):
        print ('initialize Dictionary')

    def set_dictionary(self):
        # dic.txt open in a
        dic_file = open("dic.txt", "a")
        print('Input (s) when you whant add new word in your dic. Else, input (n).')
        # 위의 질의에 대한 응답 저장 변수
        action_whether = input()
        if action_whether == 's':
            # dic.txt 에 넣을 단어 받기
            input_dic_en = input('영어 스펠링을 써주세요. 끝내고 싶으시면 q를 누르세요: ')
            input_dic_kr = input('한국어 뜻을 써주세요:')
            # dic.txt 에 "english word=korean word" 꼴로 넣기
            line = dic_file.write("\n" + input_dic_en + '=' + input_dic_kr)
        dic_file.close()

    # kr, en_list 를 바깥으로 빼주는 함수
    def get_dictionary(self, type):
        if type == 1:
            return self.kr_list
        else:
            return self.en_list

    def read_from_dictionary(self):
        # dic.txt open
        dic_file = open("dic.txt", "r")
        while 1:
            line = dic_file.readline()
            if not line:
                break
            # '=' 를 단어에서 빼기
            line_list = line.split('=')
            self.en_list.append(line_list[0])
            # enter 없애줌
            self.kr_list.append(line_list[1].strip("\n"))
        dic_file.close()
