# Day 5

## My Discount

'''
Create a function called my_discount. The function takes no arguments but asks the user to input the price and the discount (percentage) of the product. 
Once the user inputs the price and discount, it calculates the price after the discount. The function should return teh price after the discount. 
For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5. 
'''

def my_discount():
    price = input("Write the price of the product: ")
    price = float(price) if price.isdigit() else 0
    discount = input("Write the discount to apply: ")
    discount = float(discount) if discount.isdigit() else 0
    #coumpute discount 
    discount_on_price = (discount * price) / 100
    final_price = price - discount_on_price
    return final_price

print(f"The final price is: {my_discount()}")