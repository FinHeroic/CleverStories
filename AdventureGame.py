def main():
    print("Welcome to the Time Travel Adventure!")

    # Level 1
    print("You find yourself in front of a time machine with three buttons: PAST, PRESENT, and FUTURE.")
    choice1 = input("Which button do you press? ").lower()

    if choice1 == "past":
        # Level 2
        print("You are transported to the age of dinosaurs.")
        print("You see a T-REX, a VELOCIRAPTOR, and a BRACHIOSAURUS.")
        choice2 = input("Which dinosaur do you want to approach? ").lower()

        if choice2 == "t-rex":
            # Level 3
            print("The T-Rex notices you and starts to chase you!")
            print("You see a CAVE and a RIVER.")
            choice3 = input("Do you run to the CAVE or jump into the RIVER? ").lower()

            if choice3 == "cave":
                print("You manage to escape the T-Rex and find a hidden time machine. You safely return to your own time. Congratulations, you won!")
            elif choice3 == "river":
                print("You jump into the river and get swept away by the current. The T-Rex loses interest, but you're now stranded. Game over.")
            else:
                print("Invalid choice. Game over.")

        elif choice2 == "velociraptor":
            print("The Velociraptor sees you and quickly surrounds you with its pack. Game over.")
        elif choice2 == "brachiosaurus":
            print("The Brachiosaurus is peaceful and doesn't mind your presence. You spend some time observing it and then return to the time machine. Congratulations, you won!")
        else:
            print("Invalid choice. Game over.")

    elif choice1 == "present":
        print("You press the present button, but nothing happens. You're already in the present. Game over.")

    elif choice1 == "future":
        # Level 2
        print("You are transported to a futuristic city.")
        print("You encounter a group of friendly ROBOTS and a mysterious HOLOGRAM.")
        choice4 = input("Do you want to talk to the ROBOTS or investigate the HOLOGRAM? ").lower()

        if choice4 == "robots":
            # Level 3
            print("The robots explain that they have taken over most tasks in the city.")
            print("They offer you a chance to join their INTELLIGENCE NETWORK or return to your own time.")
            choice5 = input("Do you want to join the INTELLIGENCE NETWORK or RETURN to your time? ").lower()

            if choice5 == "intelligence network":
                print("You become part of the network and gain incredible knowledge. Congratulations, you won!")
            elif choice5 == "return":
                print("The robots help you return to your own time. Congratulations, you won!")
            else:
                print("Invalid choice. Game over.")

        elif choice4 == "hologram":
            print("As you investigate the hologram, a hidden security system detects your presence and traps you. Game over.")
        else:
            print("Invalid choice. Game over.")

    else:
        print("Invalid choice. Game over.")


if __name__ == "__main__":
    main()
