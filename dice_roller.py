import random
import time
import os

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_dice():
    input("🎲 Press Enter to roll the dice...")
    print("Rolling", end='', flush=True)
    
    # Suspense animation
    for _ in range(3):
        time.sleep(0.5)
        print('.', end='', flush=True)
    time.sleep(0.5)

    result = random.randint(1, 6)
    print(f"\n\n🎉 You rolled a {result}!")

if __name__ == "__main__":
    while True:
        clear_screen()
        roll_dice()
        again = input("\nDo you want to roll again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break
