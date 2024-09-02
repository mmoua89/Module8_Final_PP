"""
A Shopping Cart class that represent a customer name,
date and the added items with their prices and the total cost.
"""
from datetime import datetime
from Item import Item
class ShoppingCart:
    def __init__(self, customerName="none", currentDate=datetime(2020, 1, 1)):
        """
        Default constructor
        :param customerName: customer name
        :param currentDate: date
        """
        self.customerName = customerName
        self.currentDate = currentDate
        self.cartItems = []

    def addItem(self, itemToPurchase):
        """
        Add an item into a shopping cart
        :param itemToPurchase: item to purchase (object)
        :return: none
        """
        self.cartItems.append(itemToPurchase)

    def removeItem(self, itemName):
        """
        Remove an item from the shopping cart
        :param itemName: item name
        :return: none
        """
        for item in self.cartItems:
            if itemName == item.itemName:
                self.cartItems.remove(item)
                print('Removed:', itemName)
                return
        print('Item not found in cart. Nothing removed.')

    def modifyItem(self, itemToPurchase):
        """
        Modify an item only if they are not equal
            to the default value
        :param itemToPurchase: item to modify (object)
        :return: none
        """
        for item in self.cartItems:
            if item.itemName == itemToPurchase.itemName:
                if itemToPurchase.itemPrice > 0.0:
                    item.itemPrice = itemToPurchase.itemPrice
                if itemToPurchase.itemQuantity > 0:
                    item.itemQuantity = itemToPurchase.itemQuantity
                if itemToPurchase.itemDescription != "none":
                    item.itemDescription = itemToPurchase.itemDescription
                return
        print('Item not found in cart. Nothing modified.')

    def getNumItemInCart(self):
        """
        Get the total number items in the shopping cart
        :return: total item quantity
        """
        totalQuantity = 0
        for item in self.cartItems:
            totalQuantity += item.itemQuantity
        return totalQuantity

    def getTotalCost(self):
        """
        Get the total cost for all items in the shopping cart
        :return: total cost of all items
        """
        totalCost = 0.0
        for item in self.cartItems:
            totalCost += item.calculate_total_cost()
        return totalCost

    def printTotal(self):
        """
        Print each item and their total cost
        :return: none
        """
        if len(self.cartItems) == 0:
            print('SHOPPING CART IS EMPTY.')
            return

        for item in self.cartItems:
            item.print_item_cost()

        print('Total: ${:.2f}'.format(self.getTotalCost()))

    def printDescriptions(self):
        """
        Print each item and their description
        :return: none
        """
        for item in self.cartItems:
            print('{}: {}'.format(item.itemName, item.itemDescription))