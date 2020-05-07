from room import Room
from player import Player
from items import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                  [(Item('Map', 'Map to another treasure in another location.'))]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [(Item('sword', "an old rusty blade it's been here awhile."))]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                   [(Item('Key', "Old rusty key, it has an inscription on it but it's worn and faded."))]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [(Item('Skeleton', "Only dusty bones remain in this room."))]),
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


running = True

while running:
    print(f"{player.current_room.name}\n")
    print(f"{player.current_room.description}\n")
    if len(player.current_room.items) > 0:
        for item in player.current_room.items:
            print(f"In the room you find {item.name}, {item.description}")

    user_input = input('Where do you want to go? Enter (n, s, e, or w; q to quit: ')
    if user_input == 'q':
        print("\nThanks for playing come again!\n")
        running = False
    elif user_input in ['?', 'help']:
        print("\nValid commands: n: to go north, e: to go east,\n"
              "w: to go west q: to quit game, ?,help: Help\n ")
    else:
        next_room = player.move_to(user_input)
        if next_room is None:
            print("\nThere is no place to go in that direction\n")
        else:
            player.current_room = next_room
