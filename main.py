from src.welcome import welcome
from src.order import place_order
from src.message import message_dict
from src.stock_manage import update_stock, check_stock


if __name__ == '__main__':
    while 1:
        welcome()
        amount_to_reduce_dict = place_order()
        update_stock(amount_to_reduce_dict)

        check_stock()
        if input(message_dict['response']).upper() != "Y":
            break
