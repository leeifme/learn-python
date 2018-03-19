from random import randint
from collections import deque
# import pickle

number = randint(0, 100)
history = deque([], 5)


def guess(k):
    if k == number:
        print('right')
        return True
    elif k > number:
        print('%d is greater-than Number' % k)
        return False
    elif k < number:
        print('%d is less-than Number' % k)
        return False


while True:
    # q = pickle.load(open('history'))
    n = input("Please input a number: ")
    if n == 'history' or n == 'h?':
        print(list(history))
    else:
        k = int(n)
        history.append(k)
        # pickle.dump(history, open('history', 'w'))
        if guess(k):
            break
