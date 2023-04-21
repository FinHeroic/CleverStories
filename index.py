# This program adds a few extra words to the story for creativity and fun.

def main():
    print("Please enter the following:\n")

    adjective = input("adjective: ")
    animal = input("animal: ")
    verb1 = input("verb: ")
    exclamation = input("exclamation: ")
    verb2 = input("verb: ")
    verb3 = input("verb: ")
    location = input("location: ")
    emotion = input ("emotion")

    exclamation = exclamation.capitalize()

    story = f"""The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family. Then, I saw it {verb1} towards the {location}. I couldn't believe my eyes. I felt so {emotion}."""

    print("\nYour story is:\n")
    print(story)


if __name__ == "__main__":
    main()
