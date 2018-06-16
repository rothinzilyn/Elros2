# coding=utf-8
import random
import dic.txt


class Dictionary:
    en_list = []
    kr_list = []

    def set_dictionary(self):
        print('Input (s) when you whant add new word in your dic. Else, input (n).')
        # 위의 질의에 대한 응답 저장 변수
        action_whether = input()
        if action_whether == 's':
            input_dic_en = input('영어 스펠링을 써주세요. 끝내고 싶으시면 q를 누르세요: ')
            input_dic_kr = input('한국어 뜻을 써주세요:')

    # kr, en_list 를 바깥으로 빼주는 함수
    def get_dictionary(self, type):
        if type == 1:
            return self.kr_list
        else:
            return self.en_list

    def read_from_dictionary(self):
        # dic.txt open
        dictionary = open("dic.txt", "r")
        while 1:
            line = dic.readline()
            if not line:
                break
                # '=' 단어에서 빼기
            line_list = line.split('=')
            self.en_list.append(line_list[0])
            # enter 없애줌
            self.kr_list.append(line_list[1].strip("\n"))
        dic.close()


my_dictionary = Dictionary()
my_dictionary.out_question()


print("kr_list: ", my_dictionary.get_dictionary(1))
print("en_list: ", my_dictionary.get_dictionary(2))


