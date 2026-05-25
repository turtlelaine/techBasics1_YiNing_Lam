""" this assignment uses AI (deepseek, gemini) for assist:
# 1. help solving errors in def use_item, def process_command, and door_scene (deepseek)
# 2. help checking if all the assignment requirements are fulfilled (deepseek)
# 3. translation in story (gemini)
# 4. suggestions for code structure,
tho I didn't take that suggestion because they put endings at the very first of the code, i dont like (both)(dumb ai)
# 5. deciding my dinner and emotional support🥀🥀🥀(both)(thx ai) """

import time

INVENTORY_LIMIT = 5
inventory = []
current_room = None

inventory.append({"name": "map", "type": "key", "description": "A worn map showing the way."})
ending_conditions = set()


def show_inventory():
    if not inventory:
        print("\nYour bag is empty.")
    else:
        print("\n=== Your Bag ===")
        for i, item in enumerate(inventory, 1):
            uses_info = f" (uses: {item['uses']})" if item.get('uses') else ""
            print(f"{i}. {item['name']} - {item['type']}{uses_info}")
        print(f"Space: {len(inventory)}/{INVENTORY_LIMIT}")


def show_room_items(room_items):
    if not room_items:
        print("\nThere are no items here.")
    else:
        print("\nItems in this area: ")
        for item in room_items:
            print(f"  - {item['name']} ({item['type']})")

def has_item(item_name):
    for item in inventory:
        if item["name"] == item_name:
            return True
    return False

def pick_up(item_name, item_type="normal", uses=1):
    if len(inventory) >= INVENTORY_LIMIT:
        print("Can't carry more items.")
        return False
    inventory.append({"name": item_name, "type": item_type, "uses": uses})
    print(f"[You got: {item_name}]")
    return True

def use_item(item_name):
    for i, item in enumerate(inventory):
        if item["name"] == item_name:
            if item["type"] == "healing":
                print(f"You used {item_name}. You feel better!")
                if item["uses"] > 1:
                    item["uses"] -= 1
                else:
                    inventory.pop(i)
                return True
            elif item["type"] == "key":
                print(f"You can't use {item_name} here. Save it for the door.")
                return True
            else:
                print(f"{item_name} is not usable in this situation.")
                return False
    print(f"You don't have {item_name}.")
    return False

def examine_item(item_name):
    for item in inventory:
        if item["name"] == item_name:
            print(f"\n{item['name']} ")
            print(f"Type: {item['type']}")
            print(f"Uses left: {item.get('uses', 'N/A')}")
            if item["name"] == "map":
                print("Description: A worn map showing the way through the forest.")
            elif item["name"] == "leaf":
                print("Description: A beautiful leaf with unique patterns.")
            elif item["name"] == "crystal ball":
                print("Description: A crystal ball that glows with inner light.")
            else:
                print("Description: Nothing special.")
            return True
    print(f"You don't have {item_name}.")
    return False

def drop(item_name):
    for i, item in enumerate(inventory):
        if item["name"] == item_name:
            inventory.pop(i)
            print(f"[Lost: {item_name}]")
            return True
    return False

def process_command(cmd, room_items):
    cmd = cmd.strip().lower()

    if cmd in ["inventory", "i"]:
        show_inventory()
    elif cmd.startswith("pickup "):
        item_name = cmd[7:].strip()
        found = None
        for item in room_items:
            if item["name"] == item_name:
                found = item
                break
        if found:
            pick_up(item_name, found.get("type", "normal"), 1)
            room_items.remove(found)
            if current_room == "river" and item_name == "bottle":
                print("\nYou pick up the crow's bottle.")
            elif current_room == "grassland" and item_name == "leaf":
                print("\nYou look at the leaves. Their patterns are beautiful.")
                print("You decide to pick one up.")
                ending_conditions.add("picked_leaf")
        else:
            print(f"There is no '{item_name}' here.")
    elif cmd.startswith("drop "):
        item_name = cmd[5:].strip()
        drop(item_name)
    elif cmd.startswith("use "):
        item_name = cmd[4:].strip()
        use_item(item_name)
    elif cmd.startswith("examine "):
        item_name = cmd[8:].strip()
        examine_item(item_name)
    elif cmd in ["look", "l"]:
        show_room_items(room_items)
    elif cmd in ["help", "h"]:
        print("\n=== Commands ===")
        print("inventory / i     - Show your inventory")
        print("look / l          - Look around")
        print("pickup <item>     - Pick up item")
        print("drop <item>       - Drop item")
        print("use <item>        - Use item")
        print("examine <item>    - Examine item")
        print("continue / c      - Continue to next scene")
        print("drink             - Drink water")
        print("give / refuse     - On the train")
        print("leave / keep      - At the sad person")
        print("help / h          - Show this")
    elif cmd in ["continue", "c"]:
        return False
    elif current_room == "river" and cmd == "drink":
        print("\nYou drink the water. It's cool and refreshing!")
        ending_conditions.add("drank_water")
    elif current_room == "train" and cmd == "give":
        print("\nYou hand over all your items.")
        items_to_remove = [item["name"] for item in inventory if item["name"] != "map"]
        for item_name in items_to_remove:
            drop(item_name)
        print("\nThe conductor takes them.")
        print("A warm current flows through your body.")
        print("After a bright flash, you're back on the grassland.")
        pick_up("normal key", "key", 1)
        ending_conditions.add("gave_all_items")
        return False
    elif current_room == "train" and cmd == "refuse":
        print('\nThe conductor smiles: "I understand."')
        print('He hands you a key.')
        print('"Go fulfill your wish," he says.')
        print("\nYou blink, and find yourself back on the grassland.")
        pick_up("wish key", "key", 1)
        ending_conditions.add("kept_items")
        return False
    else:
        print("Unknown command. Type 'help' for available commands.")

    return True

def scene_grassland():
    global current_room
    current_room = "grassland"
    room_items = [{"name": "leaf", "type": "normal"}]

    print("\n" + "=" )
    print("Scene 1: The Grassland")
    print("=" )
    time.sleep(1)

    print("\nYou wake up on an empty grassland.")
    print("The weather is clear. Leaves are gently floating around you.")
    time.sleep(2)

    show_room_items(room_items)
    print("\nType 'help' to see available commands.")

    while True:
        cmd = input("\n> ")
        if not process_command(cmd, room_items):
            break

    if not has_item("leaf"):
        ending_conditions.add("watched_clouds")

    time.sleep(1.5)
    return True

def scene_river():
    global current_room
    current_room = "river"

    room_items = [{"name": "bottle", "type": "normal"}]

    print("\n" + "=" )
    print("Scene 2: The River")
    print("=" )
    time.sleep(1)

    print("\nYou follow the map and walk through a forest.")
    print("A gentle breeze brushes your face.")
    time.sleep(2)
    print("You arrive at a river.")
    time.sleep(1)

    print("\nYou feel a little thirsty.")
    show_room_items(room_items)
    print("\nType 'help' to see available commands. Type 'drink' to drink water.")

    while True:
        cmd = input("\n> ")
        if not process_command(cmd, room_items):
            break

    if has_item("bottle") and "helped_crow" not in ending_conditions:
        print("\nThe crow looks angry! He squawks: 'I'm thirsty! Give it back!'")
        time.sleep(1.5)
        print("You point at the river, showing him there's plenty of water.")
        print("The crow pauses, then bursts into laughter.")
        time.sleep(2)
        print('"I was so focused on the bottle, I didn\'t see the river!"')
        print("To thank you, the crow gives you a gift.")
        pick_up("shiny stone", "special", 1)
        ending_conditions.add("helped_crow")

    time.sleep(1.5)
    return True

def scene_darkness():
    global current_room
    current_room = "darkness"

    print("\n" + "=" )
    print("Scene 3: The Darkness")
    print("=" )
    time.sleep(1)

    print("\nYou continue your journey and arrive at a flickering, shadowy place.")
    time.sleep(2)
    print('A voice echoes: "Why have you come?"')
    time.sleep(1.5)

    print("\nYou think deeply...")
    print("You feel something peering into your mind.")
    time.sleep(2)

    print('\nThe voice speaks again: "...I see. I will let you pass."')
    print('"But you must trade one item with me."')
    time.sleep(1.5)

    print("\nLet's check your bag:")
    show_inventory()

    print("\nWhat do you want to trade?")
    option_num = 1
    options = []

    if has_item("leaf"):
        print(f"{option_num}. Leaf")
        options.append("leaf")
        option_num += 1
    if has_item("bottle"):
        print(f"{option_num}. Bottle")
        options.append("bottle")
        option_num += 1
    if has_item("shiny stone"):
        print(f"{option_num}. Shiny stone")
        options.append("shiny stone")
        option_num += 1

    print(f"{option_num}. Nothing")
    options.append("nothing")

    choice = input(f"\nChoose 1-{option_num}: ")

    try:
        idx = int(choice) - 1
        if idx < len(options):
            selected = options[idx]

            if selected == "leaf":
                drop("leaf")
                print("\nYou offer the leaf.")
                print('The voice chuckles softly but says nothing.')
                print("The darkness parts before you.")
                print("On the ground, you see a branch with leaves attached.")
                print("You happily pick it up.")
                pick_up("branch with leaves", "normal", 1)
                ending_conditions.add("traded_leaf")
            elif selected == "bottle":
                print("\nYou offer the bottle, thinking the voice might be thirsty.")
                print('"Little one, I\'m not thirsty. Keep your bottle."')
                print("The darkness parts before you.")
                print("On the ground, you see a bottle of liquid.")
                print("You pick it up.")
                drop("bottle")
                pick_up("water bottle", "special", 1)
                ending_conditions.add("traded_bottle")
            elif selected == "shiny stone":
                drop("shiny stone")
                print('\nYou offer the shiny stone.')
                print('The voice sounds surprised: "How did you get this stone?..."')
                print('"...Because you helped the crow? I see."')
                print("The voice laughs gently.")
                print("The darkness parts before you.")
                print("On the ground, you see a crystal ball.")
                print("You pick it up.")
                pick_up("crystal ball", "special", 1)
                ending_conditions.add("traded_stone")
            else:
                print('\n"Not trading? How cute."')
                print("The voice laughs loudly as the darkness parts before you.")
                print("You pass through without trading anything.")
                ending_conditions.add("traded_nothing")
    except:
        print('\n"Not trading? How cute."')
        print("The voice laughs loudly as the darkness parts before you.")
        print("You pass through without trading anything.")
        ending_conditions.add("traded_nothing")

    time.sleep(1.5)
    return True

def scene_sad_person():
    global current_room
    current_room = "sad guy"

    print("\n" + "=" )
    print("Scene 4: The Sad Person")
    print("=" )
    time.sleep(1)

    print("\nYou walk on and reach a place where light and shadow meet.")
    time.sleep(1.5)
    print("A person sits on the ground. He looks very sad.")
    time.sleep(1.5)

    print('\nHe mutters to himself: "I miss you so much, Jade..."')
    time.sleep(2)

    print("\nYou stand beside him for a long time.")
    print("So long that you almost think he's fallen asleep.")
    time.sleep(2)

    print("\nBut you need to leave this place.")
    time.sleep(1)

    if has_item("branch with leaves"):
        print("\nDo you want to leave the branch with leaves for him?")
        print("Type 'leave' to leave it, or 'keep' to keep it.")

        while True:
            cmd = input("\n> ").strip().lower()
            if cmd == "leave":
                drop("branch with leaves")
                print("\nYou gently place the branch beside him.")
                ending_conditions.add("left_branch_for_owner")
                break
            elif cmd == "keep":
                print("\nYou decide to keep the branch.")
                ending_conditions.add("kept_branch")
                break
            else:
                print("Type 'leave' or 'keep'.")

    print("\nYou reach out and gently pat his back, bringing a cool breeze.")
    print("You hope he will feel better.")
    time.sleep(2)

    print("\nAfter a while, he slowly looks up...")
    print('"...Jade?"')
    time.sleep(2)

    print("\nBut you've already walked away.")

    time.sleep(1.5)
    return True

def scene_train():
    global current_room
    current_room = "train"

    print("=" )
    print("Scene 5: The Train")
    print("=" )
    time.sleep(1)

    print("\nYou arrive at a train covered in flowers.")
    time.sleep(1.5)
    print("People sit nervously inside.")
    print("You don't know what's happening, but you're glad to finally rest.")
    time.sleep(2)

    print("\nThe flowers beside you turn white when you sit down.")
    print("You like them.")
    print("Other people have flowers of different colors.")
    print("You feel a little envious, but you love your flowers too.")
    time.sleep(2.5)

    print("\nA conductor walks toward each person.")
    print("Each person gives something to the conductor... then disappears.")
    time.sleep(2)

    print('\nThe conductor stops in front of you.')
    print('"Why are you here, little one?" he asks gently.')
    time.sleep(2)

    print("\nYou don't know how to answer, so you just smile.")
    print("You feel something peering into your mind again.")
    time.sleep(2)

    print('\n"I see..." the conductor nods.')
    print('"I need all the items you collected from outside."')
    print('"Can you give them to me?"')
    time.sleep(2)

    print("\nType 'give' to give him everything, or 'refuse' to refuse.")

    while True:
        cmd = input("\n> ").strip().lower()
        if cmd == "give":
            print("\nYou hand over all your items.")
            items_to_remove = [item["name"] for item in inventory if item["name"] != "map"]
            for item_name in items_to_remove:
                drop(item_name)
            print("\nThe conductor takes them.")
            print("A warm current flows through your body.")
            print("After a bright flash, you're back on the grassland.")
            pick_up("normal key", "key", 1)
            ending_conditions.add("gave_all_items")
            break
        elif cmd == "refuse":
            print('\nThe conductor smiles: "I understand."')
            print('He hands you a key.')
            print('"Go fulfill your wish," he says.')
            print("\nYou blink, and find yourself back on the grassland.")
            pick_up("wish key", "key", 1)
            ending_conditions.add("kept_items")
            break
        else:
            print("Type 'give' or 'refuse'.")

    time.sleep(1.5)
    return True

def scene_giant_trees():
    global current_room
    current_room = "giant tree"

    print("\n" + "=" )
    print("Scene 6: The Giant Trees")
    print("=" )
    time.sleep(1)

    print("\nYou look around and see two giant trees.")
    time.sleep(1.5)
    print("On one of them, you notice branches that look familiar...")
    time.sleep(1.5)

    got_something = False

    if has_item("branch with leaves"):
        print("\nYou see your branch resting on the tree.")
        print("You pick it up. It looks cleaner now.")
        got_something = True
    elif has_item("water bottle"):
        print("\nYou see your water bottle by the tree roots.")
        print("The water inside glows faintly.")
        got_something = True
    elif has_item("crystal ball"):
        print("\nYou see your crystal ball sitting on a tree stump.")
        print("It shines brighter than before.")
        got_something = True
    else:
        if "gave_all_items" in ending_conditions:
            print("\nA crystal ball appears on the tree stump, glowing softly.")
            print("The trees remember what you once carried.")
            print("It returns to you, purified.")
            pick_up("crystal ball", "special", 1)
            got_something = True
        else:
            print("\nYou don't see any familiar items here.")

    if not got_something:
        print("\nYou don't see any familiar items here.")

    print("\nYou pass between the two trees...")
    time.sleep(1.5)
    return True

def door_scene():
    global current_room
    current_room = "door"

    print("\n" + "=" )
    print("THE DOOR")
    print("=" )
    time.sleep(1)

    print("\nYou arrive at a door.")

    if has_item("wish key"):
        print("You use the wish key to open the door.")

        if has_item("water bottle"):
            ending_2_wish()
        elif has_item("crystal ball") or has_item("shiny stone"):
            ending_1_home()
        elif "kept_items" in ending_conditions and has_item("branch with leaves"):
            ending_5_flowers()
        else:
            ending_4_wander()

    elif has_item("normal key"):
        print("You use the ordinary key to open the door.")

        if has_item("shiny stone") or has_item("crystal ball"):
            ending_3_kindness()
        else:
            ending_3_kindness()
    else:
        print("\nYou don't have a key to open the door.")
        print("You sit in front of it, waiting...")
        print("Maybe someone will come. Maybe not.")
        print("\n[Ending: Still Waiting]")
        ending_conditions.add("ending_no_key")

def ending_1_home():
    print("\nENDING 1: Way Back Home")
    print("=" )
    time.sleep(1)

    print("\nThe door opens. You smell a familiar scent...")
    print("It's the scent of your owner.")
    time.sleep(1.5)
    print("You walk quickly down the hall and see a half-open door.")
    print("You push it open with your nose.")
    time.sleep(2)

    print("\nYour owner sits in a chair, holding an old collar.")
    print("Your form has changed. You're not the same as before.")
    print("But you remember everything.")
    time.sleep(2)

    print("\nYou believe he will remember you too.")
    print("You bark twice and run toward him.")
    time.sleep(1.5)

    print('\n"Jade...?" He looks up. Tears fall from his eyes.')
    print("\nYou wag your tail and jump into his arms.")
    print("\nYou are home.")

    ending_conditions.add("ending_1_home")

def ending_2_wish():
    print("\nENDING 2: The Weight of Wishes")
    print("=" )
    time.sleep(1)

    print("\nThe key turns into a droplet of water and falls on your hand.")
    print("Your body feels lighter.")
    time.sleep(1.5)
    print("You close your eyes. When you open them, you stand before him.")
    print("You bark with all your might: 'Woof! Woof!'")
    time.sleep(2)

    print("\nHe can't see you. He can't hear you.")
    print("You nuzzle his hand.")
    time.sleep(1.5)

    print('\nHe pauses: "Jade?"')
    print("You wag your tail to answer, but he cannot see or hear you.")
    time.sleep(2)

    print("\nAfter a while, he stands up and closes the door.")
    print("\nYou stay outside, guarding him...")
    print("Guarding the home you can never return to.")

    ending_conditions.add("ending_2_wish")


def ending_3_kindness():
    print("\nENDING 3: The Color of Kindness")
    print("=" )
    time.sleep(1)

    print("\nThe door opens. A soft white glow surrounds you.")
    print("You look down. Your fur has turned pure white...")
    print("As if washed by moonlight.")
    time.sleep(2)

    print("\nYou run across the grassland and through the forest.")
    print("You arrive before him. This time, he sees you.")
    time.sleep(1.5)

    print('\n"Jade... You\'ve become so bright."')
    print("\nHe places his hand on your head.")
    print("His palm glows too.")
    time.sleep(2)

    print("\nYou look at his wrinkled face and white hair... and smile.")
    print("Two shadows stretch long in the sunset...")
    print("Long enough to never part.")

    ending_conditions.add("ending_3_kindness")

def ending_4_wander():
    print("\nENDING 4: The End of Wandering")
    print("=" )
    time.sleep(1)

    print("\nThe key disappears. The door doesn't appear.")
    time.sleep(1.5)
    print("You sit in place, watching the sky turn from blue to orange to purple.")
    print("You don't leave. You don't look back.")
    time.sleep(2)

    print("\nA wind blows, bringing a leaf.")
    print("You hold it in your mouth and keep walking.")
    time.sleep(1.5)

    print("\nMaybe one day, you'll reach your owner. Maybe not.")
    print("But that's okay. You're a dog.")
    print("Dogs don't get lost.")

    ending_conditions.add("ending_4_wander")

def ending_5_flowers():
    print("\nENDING 5: The Language of Flowers")
    print("=" )
    time.sleep(1)

    print("\nYou place the branch in a vase on the train.")
    print("The flowers slowly turn white... then gold.")
    time.sleep(2)

    print('\nThe conductor looks at you and smiles.')
    print('"So you understand the language of flowers."')
    time.sleep(1.5)

    print("\nYou tilt your head. You don't understand.")
    print('\n"They say you\'re a good dog."')
    time.sleep(2)

    print("\nThe train departs. You don't get off.")
    print("You follow the conductor, waiting for the day...")
    print("When the train arrives at 'Home'.")

    ending_conditions.add("ending_5_flowers")

def main():
    print("=" )
    print("JADE's JOURNEY")
    print("=" )
    time.sleep(1.5)

    scene_grassland()
    input("\nPress Enter to continue")

    scene_river()
    input("\nPress Enter to continue")

    scene_darkness()
    input("\nPress Enter to continue")

    scene_sad_person()
    input("\nPress Enter to continue")

    scene_train()
    input("\nPress Enter to continue")

    scene_giant_trees()
    input("\nPress Enter to continue")

    door_scene()

    print("\n" + "=" )
    print("Thanks for playing! :D")
    print("=" )

if __name__ == "__main__":
    main()