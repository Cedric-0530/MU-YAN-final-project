'''Backpack Management'''
item_library = [
    {'name': 'Stamina Potion', 'rarity': 'Common', 'type': 'Consumable'},
    {'name': 'Mana Potion', 'rarity': 'Common', 'type': 'Consumable'},
    {'name': 'Gold Coin', 'rarity': 'Common', 'type': 'Currency'},
    {'name': 'Map', 'rarity': 'Uncommon', 'type': 'Tool'},
    {'name': 'Master Key', 'rarity': 'Rare', 'type': 'Tool'},
    {'name': 'Universal Forging Material', 'rarity': 'Uncommon', 'type': 'Material'},
    {'name': 'Sword', 'rarity': 'Common', 'type': 'Equipment'},
    {'name': 'Shield', 'rarity': 'Common', 'type': 'Equipment'},
    {'name': 'Ring', 'rarity': 'Rare', 'type': 'Equipment'},
    {'name': 'Skill Book', 'rarity': 'Rare', 'type': 'Consumable'}
]

inventory = {}

'''Maximum number of items allowed in backpack (total quantity)'''
MAX_CAPACITY = 64

'''View Backpack'''
def view_inventory():
    while True:
        print('')
        print('Your Backpack:')
        if len(inventory) == 0:
            print('(Empty)')
        else:
            total = 0
            for item in inventory:
                rarity = next((i['rarity'] for i in item_library if i['name'] == item), 'Unknown')
                type_ = next((i['type'] for i in item_library if i['name'] == item), 'Unknown')
                print(f"- {item} [{type_}, {rarity}] x {inventory[item]}")
                total += inventory[item]
            print('Total items:', total, '/', MAX_CAPACITY)
        
        print('\n0. Return to main menu')
        choice = input('Press 0 to return: ')
        if choice == '0':
            break

'''Show current capacity'''
def show_capacity():
    total = 0
    for item in inventory:
        if item == 'Gold Coin':
            total += 1 if inventory[item] > 0 else 0
        else:
            total += inventory[item]
    print('Current capacity:', total, '/', MAX_CAPACITY)

'''Use an item'''
def use_item():
    while True:
        print('')
        print('Available Items:')
        if len(inventory) == 0:
            print('(No items in backpack)')
            print('\n0. Return to main menu')
            choice = input('Press 0 to return: ')
            if choice == '0':
                break
            return
            
        available_items = []
        for item in inventory:
            if item != 'Gold Coin':  # Skip items that cannot be used
                rarity = next((i['rarity'] for i in item_library if i['name'] == item), 'Unknown')
                type_ = next((i['type'] for i in item_library if i['name'] == item), 'Unknown')
                available_items.append((item, type_, rarity, inventory[item]))
        
        if not available_items:
            print('(No usable items in backpack)')
            print('\n0. Return to main menu')
            choice = input('Press 0 to return: ')
            if choice == '0':
                break
            return
            
        for item, type_, rarity, quantity in available_items:
            print(f"- {item} [{type_}, {rarity}] x {quantity}")
        
        print('\n0. Return to main menu')
        item = input('Enter the name of the item to use (or 0 to return): ')
        if item == '0':
            break
        if item == 'Gold Coin':
            print('You cannot use this item directly.')
            continue
        if item in inventory:
            if inventory[item] > 0:
                inventory[item] -= 1
                if inventory[item] == 0:
                    del inventory[item]
                print('You used a', item + '!')
                if item == 'Stamina Potion':
                    print('You feel re-energized!')
                elif item == 'Mana Potion':
                    print('Your mana is restored!')
                elif item == 'Map':
                    print('You check your surroundings and mark new paths.')
                elif item == 'Master Key':
                    print('You unlock a mysterious door.')
                elif item == 'Universal Forging Material':
                    print('You use the material to upgrade equipment!')
                elif item == 'Ring':
                    print('You wear the ring and feel magical power flow through you.')
                elif item == 'Skill Book':
                    print('You learned a new ability!')
                else:
                    print('It had some effect...')
            else:
                print('No more of this item left.')
        else:
            print('This item is not in your backpack.')

'''Add Item to Backpack'''
def add_item():
    while True:
        print('')
        print('Available Items:')
        index = 0
        while index < len(item_library):
            item = item_library[index]
            print(f"{index + 1}. {item['name']} ({item['type']}, {item['rarity']})")
            index += 1

        print('\n0. Return to main menu')
        choice = input('Choose an item number to add (or 0 to return): ')
        if choice == '0':
            break
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(item_library):
                selected_item = item_library[choice - 1]['name']
                qty_input = input('How many do you want to add? ')
                if qty_input.isdigit():
                    qty = int(qty_input)

                    current_total = sum(inventory.values())
                    if current_total + qty > MAX_CAPACITY:
                        print('Cannot add items. Backpack will exceed capacity of', MAX_CAPACITY, 'items.')
                        continue

                    if selected_item in inventory:
                        inventory[selected_item] += qty
                    else:
                        inventory[selected_item] = qty
                    print('Added', qty, selected_item, 'to your backpack.')
                else:
                    print('Invalid quantity.')
            else:
                print('Invalid item number.')
        else:
            print('Invalid input.')

'''Remove Item from Backpack'''
def remove_item():
    while True:
        print('')
        if len(inventory) == 0:
            print('(No items in backpack)')
            print('\n0. Return to main menu')
            choice = input('Press 0 to return: ')
            if choice == '0':
                break
            return
            
        print('Items in backpack:')
        for item in inventory:
            rarity = next((i['rarity'] for i in item_library if i['name'] == item), 'Unknown')
            type_ = next((i['type'] for i in item_library if i['name'] == item), 'Unknown')
            print(f"- {item} [{type_}, {rarity}] x {inventory[item]}")
            
        print('\n0. Return to main menu')
        item = input('Enter the name of the item to remove (or 0 to return): ')
        if item == '0':
            break
        if item in inventory:
            qty_input = input('How many do you want to remove? ')
            if qty_input.isdigit():
                qty = int(qty_input)
                if qty >= inventory[item]:
                    del inventory[item]
                    print('All of', item, 'removed.')
                else:
                    inventory[item] = inventory[item] - qty
                    print('Removed', qty, item, '. Remaining:', inventory[item])
            else:
                print('Invalid quantity.')
        else:
            print('This item is not in your backpack.')

'''Search Items'''
def search_items():
    print('')
    search_term = input('Enter item name to search: ').lower()
    found_items = []
    
    # Search in inventory
    for item in inventory:
        if search_term in item.lower():
            rarity = next((i['rarity'] for i in item_library if i['name'] == item), 'Unknown')
            type_ = next((i['type'] for i in item_library if i['name'] == item), 'Unknown')
            found_items.append((item, type_, rarity, inventory[item], 'In Backpack'))
    
    # Search in item library
    for item in item_library:
        if search_term in item['name'].lower():
            if item['name'] not in inventory:
                found_items.append((item['name'], item['type'], item['rarity'], 0, 'In Library'))
    
    if found_items:
        print('\nSearch Results:')
        for item, type_, rarity, quantity, location in found_items:
            if quantity > 0:
                print(f"- {item} [{type_}, {rarity}] x {quantity} ({location})")
            else:
                print(f"- {item} [{type_}, {rarity}] ({location})")
    else:
        print('No items found matching your search.')

'''Clear Backpack'''
def clear_inventory():
    confirm = input('Are you sure you want to clear your backpack? (y/n): ')
    if confirm.lower() == 'y':
        inventory.clear()
        print('Backpack has been cleared!')
    else:
        print('Cancelled.')

'''Show Help Menu'''
def show_help():
    print('\nHelp Menu:')
    print('1. View Backpack         - View all items and their quantities in your backpack')
    print('2. Add Item              - Add items from the item library to your backpack')
    print('3. Remove Item           - Remove specified items from your backpack')
    print('4. Show Current Capacity - Show the current capacity of your backpack')
    print('5. Use Item              - Use an item from your backpack')
    print('6. Search Items          - Search for items in your backpack or the item library')
    print('7. Clear Backpack        - Remove all items from your backpack at once')
    print('8. Help                  - Show this help menu')
    print('9. Exit                  - Exit the program')

'''Main Program Menu'''
def main():
    while True:
        print('')
        print('Backpack Management')
        print('1. View Backpack')
        print('2. Add Item')
        print('3. Remove Item')
        print('4. Show Current Capacity')
        print('5. Use Item')
        print('6. Search Items')
        print('7. Clear Backpack')
        print('8. Help')
        print('9. Exit')
        choice = input('Choose an option (1-9): ')

        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            show_capacity()
        elif choice == '5':
            use_item()
        elif choice == '6':
            search_items()
        elif choice == '7':
            clear_inventory()
        elif choice == '8':
            show_help()
        elif choice == '9':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')

'''Start the program'''
main()
