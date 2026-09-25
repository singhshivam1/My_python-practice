def calculate_discount(price,discount):

    final_price = price + discount
    return final_price

amount = calculate_discount(100, 10)
print(f"Final price after discount: {amount}")