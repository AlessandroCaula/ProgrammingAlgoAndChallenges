# Day 13

## Pay Your Tax

'''
Write a function called your_vat. The function takes no parameter. 
The function asks the user to input the price of an item and VAT (vat should be a percentage). The function should return the price of the item plus VAT. If the price is 220 and, VAT is 15% your code should return a vat inclusive price of 253. 
Make sure that your code can handle ValueError. Ensure the code runs until valid numbers are entered. (hint: Your code should include a while loop). 
'''

def your_vat():
    item_price = input("Item price: ")
    vat = input("VAT: ")
    try:
        price_increase = (float(item_price) * float(vat)) / 100
        print("Item price plus Vat: ", float(item_price) + price_increase)
    except ValueError:
        print("One of your input is not a valid value.")

your_vat()