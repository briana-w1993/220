# a * 0 = 0 | | a and False == False
# a * 1 = a || a and True == a
# a + 0 = a  || a or False == a
#
#

#
""""
x  -> and
+ -> or
0 -> false

Distributive Property
    a and (b or c) == (a and b) or (a and c)
    a or (b and c) == (a or b) and (a or c)

    De Morgan's Law
        not (a and b) == not a or not b
        not(a or b) == not a and not b




"""

def deMorgan_one(a, b):
    return not(a and b) == (not a or not b)



def deMorgan_test():
    tests = [ [True, True] , [True, False] , [False, True], [False, False] ]
    for test in tests:
        # test = [True, True]
        a = test[0]
        b = test[1]
        result = deMorgan_one(a,b)
        print('input: {}, output{}'.format(test, result))