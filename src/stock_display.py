def display(stock_details):
    print("flower name           quantity")
    for flower, quantity in stock_details.items():
        print(flower, (20-len(flower))*" ", quantity)



