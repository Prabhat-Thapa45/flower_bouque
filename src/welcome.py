from src.constants import STOCK_DICT
from src.message import message_dict
from src.stock_display import display


def welcome():
    # prints "Hello, Welcome To Flower Bouquet Store"
    print(message_dict['welcome'])
    # prints "Stock details are displayed below"
    print(message_dict['stock_details'])
    # displays stock details
    display(STOCK_DICT)
