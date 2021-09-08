from src.constants import STOCK_DICT
from src.message import message_dict


# takes order amount
def place_order():
    amount_to_reduce_dict = {}
    for flower in STOCK_DICT.keys():
        # this block checks the invalid entry and order over stock
        while 1:
            try:
                amount = int(input(f"{message_dict['amount']} {flower}: "))
                if amount > STOCK_DICT[flower]:
                    raise Exception(f"{message_dict['shortage_error']} {STOCK_DICT[flower]}")
            except Exception as e:
                print(e)
            else:
                amount_to_reduce_dict[flower] = amount
                break
    return amount_to_reduce_dict


# prints order details
def order_details(order_amount_dict):
    for flower, quantity in order_amount_dict.items():
        print(f"{flower}: {quantity}", end=" ")
    print("\n")
