from collections import Counter

def get_feedback(guess, secret):
    correct_pos = sum(g == s for g, s in zip(guess, secret))
    guess_counter = Counter(guess)
    secret_counter = Counter(secret)
    correct_colors = sum((guess_counter & secret_counter).values())
    wrong_pos = correct_colors - correct_pos
    return [correct_pos, wrong_pos]

def is_valid_guess(guess, secret, feedback):
    return get_feedback(guess, secret) == feedback

def solve_mastermind(guesses_feedback):
    possible_colors = set()
    all_guesses = []
    all_feedbacks = []
    
    for guess, feedback in guesses_feedback:
        all_guesses.append(guess)
        all_feedbacks.append(feedback)
        possible_colors.update(guess)
    
    possible_combinations = []
    for c1 in possible_colors:
        for c2 in possible_colors:
            for c3 in possible_colors:
                for c4 in possible_colors:
                    possible_combinations.append([c1, c2, c3, c4])
    
    for combination in possible_combinations:
        valid = True
        for guess, feedback in zip(all_guesses, all_feedbacks):
            if not is_valid_guess(guess, combination, feedback):
                valid = False
                break
        if valid:
            return combination
    
    return None

def parse_input(input_str):
    guesses_feedback = []
    # Split the input string into parts (by lines)
    parts = input_str.strip().split("\n")
    
    for i in range(0, len(parts), 2):
        guess_str = parts[i].strip("[]")
        guess = guess_str.split(", ")
        feedback_str = parts[i+1].strip("[]")
        feedback = list(map(int, feedback_str.split(", ")))
        guesses_feedback.append((guess, feedback))
    
    return guesses_feedback

# Parse input and solve
guesses_feedback = parse_input(body)
solve_mastermind(guesses_feedback)

