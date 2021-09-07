from src.constants import stock_dict, add_stock_amount
from src.order import place_order


def add_stock(flower):
    stock_dict[flower] += add_stock_amount


def update_stock(amount_to_reduce_dict):
    for flower, quantity in amount_to_reduce_dict.items():
        stock_dict[flower] -= quantity


def check_stock():
    for flower, quantity in stock_dict.items():
        if stock_dict[flower] <= 30:
            print(stock_dict[flower])
            add_stock(flower)
