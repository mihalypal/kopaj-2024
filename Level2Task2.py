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
input_str = "[[958, 985, 13], [1322, 1336, 70], [208, 227, 11], [253, 270, 88], [593, 628, 84], [410, 432, 78], [1152, 1152, 37], [272, 296, 69], [185, 221, 70], [987, 1010, 9], [872, 885, 17], [1279, 1290, 85], [578, 597, 55], [1283, 1318, 25], [837, 843, 72], [189, 224, 82], [1360, 1364, 85], [214, 246, 13], [906, 915, 75], [441, 444, 49], [870, 885, 61], [904, 931, 63], [1337, 1356, 87], [838, 850, 91], [713, 741, 57], [531, 554, 51], [23, 60, 53], [1329, 1335, 97], [1002, 1030, 2], [573, 603, 5], [866, 868, 57], [198, 216, 51], [9, 38, 4], [1392, 1423, 88], [934, 949, 49], [1000, 1028, 16], [93, 95, 98], [1214, 1252, 84], [181, 195, 4], [84, 98, 47], [313, 326, 41], [88, 114, 64], [828, 835, 40], [24, 48, 48], [753, 780, 88], [147, 147, 69], [441, 454, 45], [349, 352, 13], [770, 804, 54], [767, 789, 48], [145, 155, 44], [629, 657, 85], [1240, 1265, 73], [620, 638, 50], [744, 760, 52], [844, 881, 100], [113, 126, 14], [994, 995, 43], [946, 974, 85], [111, 125, 9]]"

# Function call
find_min_platforms_and_max_passengers(input_str)
