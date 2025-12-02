import json

# player dict has location
# "item is located in [room]

# World is a list of room dictionaries
# room dictionaries have the keys title, description, items, and doors
# player is a dictionary representing the user with the keys location and inventory 
# the players location corresponds to the title within a room dictionary where they currently are


# room = {
# "title": ,
# "description": ,
# "items": ,
# "doors": ,

def save_world(world):
    """
    Save the input for world world to a .json file called world
    if the .json file exists, erase it and replace it with the contents of the list world
    Args:
    world = a list of room dictionaries
    """
    with open("world.json", "w") as f:
        json.dump(world, f, indent=2)
        print("Saved to world.json")

def save_player(player):
    """
    Save the input for the dictionary player to a .json file called player
    if the .json file exists, erase it and replace it with the contents of the player dictionary

    Args:
    player (dict):
    """
    with open("player.json", "w") as f:
        json.dump(player, f, indent=2)
        print("Saved to player.json")

def save_item(item):
    """
    Save the input for the dictionary item to a .json file called item
    if the .json file exists, erase it and replace it with the contents of the item dictionary

    Args:
    item (dict): a dictionary of items
    """
    with open("item.json", "w") as f:
        json.dump(item, f, indent=2)
        print("Saved to item.json")

def save_game():
    save_world(world)
    save_player(player)
    save_item(item)

def load_world():
    """
    Load the world data from world.json
    Returns:
        list: A list of room dictionaries
    """
    with open("world.json", "r") as f:
        world = json.load(f)
    return world

def load_player():
    """
    Load the player data from player.json
    Returns:
        dict: The player dictionary
    """
    with open("player.json", "r") as f:
        player = json.load(f)
    return player

def load_item():
    """
    Load the item data from items.json

    Returns:
        dict: The item dictionary
    """
    with open("items.json", "r") as f:
        item = json.load(f)
    return item

def load_game():
    load_world()
    load_player()
    load_item()

world = load_world()
player = load_player()
item = load_item()

def describe_room(player):
    """
    Print the value for the key description in the room dictionary in world which title matches the value for the key location in the player dictionary
    Args:
    player (dict): the player dictionary

    return:
    description (str): description of the current room
    print "You are in [room]" and then the description on the same line
    """
    for room in world:
        if room["title"] == player["location"]:
            description = room["description"]
            print("You are in the", room["title"] + ",", description)
            return description
           
def list_items(player):
    """
    Print the values for the item key in the room dictionary which title value aligns with the player dictionary's location value

    args:
    player (dict): the player dictionary

    return:
    items (list): list of items in the current room
    print the items, make sure in a list of two or more the final value is added after and "and" while the rest are separated by commas
    always begin with "You see a" and always put a period at the end
    """
    for room in world:
        if room["title"] == player["location"]:
            items = room["items"]
            if len(items) > 1:
                items_string = ", a ".join(items[:-1]) + ", and " + items[-1]
            else:
                items_string = items[0]
            print("You see a", items_string + ".")
            return room

def list_doors(player):
    """
    print the values for the door key in the room dictionary which title value matches the player dictionary's location value 

    args:
    player (dict): the player dictionary

    return:
    doors (list): list of doors in the current room
    print the doors, make sure in a list of two or more the final value is added after and "and" while the rest are separated by commas
    always begin with "There are doors to the" and always put a period at the end
    """
    for room in world:
        if room["title"] == player["location"]:
            doors = room["doors"]
            if len(doors) > 1:
                doors_string = ", ".join(doors[:-1]) + ", and " + doors[-1]
            else:
                doors_string = doors[0]
            print("You see doors to the", doors_string + ".")
            return room

def interact_item(item_name, player):
    """
    Take the input for item_name and compare it to the title value for all items in the item dictionary that have a value in the location key that matches the location key in the player dictionary
    If there is a match, return and print the value for description for that item.
    If not, print "there are no items named that"

    Args: 
    item_name (str): the name of the item to interact with, allow for multiple word names
    player (dict): the player dictionary

    Returns:
    description (str): description of the item, print it
    "there are no items named that" if no match
    """
    for itm in item:
        if itm["title"] == item_name and itm["location"] == player["location"]:
            description = itm["description"]
            print(description)
            return description
    print("there are no items named that")

def open_inventory(player):
    """
    Return and print the items listed under the key "inventory" in the player dictionary

    Args:
    player (dict): the player dictionary

    Returns:
    inventory (list): list of items in the player's inventory
    print inventory
    """
    print("You have", player["inventory"], "in your inventory")
    return player["inventory"]

def move_rooms(room_name, player):
    """
    Change the value for the key location in the player dictionary to the input room_name if room_name matches a doors value in the room dictionary where the player is currently located
    If they match, update the location key in the player dictionary to the title value of the new room dictonary

    Args:
    room_name (str): the title value of the room to move to
    player (dict): the player dictionary

    Returns:
    new_location (str): the updated location of the player
    print the new location
    """
    for room in world:
        if room["title"] == player["location"]:
            if room_name in room["doors"]:
                player["location"] = room_name
                print("You have moved to the", room_name)

def player_choice(action):
    """
    Parse the input for action for the words interact, inventory, or move
    If it is interact, use interact_item and parse action again for the input for item_name
    If it is inventory use open_inventory
    If it is move, use move_rooms and parse action again for the input for room_name
    If none, return and print "can not preform action"
    Always allow and consider multiple word names as inputs for item_name and room_name

    Args:
    action (str): the action the player wants to preform

    Returns:
    return of used function, or print "can not preform action" if otherwise
    """
    action_parts = action.split()
    if "interact" in action_parts:
        item_name = action.partition("interact ")[2]
        return interact_item(item_name, player)
    elif "inventory" in action_parts:
        return open_inventory(player)
    elif "move" in action_parts:
        room_name = action.partition("move ")[2]
        return move_rooms(room_name, player)
    else:
        print("can not preform action")

def welcome_screen():
    """
    Print and return the text below, entering a new line for every period or exclaimation point using a formatted string:

    Welcome to Cabin Fever! In this game you play a homocide detective investigating the alleged disappearance of a young man named Theodore Scott.
    In order to solve the case, traverse the house he disappeared in and collect evidence to determine the killer, the murder weapon, and which room it took place in.
    Once you have made your final decision, get in your car to return to the police station and report your findings.
    Good luck!
    ------------
    """

    text = (
        "Welcome to Cabin Fever! "
        "In this game you play a homocide detective investigating the alleged disappearance of a young man named Theodore Scott. "
        "In order to solve the case, traverse the house he disappeared in and collect evidence to determine the killer, the murder weapon, and which room it took place in. "
        "Once you have made your final decision, get in your car to return to the police station and report your findings. "
        "Good luck! ------------"
    )

    import re
    sentences = re.findall(r".*?[.!-]+", text)
    formatted = "\n".join(f"{s.strip()}" for s in sentences)

    print(formatted)
    return formatted

def check_keep_item(item_name, player):
    """
    Check to see if the specified item can be added to the player's inventory.
    For this to be possible, it must have "keep" set to "True" and also have it's inital location match the player's current location.
    If both conditions are met, return True.
    If either or both fail, return False.

    Args:
    item_name (str): the name of an item to check
    player (dict): the player dictionary containing location information

    Returns:
    bool: True if the item has the same location as player and has a keep value of True. False if otherwise
    """
    for itm in item:
        if itm["title"] == item_name:
            if itm["keep"] == "True" and itm["location"] == player["location"]:
                return True
    return False

def keep_item(item_name, player):
    """
    Add the specified item to the player's inventory.
    In doing so, remove the item from the current room's dictionary by removing it from the list of items in that room.
    Then, add the item to the player's inventory list and change it's location to "player".
    An object with it's location value as "player" should always have its title value in the player's inventory list and vice versa.
    For an object to be added 
    If the items "keep" value is "False", print "You cannot keep that item" and if the item is not in the current room print "There is no item by that name here".
    Otherwise, print "You have added [item_name] to your inventory".

    Args:
    item_name (str): the name of the item to keep
    player (dict): the player object containing inventory and location information

    Returns:
    updated_inventory (list): the updated inventory list of the player
    print appropriate messages based on the action taken.
    """

def main():
    welcome_screen()
    load_game()
    while True:
        print()
        describe_room(player)
        list_items(player)
        list_doors(player)
        print()
         # Prompt the player with choices 1. interact, 2. move, 3 open inventory and use selected choice in player_choice
        user_input = input("What would you like to move, interact with an item, or view your inventory?\n")
        player_choice(user_input)
        
        if user_input == 'quit':
            break

# add start or load prompt to main??
# offer rules or summary? (welcome screen)

if __name__ == "__main__":
    main()