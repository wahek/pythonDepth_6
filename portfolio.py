def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    total = 0
    for key, value in stocks.items():
        total += value * prices[key]
    return total


def calculate_portfolio_return(current_value: float, initial_value: float) -> float:
    return round(current_value - initial_value, 2)


def get_most_profitable_stock_by_percent(stocks_init: dict, stocks_current: dict) -> tuple:
    max_prof = 0
    name = None
    for key, value in stocks_init.items():
        temp = (stocks_current[key] * 100 / value) - 100
        if temp > max_prof:
            max_prof = temp
            name = key
    return name, f'{round(max_prof, 2)}%'


def get_most_profitable_stock_by_total(stocks_init: dict, stocks_current: dict, stocks_value: dict) -> tuple:
    max_prof = 0
    name = None
    for key, value in stocks_value.items():
        temp = (stocks_current[key] - stocks_init[key]) * value
        if temp > max_prof:
            max_prof = temp
            name = key
    return name, round(max_prof, 2)
