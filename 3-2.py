from itertools import permutations

# Define the possible colors
colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]

# Function to generate all possible permutations of color combinations
def generate_combinations():
    return list(permutations(colors, 4))

# Function to compare a guess with the solution
def compare_guess(guess, solution):
    correct_position = sum([1 if guess[i] == solution[i] else 0 for i in range(len(guess))])
    correct_color_wrong_position = sum([min(guess.count(c), solution.count(c)) for c in set(guess)]) - correct_position
    return (correct_position, correct_color_wrong_position)

# Example guesses and feedback
guesses = [
    (["Yellow", "Red", "Red", "Blue"], (0, 1)),
    (["Red", "Green", "Green", "Green"], (0, 0)),
    (["Blue", "Blue", "Blue", "Orange"], (0, 1)),
    (["Orange", "Yellow", "Yellow", "Yellow"], (3, 0)),
    (["Orange", "Yellow", "Yellow", "Purple"], (2, 1)),
    (["Orange", "Orange", "Yellow", "Yellow"], (2, 2))
]

# Generate all possible combinations
all_combinations = generate_combinations()

# Try to find the correct solution based on the guesses and feedback
for combination in all_combinations:
    match = True
    for guess, feedback in guesses:
        if compare_guess(guess, combination) != feedback:
            match = False
            break
    if match:
        print("Possible solution:", combination)
        break
print(all_combinations)