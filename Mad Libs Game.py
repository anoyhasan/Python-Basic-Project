name = input("Enter a name : ")
place = input("Enter a place : ")
adjective = input("Enter a adjective : ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
story = (
    f"One day, {name} went to {place}. "
    f"There, they saw a very {adjective} {animal}. "
    f"{name} decided to {verb} with it. "
    f"It was the best day ever!"
)
print("\nHere’s your Mad Libs story:\n")
print(story)