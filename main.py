"""
Author: Meng Moua
Course: CSC500
Assignment: Module 8, Final Portfolio Project
"""
from ShoppingCart import ShoppingCart
from Item import Item
from datetime import datetime

def main():
    customerName = input("Enter customer's name:\n")
    todayDate = input("Enter today's date in the format of [January 31, 9999]:\n")

    while(not isValidDate(todayDate)):
        print('Entered date is not a valid date. Please try again:')
        todayDate = input()

    print('Customer name:', customerName.title())
    print("Today's date:", todayDate.capitalize())

    dateObject = datetime.strptime(todayDate, "%B %d, %Y").date()
    shoppingCart = ShoppingCart(customerName.title(), dateObject)

    while True:
        printMenu()
        userInput = input()

        if userInput == 'a':
            try:
                itemName = input('Item name:\n')
                itemPrice = float(input('Item price:\n'))
                itemQuantity = int(input('Item quantity:\n'))
                itemDescription = input('Item description:\n')
            except ValueError:
                print('Entered value is invalid. Please try again.\n')
                continue

            # append item in (Item) class
            item = Item(itemName, itemPrice, itemQuantity, itemDescription)
            shoppingCart.addItem(item)
        elif userInput == 'o':
            print('Output Shopping Cart')
            print("{}'s Shopping Cart - {}".format(shoppingCart.customerName,
                                                   shoppingCart.currentDate.strftime("%B {}, %Y")
                                                   .format(shoppingCart.currentDate.day)))
            print('Number of Items:', shoppingCart.getNumItemInCart())
            shoppingCart.printTotal()
        elif userInput == 'i':
            print("Output Items' Descriptions")
            print("{}'s Shopping Cart - {}".format(shoppingCart.customerName,
                                                   shoppingCart.currentDate.strftime("%B {}, %Y")
                                                   .format(shoppingCart.currentDate.day)))
            shoppingCart.printDescriptions()
        elif userInput == 'r':
            itemName = input('Item name to remove:\n')
            shoppingCart.removeItem(itemName)
        elif userInput == 'c':
            try:
                itemName = input('Item name to modify:\n')
                itemPrice = float(input('Item price:\n'))
                itemQuantity = int(input('Item quantity:\n'))
                itemDescription = input('Item description:\n')
            except ValueError:
                print('Entered value is invalid. Please try again.\n')
                continue

            # append item in (Item) class
            item = Item(itemName, itemPrice, itemQuantity, itemDescription)
            shoppingCart.modifyItem(item)
        elif userInput == 'q':
            break
        else:
            print('Invalid choice, please try again')

        print()

def isValidDate(dateString):
    """
    Validate the date string
    :param dateString: date string in the format [January 31, 9999]
    :return: true or false
    """
    try:
        datetime.strptime(dateString, "%B %d, %Y")
        return True
    except ValueError:
        return False

def printMenu():
    """
    print menu choices
    :return: none
    """
    menuList = ['a - Add item to cart',
                'r - Remove item from cart',
                'c - Change item quantity',
                "i - Output items' description",
                'o - Output shopping cart',
                'q - quit']
    print('Menu')
    for menuItem in menuList:
        print(menuItem)
    print('Choose an option:')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
