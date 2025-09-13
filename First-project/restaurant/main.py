menu = {}

from restaurant.chef import add_dish, remove_dish, update_price, place_order, display_menu

# Adding dishes to the menu
add_dish(menu, "Pizza", 12.99)
add_dish(menu, "Pasta", 9.99)
add_dish(menu, "Salad", 6.99)

# Displaying the menu
display_menu(menu)

# Placing an order for Pizza
place_order(menu, "Pizza")

# Displaying the menu after placing the order
display_menu(menu)

# Updating the price of Pizza
update_price(menu, "Pizza", 13.99)

# Displaying the menu after price update
display_menu(menu)