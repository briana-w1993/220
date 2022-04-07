def average_sentinel():
    acc = 0
    count = 0
    num = 0
    while num >= 0:
        acc = acc + num
        count = count + 1
        num = eval(input("enter a number(enter a negative to stop) >> "))
    print("average: {}".format(acc / count))


def average_file():
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != '':
        nums_string = line.split(',')
        i = 0
    #     while i <
    #         acc = acc + eval(nums_string[i])
    #         count = count + 1
    #         i = i + 1
    #     line = file.readline()
    # print('average: {}'.format(acc / count))
