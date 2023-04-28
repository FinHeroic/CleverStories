def main():
    print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")
    choice = input().upper()

    if choice == "MATCH":
        print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?")
    elif choice == "FLASHLIGHT":
        print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
    else:
        print("Invalid choice. Please choose MATCH or FLASHLIGHT.")

if __name__ == "__main__":
    main()
