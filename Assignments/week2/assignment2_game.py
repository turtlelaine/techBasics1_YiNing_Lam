import time

print("===")
print("13 Steps Till Dawn")
print("===")
time.sleep(1)
print("This story has 5 endings.")
time.sleep(1)
print("=")

print("An old notebook lies quietly on your bedside.")
print("You vaguely feel that it contains some important guidance...")
time.sleep(1.5)

while True:
    start = input('Please enter "Start" to open the notebook: ')
    if start == "Start":
        print("You opened the notebook...")
        time.sleep(1)
        break
    else:
        print("The notebook seems to be calling you. Please try again.")
        time.sleep(1.5)

notebook = []
repeat = 0
loop = 0
memory = None

while True:
    print("\n[ Step 1: Falling Asleep ]")
    print("===")
    time.sleep(1.5)

    print("You've suffering from insomnia for a long time. Your doctor recommended stopping use of phone one hour before sleep.")
    time.sleep(1.5)
    print("In a half-dream state, you received a phone call...")
    time.sleep(1)

    phone_loop = True
    while phone_loop:
        choice = input("Answer? (yes/no): ")
        if choice == "yes":
            repeat += 1
            print("You opened your phone but saw no missed calls.")
            time.sleep(1)
            print("You suspected you're hallucinating from exhaustion.")
            time.sleep(1)
            print("You saw a photo of the two of you on the screen, memories flooding in while tears run down your face.")
            time.sleep(1.5)

            if repeat >= 3:
                print("You're exhausted and mentally broke down.")
                print("You can no longer fall asleep, nor wake up.")
                print("[Bad Ending: Exhaustion]")

                retry = input('Do you want to wake up and try again? (Enter "retry" to restart / Enter "end" to quit): ')
                if retry == "retry":
                    print("You closed your eyes again...")
                    time.sleep(1.5)
                    repeat = 0
                    loop = 0
                    notebook = []
                    break
                else:
                    print("The notebook closes quietly , waiting to be opened again...")
                    exit()
            else:
                print("You couldn't sleep until dawn, the birds called you up.")
                time.sleep(1.5)
                print("You got out of bed for a drink and started another dazed day.")
                time.sleep(1.5)
                print("""After a tiring day, you got back home.
                you were extremely tired so you collapsed directly onto the bed.""")
                time.sleep(1.5)
                print("Just as you're about to fall asleep, another phone rings...")
        elif choice == "no":
            print("You didn't answer the phone. You fell into deep sleep.")
            time.sleep(1.5)
            phone_loop = False
        else:
            print('Please enter "yes" or "no".')
    if repeat >= 3:
        continue

    loop += 1
    print("===")
    print(f"\n[ Step 2: Observation ] (Cycle #{loop})")
    print("===")
    time.sleep(1.5)

    print("You entered a dream.")
    time.sleep(2)
    print("You looked around and found yourself on a rooftop.")
    time.sleep(2)
    print("\nA gentle breeze blown.")
    time.sleep(2)

    print("\n You saw him standing at the edge of the rooftop with his back facing you.")
    time.sleep(2)
    print("\nYour heart was pounding. You wanted to:")
    time.sleep(2)
    print("1. Slowly walk toward him")
    time.sleep(1)
    print("2. Stand still and watch him")
    time.sleep(1)
    print("3. Call his name")
    time.sleep(1)

    sunset = input("Choose 1, 2, or 3: ")

    if sunset == "1":
        print("\nYou walked toward him quietly, footsteps light, afraid to disturb him.")
        time.sleep(1)
        print("He didn't seem to notice you.")
        notebook.append("I chose to walk toward him, but could never reach.")
    elif sunset == "2":
        print("\nYou stood still, watching his back.")
        time.sleep(1)
        print("The wind lifted the corner of his clothes. You suddenly felt a deja-vu.")
        notebook.append("I stood still watching him, not getting closer.")
    else:
        print("\nYou tried to call his name.")
        time.sleep(1)
        print("The name got stuck in your throat, unable to come out.")
        notebook.append("I tried to call him, but something blocked my voice.")

    time.sleep(1.5)

    print("\nHe looked up at the sky. You followed his gaze and looked up as well.")
    time.sleep(2)
    print("The sunset was stunning. You felt a sense of peace.")
    time.sleep(2)
    print("You looked away.")
    time.sleep(2)
    print("He was gone.")
    time.sleep(2)
    print("A loud crash came below the building. Something deep in your soul crumbled.")
    time.sleep(2)

    print("\n[ Step 3: Recording ]")
    time.sleep(2)
    print("You saw him facing you with his back, seemingly trying to call someone, but no one answers.")
    time.sleep(2)
    dream_record = input("Please record this dream: ")
    notebook.append(dream_record)
    print("Recorded.")
    time.sleep(0.5)
    print("You rushed forward, trying to grab him, but heard a familiar yet rigid voice:")
    time.sleep(1)

    print("\n[ Step 4: Failure]")
    print('"You should go as fast as you can to the nearest building and jump from the rooftop."')
    time.sleep(1.5)

    if loop == 1:
        print("Yes, I am the one who should die. I must admit. I must pull him back. I must be responsible for it.")
        time.sleep(1.5)
        print("You should've been there. You should've been there. You should've been there. You should've been there.")
        time.sleep(1.5)
        print("I'm sorry.")
        time.sleep(1.5)
        print("You felt an unprecedented reality: falling, heart palpitations, sobbing, restlessness...")
        time.sleep(1.5)
        print('You also heard a faint voice: "...go back."')
    elif loop == 2:
        print("...This is all my fault.")
        time.sleep(1.5)
        print("If only I had answered the phone... if only I had noticed earlier...")
        time.sleep(2)
        print("You fell again, heart palpitating, sobbing, restless. It feels familiar, but something is missing.")
    elif loop >= 3:
        print("...")
        time.sleep(2)
        print("...You feel an unprecedented calm.")

    time.sleep(1.5)

    print("===")
    print("[ Step 5: Reset ]")
    print("===")
    time.sleep(1.5)

    if loop >= 3:
        print("Sorry.")
        time.sleep(1)
        print("I'm coming for you.")
        time.sleep(1.5)
        print("[Bad Ending: I'm coming for you.]")

        retry = input("Do you want to wake up and try again? (retry/end): ")
        if retry == "retry":
            print("You closed your eyes again.")
            time.sleep(1.5)
            print("The dream is reweaving...")
            time.sleep(1.5)
            loop = 0
            repeat = 0
            notebook = []
            continue
        else:
            print("The notebook quietly closes, waiting to be opened again...")
            break

    print("Please record your dream content.")
    print("Then, cover your sight and hearing with objects.")
    print("If you don't have any, try to ignore the noise during the reset and keep your eyes closed throughout.")
    print("The dream will begin resetting after full recording and sensory closure.")
    time.sleep(2)

    record = input("Please enter your dream record: ")

    if record == "":
        print("You didn't record anything...")
        time.sleep(1.5)
    elif record in notebook:
        notebook.append(record)
        print("Recording complete. The dream begins resetting...")
        time.sleep(1.5)
        print("You feel falling, heart palpitations, sobbing, restlessness... this is normal.")
        time.sleep(2)
        continue
    else:
        print("Your record doesn't match the dream. The reset is experiencing anomalies...")
        time.sleep(1.5)

    print("===")
    print("\n[ Step 6: Dimensional Descent ]")
    print("===")
    time.sleep(1.5)
    print("Your consciousness sinks into the dream due to hesitation.")
    time.sleep(2)
    print("Do not try to recall back.")
    time.sleep(2)

    print("\n[ Step 7: Pursuit ]")
    time.sleep(1.5)
    print("Please recall the clearest scene from your memory and begin pursuing 'him.'")
    print("The clarity of your memory will determine how close you can get to him in this dream.")
    time.sleep(1.5)

    print("\nYour notebook records:")
    #I asked deepseek for assisting this part. Just to see if I can make it more emotional.
    memoryRecord = []

    if loop >= 1:
        memoryRecord.append(("Sunset on the rooftop", "sunset"))
    if repeat >= 1:
        memoryRecord.append(("The missed phone call", "phone"))
    if len(notebook) > 0:
        record = notebook[-1][:30] + "..." if len(notebook[-1]) > 30 else notebook[-1]
        memoryRecord.append((f"Dream record: {record}", "dream"))

    if sunset == "1":
        memoryRecord.append(("The moment I walked toward him", "approach"))
    elif sunset == "2":
        memoryRecord.append(("Me standing still", "stay"))
    elif sunset == "3":
        memoryRecord.append(("The name I couldn't call out", "noname"))

    if len(memoryRecord) < 2:
        memoryRecord.append(("Blurry white figure", "shadow"))

    for i, (desc, _) in enumerate(memoryRecord, 1):
        print(f"{i}. {desc}")

    print(f"{len(memoryRecord) + 1}. Blank. I can't remember anything.")

    memory = input(f"\nChoose 1-{len(memoryRecord) + 1}: ")

    try:
        chosenNumber = int(memory) - 1
        if chosenNumber < len(memoryRecord):
            selectedNumber, memoryInput = memoryRecord[chosenNumber]
            print(f"You close your eyes and recall: {selectedNumber}")
            if memoryInput == "sunset":
                distance = "very close, almost within reach"
            elif memoryInput == "phone":
                distance = "a bit far, but you can see his silhouette"
            elif memoryInput == "dream":
                distance = "sometimes near, sometimes far, like through a fog"
            elif memoryInput == "approach":
                distance = "right in front of you, within arm's reach"
            elif memoryInput == "stay":
                distance = "neither far nor near, but you see him clearly"
            elif memoryInput == "noname":
                distance = "very close, but his face is blurry"
            else:
                distance = "you feel he's not far away"
            print(f"You feel he is {distance}.")
            notebook.append(f"I recalled: {selectedNumber}. He was {distance} from me.")
        else:
            print("\nYou chose blank. You can't remember anything.")
            print("He is far, far away, like a whole world apart.")
            distance = "far, far away"
            notebook.append("I couldn't remember anything. He was far from me.")
    except:
        print("\nYou hesitated too long. The memory begins to blur...")
        distance = "getting farther and farther"

    time.sleep(1.5)
    print("\nYou begin pursuing his figure...")
    time.sleep(1.5)

    print("\n[ Step 8 ]")
    print("It's all your fault.")
    time.sleep(0.3)
    print("\n[Step 8: Watch]")
    time.sleep(1.5)
    print("Let me see your face one more time.")
    time.sleep(1.5)

    print("\n[ Step 9: Diagnosis ]")
    time.sleep(1.5)
    print("All the guilt points to you.")
    time.sleep(0.5)
    print("You are the one who should die. You are th")
    time.sleep(0.3)
    print("[ Step 9: Judgment ]")
    time.sleep(1.5)
    print("Recall why you entered this dream.")
    time.sleep(2)

    print("A stronger wave of dizziness hits you. You can't move. You feel like you're being held down by a ghost.")
    time.sleep(1.5)
    print("If only I could die here...")
    time.sleep(2)

    print("=")
    print("\n[ Step 10: Awakening ]")
    print("=")
    time.sleep(1.5)

    print("Congratulations. You slept well. You've finally returned to the real world.")
    time.sleep(1)
    print("""""Hey, wake up. You're going to be late.""""")
    time.sleep(1)
    print("You opened your eyes and saw him waking you up.")
    time.sleep(1.5)

    print('"Wow, I had a nightmare..." You wanted to tell him what you dreamed.')
    print('"I saw a beautiful sunset on the rooftop, but then—"')
    time.sleep(1.5)
    print("Your voice stopped suddenly. He looked at you confused.")
    time.sleep(1)
    print("You realized you can't remember anything from this dream.")
    time.sleep(1.5)
    print('"Never mind."')
    time.sleep(1.5)

    print("You return to the warm, ordinary days like before.")
    print("You feel happy being back in those warm, ordinary days.")
    print("You're really home.")
    time.sleep(3)
    print("You woke up successfully.")
    time.sleep(3)

    print("The end.")
    time.sleep(10)

    daily = input("Do you want to end the record? (yes/no): ")

    if daily != "no":
        print("You close the notebook and choose to continue this life.")
        print("[Normal Ending: Unchanging Daily Life]")
        print("=")
        print("Thank you for playing.")
        print("=")
        break

    print("You look around at your surroundings.")
    time.sleep(1)
    print("Sunset, the clock ticking, even the birdsong is just right.")
    time.sleep(1.5)
    print("You're content with this peaceful life, living like this for a while.")
    time.sleep(1.5)
    print("You realized you've forgotten what day it is, so you went to check the time.")
    time.sleep(1)

    print("The clock's hand landed 'just right' on the time you were thinking of.")
    time.sleep(1.5)
    print('"The next second, birds should be flying by," you thought.')
    print("You're proud of yourself for predicting it perfectly.")
    time.sleep(1.5)
    print("Until a flock of sparrows actually flew by outside.")
    time.sleep(1.5)

    print("You started feeling uneasy...")
    time.sleep(1)
    print("The TV's plot was always 'just right' — exactly what you were thinking.")
    time.sleep(1)
    print("The scent of food was always 'just right' — exactly what you were craving.")
    print("Even the moment he appeared was 'just right' — exactly when you thought of him.")
    time.sleep(2)

    print("Everything was too perfect to be real.")
    time.sleep(1.5)

    print("You lowered your head and saw your previous record.")
    time.sleep(1)
    print("You remembered the dream, remembered every moment with him — and remembered his death.")
    time.sleep(2)

    print("=")
    print("\n[ Step 5: Reset ]")
    print("=")
    time.sleep(1.5)
    print("Yeah. ")
    time.sleep(1)
    print("I don't deserve to live.")
    time.sleep(1.5)
    print("Please authorize to reset the dream record.")

    reset = input("> ")

    if reset != "":
        print("You authorized to start over. The dream is about to begin again...")
        time.sleep(1.5)
        continue

    print("You hesitated.")
    time.sleep(1)
    print("You heard all the voices at one millisecond.")
    time.sleep(1)
    print("All the sirens, crowd, lights came back to your mind.")
    time.sleep(1)
    print("'I shouldn/'t be...'")
    time.sleep(1)
    print("Someone came by.")
    time.sleep(1)

    print("\n[ Step 11 ]")
    time.sleep(0.5)
    print('"Don\'t listen. Don\'t look. Don\'t remember this place."')
    time.sleep(1)
    print("He covers your ears.")
    time.sleep(1)
    print('"I\'m here."')
    time.sleep(1.5)
    print("But you could still hear his voice clearly.")
    time.sleep(2)
    print("After a strong fluctuation, you entered an void.")
    time.sleep(1.5)
    print("He stood before you, unharmed.")
    time.sleep(1)
    print("'You...'")
    time.sleep(1)
    print('"Hi."')
    time.sleep(1)
    print('"Time is running out..."')
    time.sleep(1.5)
    print("You remember everything. An overwhelming sense of guilt chokes you with coldness.")
    time.sleep(2)
    print("'I\'m sorry, I\'m sorry I didn\'t answer your phone. I should have noticed earlier...'")
    time.sleep(1)
    print('"I should have caught you. I should have..."')
    time.sleep(0.5)

    print("He holds you tightly, catching your tears.")
    print("You feel a warmth that you haven't felt in a long time.")
    time.sleep(2)

    print('"I\'m sorry."')
    time.sleep(1.5)
    print("The world started to fade.")
    time.sleep(1.5)
    time.sleep(0.2)
    print("The dream evaporates before your eyes.")
    time.sleep(5)
    print("You heard his voice from the deepest of your soul.")
    time.sleep(5)
    print('"I love you."')
    time.sleep(5)

    print("\n[ Step 12: Dream's End ]")
    time.sleep(1.5)

    print("You're woken by your alarm and birdsong. You find tears dried on your face.")
    time.sleep(1.5)
    print("You try to recall what the dream's about, but it feels blurry.")
    time.sleep(1.5)
    print("You give up recalling it like you give up your math exam.")
    time.sleep(1)

    print("You take a look at today's date.")
    time.sleep(0.5)
    print("It feels like you've slept for an incredibly long time, but only one night has passed.")
    time.sleep(2)

    print("On the way to school, you mindlessly scroll through short videos on social media.")
    time.sleep(1.5)
    print("You tap to share. His avatar still sits at the top of your share list.")
    time.sleep(1.5)

    print("You miss him a little.")
    time.sleep(1.5)
    print("You're a little annoyed, complaining to yourself that you think of him so often, yet he hasn't visited your dreams for even once.")
    time.sleep(2)

    print("But it's okay.")
    time.sleep(3)
    print("You believe that living your life is the only way you can be proudly see him again.")
    time.sleep(2)

    print("[True Ending: See you again]")
    time.sleep(3)
    print("[Step 13: Dawn]")
    time.sleep(3)
    print("\nThank you for playing.")
    time.sleep(2)
    print("If you enjoyed this story, here's the adapted short film directed by me: https://youtu.be/Sh820Sh9ffQ?si=6FQyPpZEB1UWHIoN")
    print("I hope you enjoyed them as much as I did :D")
    print("See ya")
    break
