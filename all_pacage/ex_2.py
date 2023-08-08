import random

__all__ = ['riddle_', 'all_riddle']

DICT_RIDDLE = {"а какой": ['такой', 'нет, такой', 'а может такой', 'очевидно что такой'],
               'сколько': ['1', '2', '3', '4'],
               'зачем': ['за надом', 'за ненадом', 'прекрати этот бред']}


def riddle_(riddle: str, answer: list, attempt: int = 2):
    print(f'Загадка: {riddle}')
    print(f'Варианты ответа: {answer}')
    for _ in range(attempt):
        answer_console = input('Введи отгадку: ')
        if answer_console != answer[2]:
            print('Неверно')
        else:
            return answer_console == answer[2]
    return answer_console == answer[2]


def all_riddle(dict_riddle: dict, attempt: int = 1):
    _check_list = dict()
    for key, value in dict_riddle.items():
        print(key)
        print(value)
        for i in range(attempt):
            if value[1] != input('Введи отгадку: '):
                print('Неверно')
                _check_list[key] = 'Неверно'
            else:
                _check_list[key] = f'Верно, за {i + 1} попыток'
                break
    return _check_list


if __name__ == '__main__':
    # print(riddle_('а какой', ['такой', 'нет, такой', 'а может такой', 'очевидно что такой']))
    print(all_riddle(DICT_RIDDLE, 2))
