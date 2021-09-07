from src.constants import stock_dict
from src.message import message_dict
from src.stock_display import display


def welcome():
    print(message_dict['welcome'])  # prints "Hello, Welcome To Flower Bouquet Store"
    print(message_dict['stock_details'])  # prints "Stock details are displayed below"
    display(stock_dict)  # displays stock details

