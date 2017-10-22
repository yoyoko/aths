inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(myInventory):
    print('Inventory:')
    item_total = 0
    for k, v in myInventory.items():
        print(f"{v} {k}")
        item_total = item_total + v
    print(f"Total number of items: {str(item_total)}")

displayInventory(inventory)

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)): #loops the whole way through the Loot
        inventory.setdefault(addedItems[i], 0) #adds loot names into inventory
        inventory[addedItems[i]] = inventory[addedItems[i]] + 1 #adds one to each listed item
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
