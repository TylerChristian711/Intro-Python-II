from room import Room
from player import Player
from items import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                  [(Item('map', 'Map to another treasure in another location.'))]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [(Item('sword', "an old rusty blade it's been here awhile."))]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                   [(Item('key', "Old rusty key, it has an inscription on it but it's worn and faded."))]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [(Item('skeleton', "Only dusty bones remain in this room."))]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
# needed a comment for commit

# Make a new player object that is currently in the 'outside' room.

player = Player("Tyler", room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def perform_move(user_input):
    if user_input in ['q', 'quit', 'exit']:
        print("\nThanks for playing!\n")
        global running
        running = False
    elif user_input in ['?', 'help']:
        print("\nValid commands: ['n': North, 's': South, 'e': East,\n"
              "'w': West, i: View Inventory, 'q, quit, exit': Quit, '?, help': Help]\n")
    elif user_input == 'i':
        for index, item in enumerate(player.items):
            print(f"{index +1}. {item.name}")
    else:
        next_room = player.move_to(user_input)
        if next_room is None:
            print("\nNo room in this direction.\n")
        elif next_room is room['treasure']:
            item_list = [i.name for i in player.items]
            if 'key' not in item_list:
                print("You must find the key to open this door")
            else:
                player.current_room = next_room
        else:
            player.current_room = next_room


def perform_action(user_input):
    if user_input[0] in ['get', 'take,', 'pickup']:
        for item in player.current_room.items:
            if item.name == user_input[1]:
                item.on_take(player)
            else:
                print(f"{user_input[1]} cannot be found in this room")
    elif user_input[0] in ['drop', 'putdown', 'place']:
        for item in player.items:
            if item.name == user_input[1]:
                item.on_drop(player)


running = True

while running:
    print(f"\n{player.current_room.name}\n")
    print(f"{player.current_room.description}\n")
    if len(player.current_room.items) > 0:
        for item in player.current_room.items:
            print(f"You find: {item.name}, {item.description}")

    user_input = input('\nWhere do you want to go? Enter (n, s, e, or w; q to quit): ').split(' ')
    if len(user_input) > 1:
        perform_action(user_input)
    else:
        perform_move(user_input[0])
