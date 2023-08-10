# This is a project for Coffee Shop

print("Hello, Welcome to TCoffee!!!!!!!!")
customer_name = input("What is Your Name? \n").lower()

enemies_list = ["ben", "chintu", "superman"]

if customer_name in enemies_list:
    print("Get out of the Shop.")
else:
    print(f"\nHello! {customer_name}, thank you so much fo3r coming in today!!\n")

    menu = {
        "Black Coffee": 20,
        "Cold Coffee": 50,
        "Tea": 70
    }

    print(f"{customer_name}, what would you like to order form our menu today? Here is what we are serving:\n{menu}")

    total_items = int(input("How many items you like to order: "))
    order_list = {}

    for item in range(1, total_items + 1):
        order = input(f"Your order No. {item} Please: ")
        quantity = int(input(f"How many cups of {order} you want?"))
        order_list[order] = quantity

    print(order_list)

    total_price = 0
    for menu_item, menu_item_price in order_list.items():
        for order_item, order_item_quantity in menu.items():
            if menu_item == order_item:
                total_price += menu_item_price * order_item_quantity

    print(f"\nSounds good {customer_name}, we will have those {order_list} along with the quantity "
          f"ready for you in a moment.")
    print(f"Thank You. Your total bill is: {total_price}")
