# coding=utf-8
import random
en_list = []
kr_list = []
true_word = []
false_word = []


class Dictionary:
    def read_from_dictionary(self, first, second):
        f = open("dic.txt", "r")
        #dic.txt open
        while 1:
            line = f.readline()
            if not line:
                break
            line_list = line.split('=')
            #'=' 단어에서 빼기
            en_list.append(line_list[0])
            kr_list.append(line_list[1].strip("\n"))
        f.close()

    def out_question(self, first, second):
        c = random.randint(0, 10)
        print(c)


my_dictionary = Dictionary()
my_dictionary.out_question(en_list, kr_list)


print("en_list: ", en_list)
print("kr_list: ", kr_list)


