"""
Problem 5.6: find max profit from buy and sell stocks
"""
from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    if not prices or len(prices) <= 1:
        return 0.0
    current_max_profit = 0.0
    current_min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < current_min_price:
            current_min_price = prices[i]
        else:
            current_max_profit = max(current_max_profit, prices[i] - current_min_price)
    return current_max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
