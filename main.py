import random


def roll_dice():
    num_dice = int(input("Enter the number of dice to roll: "))
    dice_results = []

    for _ in range(num_dice):
        dice_roll = random.randint(1, 6)
        dice_results.append(dice_roll)

    return dice_results


def display_results(dice_results):
    print("Dice roll results: ", end="")
    print(*dice_results, sep=", ")


def main():
    while True:
        dice_results = roll_dice()
        display_results(dice_results)

        choice = input("Roll again? (y/n): ")
        if choice.lower() != "y":
            break


if __name__ == "__main__":
    main()
