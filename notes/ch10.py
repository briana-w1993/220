from Die import  Die

def main():
    d = Die(6)
    d2 = Die(12)
    d.roll()
    d2.roll()
    print(d.get_value(), d2.get_value())



if __name__ == '__main__':
    main()

# hit enter to roll
# 3
# hit enter to roll
# 6
#
#