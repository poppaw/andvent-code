def load_digits():
    with open("input1.txt") as f:
        return f.read().strip()


def sum_digits(digits):
    counter = 0
    for i in range (len(digits)-1):
        if digits[i-1] == digits[i]:
            counter +=int(digits[i])
    print (counter)


def sum_halfaway(digits):
    counter = 0
    step = int(len(digits)/2)
    for i in range (len(digits)-1):
        if digits[i-step] == digits[i]:
            counter +=int(digits[i])
    print (counter)

digits = load_digits()
sum_digits(digits)
sum_halfaway(digits)


