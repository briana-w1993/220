"""
Name: Briana Addison
hw5.py

Problem: This program solves several problems using strings

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def name_reverse():
    first_last = input("Enter a name (first last):")
    user_first_last = first_last.split()
    print(user_first_last[1], ",", user_first_last[0])


def company_name():
    user_domain = input("Enter a domain:")
    domain = user_domain.split(".")
    print(domain[1])


def initials():
    num_student = eval(input("How many students are in the class?"))
    for i in range(num_student):
        student_name = input(("What is the name of student " + str(i + 1) +
                              "?"))
        student_init = student_name.split()
        first_init = student_init[0][0:1]
        last_init = student_init[1][0:1]
        print(first_init + last_init)


def names():
    name_list = input("Enter a list of names: ")
    name_init = name_list.split(", ")
    init_list = ""
    for i in name_init:
        name = i.split()

        first_init = name[0][0:1]
        last_init = name[1][0:1]
        init_list = init_list + first_init + last_init +" "
    print(init_list)


def thirds():
    num_sentence = eval(input("Enter the number of sentences: "))
    third_sentence = []
    for i in range(num_sentence):
        user_sentence = input(" enter sentence " + str(i +1) + ": ")
        for j in range(0,len(user_sentence),3):

            sentence = user_sentence [j ]
            third_sentence = sentence
            print(third_sentence, end="")



def word_average():
    sentence = input("Enter a sentence")
    sentence = sentence.split()
    sentence_length = len(sentence)
    for words in range(sentence_length):

        average = sentence_length + words
    print(average/sentence_length)



def pig_latin():
    sentence = input("enter a sentence to convert to pig latin: ")
    sentence = sentence.split()
    igay_atinlay = ""
    for word in sentence:
        first_letter = word[0]
        word = word[1:] + first_letter + "ay "
        igay_atinlay = igay_atinlay + word.lower()
    print(igay_atinlay)









if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
