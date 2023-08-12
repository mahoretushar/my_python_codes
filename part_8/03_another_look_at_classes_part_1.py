# Another example of Class

class House:
    """A class to model a house that is for sale."""

    def __init__(self, style, sq_footage, year_built, price):
        self.style = style
        self.sq_footage = sq_footage
        self.year_built = year_built
        self.price = price

        self.sold = False
        self.weeks_on_market = 0

    def display_info(self):
        """Display the information on the house"""
        print(f"\n-----House for Sale-----")
        print(f"House Style: {self.style}")
        print(f"Square Feet: {self.sq_footage}")
        print(f"Year Built: {self.year_built}")
        print(f"Sale Price: {self.price}")
        print(f"\nThis house has been on the market for {self.weeks_on_market} weeks.")

    def sell_house(self):
        """Sell the house!"""
        if self.sold == False:
            print(f"Congratulations! Your house has sold for Rs. {self.price}")
            self.sold = True
        else:
            print("Sorry, this house is no longer for sale.")

    def change_price(self, amount):
        """Change the sale price of the house"""
        self.price += amount
        if amount < 0:
            print("Price drop!!!!")
        else:
            print(f"The house has increased in value by Rs. {amount}")

    def update_week(self, weeks=1):
        """Increment the number of weeks a house has been on the market"""
        self.weeks_on_market += weeks


my_house = House("Ranch", 1800, 1962, 50000000)

# Print out attributes
print(my_house.style)
print(my_house.sq_footage)
print(my_house.price)
print(my_house.sold)

my_house.display_info()

# house on market for 1 week
my_house.update_week()
my_house.display_info()

# house on market for 15 weeks
my_house.update_week(15)
my_house.display_info()

# Change in Price
my_house.change_price(-150000)
my_house.display_info()

# Sell the house
my_house.sell_house()
my_house.display_info()
my_house.sell_house()
