import ast

def find_min_platforms_and_max_passengers(input_str):
    # Parse the input string to a list using ast.literal_eval for safety
    trains = ast.literal_eval(input_str)
    
    events = []
    
    # Split each train's arrival and departure into separate events
    for arrival, departure, passengers in trains:
        events.append((arrival, "arrival", passengers))
        events.append((departure, "departure", passengers))
    
    # Sort events: if times are the same, arrivals come before departures
    events.sort(key=lambda x: (x[0], x[1] == "departure"))
    
    max_platforms = 0
    max_passengers = 0
    current_platforms = 0
    current_passengers = 0
    
    # Process each event in sorted order
    for time, event_type, passengers in events:
        if event_type == "arrival":
            current_platforms += 1
            current_passengers += passengers
        else:
            current_platforms -= 1
            current_passengers -= passengers
        
        # Update the maximum platforms and passengers at any point in time
        max_platforms = max(max_platforms, current_platforms)
        max_passengers = max(max_passengers, current_passengers)
    
    return [max_platforms, max_passengers]

# Example input as a string:
input_str = "[ [900, 910, 10], [940, 1200, 20], [950, 1120, 30], [1100, 1130, 5] ]"

# Function call
find_min_platforms_and_max_passengers(input_str)
