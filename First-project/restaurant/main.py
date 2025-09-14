menu = {}

from restaurant.chef import add_dish as add, remove_dish as rem ,update_price as up, place_order as pla, display_menu as dis
add(menu, "Pizza", 12.99)
add(menu, "Pasta", 9.99)
add(menu, "Salad", 6.99)
dis(menu)
pla(menu, "Pizza")
dis(menu)
up(menu, "Pizza", 13.99)
dis(menu)
