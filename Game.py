import Gamefunctions
import os

def main():
    user_hp = 50
    user_gold = 20
    max_hp = 100
    user_inventory = []
    equipped_weapon = None

    if os.path.exists("savefile.json"):
        load_choice = input("Would you like to load your previous game? (y/n): ")
        if load_choice.lower() == 'y':
            data = Gamefunctions.load_game()
            if data:
                user_hp = data.get("user_hp", user_hp)
                user_gold = data.get("user_gold", user_gold)
                user_inventory = data.get("user_inventory", [])
                equipped_weapon = data.get("equipped_weapon", None)

    name = input("Enter your name: ")
    Gamefunctions.print_welcome(name, 40)
    print()

    while True:
        print(f"\nYou have {user_hp} HP and {user_gold} gold.")
        print("What would you like to do?")
        print("  1) City")
        print("  2) Fight a monster outside of the city")
        print("  3) Sleep (Restore up to 10 HP)")
        print("  4) Visit the shop")
        print("  5) Manage Inventory")
        print("  6) Quit")
        print("  7) Save and Quit")
        choice = input("Enter your choice: ")
        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Please try again.")
            continue
        if choice == "1":
            print("\nYou head to the city. You see beautiful buildings, and shops all around")
        elif choice == "2":
            user_hp, user_gold = Gamefunctions.fight_monster(user_hp, user_gold, user_inventory, equipped_weapon)
            if user_hp <= 0:
                print("\nYou died. Game Over.")
                break
        elif choice == "3":
            heal_amount = 10
            old_hp = user_hp
            user_hp = min(user_hp + heal_amount, max_hp)
            print(f"\nYou rest, restoring {user_hp - old_hp} HP. Your HP is now {user_hp}.")
        elif choice == "4":
            user_gold, user_inventory = Gamefunctions.buy_from_shop(user_gold, user_inventory)
        elif choice == "5":
            equipped_weapon = Gamefunctions.manage_inventory(user_inventory, equipped_weapon)
        elif choice == "6":
            print("\nThanks for playing!")
            break
        elif choice == "7":
            Gamefunctions.save_game(user_hp, user_gold, user_inventory, equipped_weapon)
            print("\nGame saved. Goodbye!")
            break

    print("Exiting game.")

if __name__ == "__main__":
    main()
