"""Game functions module.

This module provides functions for a text-based game. It includes
functions to print welcome messages, shop menus, simulate item purchase,
and generate random monsters.

Functions:
    purchase_item: Calculate purchase quantity and remaining money.
    random_monster: Generate a random monster with attributes.
    print_welcome: Display a welcome message
    print_shop_menu: Print a formatted shop menu.
    fight_monster: Conduct a fight with a monster (including sub-menu to fight or run).
    test_functions: Runs tests for the module functions
"""

import random

def purchase_item(itemPrice: str, startingMoney: str, quantityToPurchase: int = 1):
    """
    Purchase items based on available money and item price.
    Returns the number of items purchased and leftover money as a string.
    """
    price = float(itemPrice)
    money = float(startingMoney)
    max_affordable = int(money // price)
    num_purchased = min(quantityToPurchase, max_affordable)
    leftover_money = money - (num_purchased * price)
    leftover_money_str = f"{leftover_money:.2f}"
    return num_purchased, leftover_money_str

def random_monster():
    """
    Generate and return a dictionary representing a random monster.
    """
    monster_options = [
        {
            "name": "A goblin",
            "description": "A goblin stands before you",
            "health_range": (10, 25),
            "power_range": (4, 9),
            "money_range": (2.0, 9.0),
            "speed_range": (18, 28),
            "defense_range": (1, 4),
            "intelligence_range": (4, 9)
        },
        {
            "name": "A Crow",
            "description": "A crow stands before you",
            "health_range": (2, 4),
            "power_range": (1, 4),
            "money_range": (40.0, 130.0),
            "speed_range": (28, 38),
            "defense_range": (2, 4),
            "intelligence_range": (2, 4)
        },
        {
            "name": "An Orc",
            "description": "A tall green orc stands before you",
            "health_range": (25, 45),
            "power_range": (4, 11),
            "money_range": (1.0, 25.0),
            "speed_range": (8, 18),
            "defense_range": (4, 9),
            "intelligence_range": (2, 6)
        },
        {
            "name": "A Cyclops",
            "description": "A Cyclops stands before you",
            "health_range": (55, 95),
            "power_range": (12, 22),
            "money_range": (210.0, 490.0),
            "speed_range": (13, 28),
            "defense_range": (18, 28),
            "intelligence_range": (18, 38)
        },
        {
            "name": "A Possessed Crow",
            "description": "A possessed crow with glowing eyes and a haunting presence hovers in the air",
            "health_range": (6, 8),
            "power_range": (4, 7),
            "money_range": (35.0, 65.0),
            "speed_range": (36, 46),
            "defense_range": (3, 5),
            "intelligence_range": (9, 13)
        }
    ]
    chosen_monster = random.choice(monster_options)
    health = random.randint(chosen_monster["health_range"][0], chosen_monster["health_range"][1])
    power = random.randint(chosen_monster["power_range"][0], chosen_monster["power_range"][1])
    money = round(random.uniform(chosen_monster["money_range"][0], chosen_monster["money_range"][1]), 2)
    speed = random.randint(chosen_monster["speed_range"][0], chosen_monster["speed_range"][1])
    defense = random.randint(chosen_monster["defense_range"][0], chosen_monster["defense_range"][1])
    intelligence = random.randint(chosen_monster["intelligence_range"][0], chosen_monster["intelligence_range"][1])
    return {
        "name": chosen_monster["name"],
        "description": chosen_monster["description"],
        "health": health,
        "power": power,
        "money": money,
        "speed": speed,
        "defense": defense,
        "intelligence": intelligence
    }

def print_welcome(name: str, width: int):
    """
    Print a centered welcome message for the given name.
    """
    message = f"Hello, {name}!"
    print(message.center(width))

def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float):
    """
    Print a formatted shop menu with two items and prices.
    """
    top_border = "/" + "-" * 22 + "\\"
    bottom_border = "\\" + "-" * 22 + "/"
    price1_str = f"${item1Price:7.2f}"
    price2_str = f"${item2Price:7.2f}"
    line1 = f"| {item1Name:<12}{price1_str} |"
    line2 = f"| {item2Name:<12}{price2_str} |"
    print(top_border)
    print(line1)
    print(line2)
    print(bottom_border)

def fight_monster(user_hp, user_gold, user_inventory, equipped_weapon):
    """
    Conduct a fight between the user and a random monster, with an option to run.
    Returns the updated user HP and user gold after the fight.
    """
    monster = random_monster()
    monster_hp = monster["health"]
    print(f"\n{monster['description']}")
    print(f"It has {monster_hp} HP and {monster['power']} power.")
    """
    Gently checks if you wish to use your special gear to vanquish the monster.
    """
    can_use_weapon = None
    if equipped_weapon:
        for item in user_inventory:
            if item["name"] == equipped_weapon and item["type"] == "weapon" and item["currentDurability"] > 0:
                can_use_weapon = item
                break
    if can_use_weapon:
        use_choice = input("\nWould you like to use your equipped weapon to instantly defeat the monster? (y/n) ")
        if use_choice.lower() == "y":
            monster_hp = 0
            can_use_weapon["currentDurability"] -= 1
            if can_use_weapon["currentDurability"] <= 0:
                print(f"Your {can_use_weapon['name']} has broken.")
                user_inventory.remove(can_use_weapon)
    while user_hp > 0 and monster_hp > 0:
        print("\nWhat would you like to do?")
        print("  1) Attack")
        print("  2) Run")
        action = input("Choose an action: ")
        if action == "2":
            print("You run away from the fight.")
            break
        if action != "1":
            print("Invalid choice. Please choose again.")
            continue
        damage_to_monster = random.randint(5, 10)
        monster_hp -= damage_to_monster
        print(f"\nYou hit the monster for {damage_to_monster} damage.")
        print(f"Monster HP is now {monster_hp}.")
        if monster_hp <= 0:
            break
        damage_to_user = monster["power"]
        user_hp -= damage_to_user
        print(f"The monster hits you for {damage_to_user} damage.")
        print(f"Your HP is now {user_hp}.")
    if monster_hp <= 0:
        print(f"\nYou defeated the monster and gained {monster['money']} gold!")
        user_gold += monster["money"]
    elif user_hp <= 0:
        print("\nYou have been defeated by the monster...")
    return user_hp, user_gold

def test_functions():
    """
    Runs tests for the game functions.
    """
    print("----- Testing purchase_item() -----")
    num_purchased, leftover = purchase_item("1.23", "10", 3)
    print("Test 1: purchase_item('1.23', '10', 3)")
    print("  Items purchased:", num_purchased)
    print("  Money remaining:", leftover)
    print()
    num_purchased, leftover = purchase_item("1.23", "2.01", 3)
    print("Test 2: purchase_item('1.23', '2.01', 3)")
    print("  Items purchased:", num_purchased)
    print("  Money remaining:", leftover)
    print()
    num_purchased, leftover = purchase_item("3.41", "21.12")
    print("Test 3: purchase_item('3.41', '21.12') [default quantity]")
    print("  Items purchased:", num_purchased)
    print("  Money remaining:", leftover)
    print()
    num_purchased, leftover = purchase_item("31.41", "21.12")
    print("Additional Test: purchase_item('31.41', '21.12')")
    print("  Items purchased:", num_purchased)
    print("  Money remaining:", leftover)
    print()
    print("----- Testing random_monster() -----")
    monster1 = random_monster()
    print("Monster 1:")
    for key, value in monster1.items():
        print(f"  {key}: {value}")
    print()
    print("----- Testing print_welcome() -----")
    print_welcome("Jeff", 20)
    print_welcome("Audrey", 20)
    print_welcome("Christopher", 20)
    print()
    print("----- Testing print_shop_menu() -----")
    print_shop_menu("Wooden Sword", 119, "Wooden Spear", 100)
    print()
    print_shop_menu("Mango", 0.2, "Rasberries", 140)
    print()
    print_shop_menu("Spoiled Bread", 0.1, "Bag of Oats", 12.34)
    print()
    print_shop_menu("Rare Gem", 339, "Dirty Gem", 132)
    print()
    print_shop_menu("Iron Sword", 550, "Iron Spear", 132)
    print()

def get_shop_items():
    """
    Offers a cozy list of items that can be purchased in the shop.
    """
    return [
        {
            "name": "Sword",
            "type": "weapon",
            "itemDurability": 3,
            "currentDurability": 3,
            "price": 10,
            "note": "Makes monsters go away"
        },
        {
            "name": "Shield",
            "type": "weapon",
            "itemDurability": 5,
            "currentDurability": 5,
            "price": 8,
            "note": "Blocks scary attacks"
        },
        {
            "name": "Rock",
            "type": "misc",
            "itemDurability": 1,
            "currentDurability": 1,
            "price": 2,
            "note": "A simple stone"
        }
    ]

def buy_from_shop(user_gold, user_inventory):
    """
    Kindly shows you the shop's wares and lets you buy something
    if you have enough gold. Adds that item to your inventory.
    """
    shop_items = get_shop_items()
    print("\nAvailable items:")
    for idx, item in enumerate(shop_items, start=1):
        print(f"{idx}) {item['name']} - ${item['price']} - {item['note']}")
    choice = input("Which item would you like to buy? Enter the number or 'q' to quit: ")
    if choice.lower() == 'q':
        return user_gold, user_inventory
    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(shop_items):
            chosen_item = shop_items[choice_idx]
            if user_gold >= chosen_item["price"]:
                user_gold -= chosen_item["price"]
                user_inventory.append(chosen_item.copy())
                print(f"You purchased {chosen_item['name']} for ${chosen_item['price']}!")
            else:
                print("Not enough gold to buy that item.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")
    return user_gold, user_inventory

def manage_inventory(user_inventory, equipped_weapon):
    """
    Lets you check what you have and pick a weapon to equip
    in a gentle, friendly way.
    """
    while True:
        print("\nYour Inventory:")
        if not user_inventory:
            print("  (empty)")
        else:
            for i, item in enumerate(user_inventory, start=1):
                print(f"  {i}) {item['name']} ({item['type']}) Durability: {item['currentDurability']}/{item['itemDurability']}")
        print("\nInventory Menu:")
        print("  1) Equip a weapon")
        print("  2) Return to previous menu")
        choice = input("Choose an option: ")
        if choice == "1":
            weapons = [it for it in user_inventory if it["type"] == "weapon"]
            if not weapons:
                print("You have no weapons to equip.")
                continue
            print("\nWeapons available:")
            for i, w in enumerate(weapons, start=1):
                print(f"  {i}) {w['name']} (Durability: {w['currentDurability']}/{w['itemDurability']})")
            print("  q) Cancel")
            wep_choice = input("Pick a weapon to equip: ")
            if wep_choice.lower() == "q":
                continue
            try:
                wep_idx = int(wep_choice) - 1
                if 0 <= wep_idx < len(weapons):
                    equipped_weapon = weapons[wep_idx]["name"]
                    print(f"You have equipped the {equipped_weapon}.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid choice.")
        elif choice == "2":
            break
        else:
            print("Invalid choice.")
    return equipped_weapon

if __name__ == "__main__":
    test_functions()
