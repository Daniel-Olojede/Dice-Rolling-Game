import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

def main():
    while True:
        try:
            num_of_dice = int(input("How many dice would you like to roll? "))
            if num_of_dice <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    dice = []
    total = 0

    for _ in range(num_of_dice):
        dice.append(random.randint(1, 6))

    # Print dice side by side
    for line in range(5):
        for die in dice:
            print(dice_art[die][line], end="  ")
        print()

    for die in dice:
        total += die

    print(f"\nTotal: {total}")

if __name__ == "__main__":
    main()
