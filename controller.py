from portfolio import calculate_portfolio_value, calculate_portfolio_return, get_most_profitable_stock_by_percent, \
    get_most_profitable_stock_by_total

_stocks_price_current = {'SBER': 264.18, 'LKOH': 6118.12, 'GAZP': 172.42, 'MGNT': 5633.50, 'SNGS_p': 49.50}
_stocks_value = {'SBER': 100, 'LKOH': 5, 'GAZP': 1, 'MGNT': 5, 'SNGS_p': 1000}
_stocks_price_buy = {'SBER': 141.20, 'LKOH': 4856.50, 'GAZP': 291.5, 'MGNT': 4200.5, 'SNGS_p': 35.5}


def menu():
    while True:
        print('1: Показать стоимость портфеля\n'
              '2: Показать доходность портфеля\n'
              '3: Показать самую доходную акцию в процентах\n'
              '4: Показать самую доходную акцию в рублях\n'
              '_: Выход\n')
        choice = input('Выбери пункт меню: ')
        match choice:
            case '1':
                _current_price = calculate_portfolio_value(stocks=_stocks_value, prices=_stocks_price_current)
                print(f'{_current_price} рублей')
            case '2':
                _difference = calculate_portfolio_return(
                    calculate_portfolio_value(stocks=_stocks_value, prices=_stocks_price_current),
                    calculate_portfolio_value(stocks=_stocks_value, prices=_stocks_price_buy))
                print(f'{_difference} рублей')
            case '3':
                _percent = get_most_profitable_stock_by_percent(_stocks_price_buy, _stocks_price_current)
                print(f'Доходность {_percent[0]} составила {_percent[1]}')
            case '4':
                _total = get_most_profitable_stock_by_total(_stocks_price_buy, _stocks_price_current, _stocks_value)
                print(f'Доходность {_total[0]} составила {_total[1]} рублей')
            case _:
                exit()
