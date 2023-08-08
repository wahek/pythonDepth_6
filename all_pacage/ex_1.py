import random
from sys import argv

__all__ = ['first_ex']


def first_ex(first: int = 0, second: int = 10, attempt: int = 3):
    number = random.randint(first, second)
    for _ in range(attempt):
        num = int(input('угадывай:\n'))
        if num != number:
            if num < number:
                print('бери больше')
            else:
                print('бери меньше')
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    arg = map(int, argv[1:])
    first_ex(*arg)
