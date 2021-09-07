from src.constants import stock_dict
from src.message import message_dict


def place_order():
    amount_to_reduce_dict = {}
    for flower in stock_dict.keys():
        # this block checks the invalid entry and order over stock
        while 1:
            try:
                amount = int(input(f"{message_dict['amount']} {flower}: "))
                if amount > stock_dict[flower]:
                    raise Exception(f"{message_dict['shortage_error']} {stock_dict[flower]}")
            except Exception as e:
                print(e)
            else:
                amount_to_reduce_dict[flower] = amount
                break
    return amount_to_reduce_dict

