from src.constants import STOCK_DICT, ADD_STOCK_AMOUNT
from src.message import message_dict

# adds the stock if the flower is below the threshold amount
def add_stock(flower):
    STOCK_DICT[flower] += ADD_STOCK_AMOUNT


# updates the stocks after each order
def update_stock(amount_to_reduce_dict):
    for flower, quantity in amount_to_reduce_dict.items():
        STOCK_DICT[flower] -= quantity


# check stock and calls add_stock() method if stock is below threshold amount
def check_stock():
    for flower, quantity in STOCK_DICT.items():
        if STOCK_DICT[flower] <= 30:
            if input("{}".format(message_dict['add_stock'], flower)).upper() == "y":
                add_stock(flower)
