class Menu:

  #class Menu constructor 
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  #String representation method that will tell you the name of the menu and when the menu is available
  def __repr__(self):
    return f"{self.name} Menu is available from {self.start_time} until {self.end_time}."
  
  #return the total bill of a purchase
  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
    return bill

class Franchise:

  #Franchise class a constructor
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  #String representation to tell the Franchise apart. 
  def __repr__(self):
    return self.address

  #Creating a list to let customers know which menu is available at the "time" passed in as an argument
  def available_menus(self, time):
    menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menu_list.append(menu)
    return menu_list

class Business:

  #Business constructor
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#Brunch Menu
brunch_items = {
  'pancakes': 7.50,
  'waffles': 9.00,
  'burger': 11.00,
  'home fries': 4.50,
  'coffee': 1.50,
  'espresso': 3.00,
  'tea': 1.00,
  'mimosa': 10.50,
  'orange juice': 3.50
  }
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

#Early-bird Menu
early_bird_menu_items = {
  'salumeria plate': 8.00,
  'salad and breadsticks (serves 2, no refills)': 14.00,
  'pizza with quattro formaggi': 9.00,
  'duck ragu': 17.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 1.50, 'espresso': 3.00
  }
early_bird_menu = Menu("Early Bird", early_bird_menu_items, 1500, 1800)

#Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00,
  'caesar salad': 16.00,
  'pizza with quattro formaggi': 11.00,
  'duck ragu': 19.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 2.00,
  'espresso': 3.00
  }
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

#Kids Menu
kids_items = {
  'chicken nuggets': 6.50,
  'fusilli with wild mushrooms': 12.00,
  'apple juice': 3.00
  }
kids_menu = Menu("Kids", kids_items, 1100, 2100)

#Testing calculate_bill
# print(early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))


#---------------------------------------------------------------------
"""
Basta Fazoolin’ with my Heart has seen tremendous success with the family market, which is fantastic because when you’re at Basta Fazoolin’ with my Heart with family, that’s great!
We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the country.
"""

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# #Testing available_menu
# print(flagship_store.available_menus(1700))


#---------------------------------------------------------------------
"""
Since we’ve been so successful building out a branded chain of restaurants, we’ve decided to diversify. We’re going to create a restaurant that sells arepas!
"""

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#Creating a Menu for our new Business
arepas_items = {
  'arepa pabellon': 7.00,
  'pernil arepa': 8.50,
  'guayanes arepa': 8.00,
  'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, 1000, 2000)
#Creating a new Franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
#Creating a new Business
arepa_business = Business("Take a' Arepa", [arepas_place])

#Testing Arepa Business
print(arepa_business.franchises[0])
print(arepa_business.franchises[0].menus[0])
