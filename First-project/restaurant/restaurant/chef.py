def add_dish(menu, name, price):
    if name in menu:
        print(f"The dish '{name}' already exists in the menu.")
    else:
        menu[name] = {'price': price, 'available': True}
        print(f"Added '{name}' to the menu.")

def remove_dish(menu, name):
    if name in menu:
        del menu[name]
        print(f"Removed '{name}' from the menu.")
    else:
        print(f"The dish '{name}' does not exist in the menu.")

def update_price(menu, name, new_price):
    if name in menu:
        menu[name]['price'] = new_price
        print(f"Updated the price of '{name}' to ${new_price:.2f}.")
    else:
        print(f"The dish '{name}' does not exist in the menu.")

def place_order(menu, name):
    if name in menu:
        if menu[name]['available']:
            menu[name]['available'] = False
            print(f"'{name}' has been ordered.")
        else:
            print(f"The dish '{name}' is not available.")
    else:
        print(f"The dish '{name}' does not exist in the menu.")

def display_menu(menu):
    for name, details in menu.items():
        availability = "Available" if details['available'] else "Ordered"
        print(f"{name} - ${details['price']:.2f} - {availability}")