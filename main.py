from src.welcome import welcome
from src.order import place_order, order_details
from src.message import message_dict
from src.stock_manage import update_stock, check_stock


if __name__ == '__main__':
    while 1:
        # prints the initial details
        welcome()
        # returns the amount to be reduced
        amount_to_reduce_dict = place_order()
        # updates the stock
        update_stock(amount_to_reduce_dict)
        # checks if the stocks are below threshold point(30) and calls add_stock method if needed to add stock
        check_stock()
        # prints success message
        print(f"\n{message_dict['success_order_details']}")
        order_details(amount_to_reduce_dict)

        if input(message_dict['response']).upper() != "Y":
            break
