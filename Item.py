"""
An item class that represent an item name, price, and quantity
"""
class Item:
    def __init__(self, itemName="none", itemPrice=0.0, itemQuantity=0, itemDescription="none"):
        """
        Default constructor
        :param item_name: the name of an item -> str
        :param item_price: the price of an item -> float
        :param item_quantity: the quantity of an item -> int=
        """
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemQuantity = itemQuantity
        self.itemDescription = itemDescription

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of the quantity x price
        :return: total cost
        """
        return self.itemQuantity * self.itemPrice

    def print_item_cost(self):
        """
        Display the item name and the total cost
        :return: void
        """
        print("{} {} @ ${:.2f} = ${:.2f}".format(self.itemName,
              self.itemQuantity, self.itemPrice, self.calculate_total_cost()))
