
import random
import os
import time

numbers = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_numbers():
    global numbers
    if not numbers:
        for _ in range(25):
            while len(numbers) < 25:
                random_number = random.randint(20, 70)
                if random_number not in numbers:
                    numbers.append(random_number)
                    
def check_bingo():
    for i in range(0, 25, 5):
        if all(numbers[i + j] == "X" for j in range(5)):
            return True
            
    for i in range(5):
        if all(numbers[i + j*5] == "X" for j in range(5)):
            return True
            
    if all(numbers[i] == "X" for i in [0, 6, 12, 18, 24]):
        return True
        
    if all(numbers[i] == "X" for i in [4, 8, 12, 16, 20]):
        return True
        
    return False

def display_grid(grid_size):
    bingo_letters = ["B ", "I ", "N ", "G ", "O "]

    print(f"", end='')
    for j in range(grid_size):
        print(f"| {bingo_letters[j]} ", end='')
    print("| ")
    print((grid_size * 4 + 4) * "-")

    for i in range(grid_size):
        print("", end='')
        for j in range(grid_size):
            index = i * grid_size + j
            print(f" {numbers[index]} |", end='')
        print("")
        print((grid_size * 4 + 4) * "-")

initialize_numbers()
playing = True
while playing:
    display_grid(5)

    called_number = random.randint(20, 70)
    
    start = time.time()
    
    choice = input(f"\nNumber {called_number}! If you have the number, please type it. If you don't, type nothing: ")

    end = time.time()

    clear()

    if (end - start) < 7:
        if choice.isdigit() and int(choice) in numbers:
            numbers[numbers.index(int(choice))] = "X"
            display_grid(5)
            if check_bingo():
                print("\nBINGO! You won!")
                playing = False
            else:
                clear()
    else:
        input("Too late! You only have 7 seconds to type. Press enter to continue.")

        clear()
        
