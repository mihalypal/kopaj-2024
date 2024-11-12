def find_platform_and_max_passengers(body):
    # Convert trains list into events with timestamps
    events = []
    for arrival, departure, passengers in body:
        # Add arrival event (1 for arrival)
        events.append((arrival, 1, passengers))
        # Add departure event (-1 for departure)
        events.append((departure, -1, -passengers))
    
    # Sort events by time
    events.sort()
    
    current_platforms = 0
    current_passengers = 0
    max_platforms = 0
    max_passengers = 0
    
    # Process events in chronological order
    for time, event_type, passenger_change in events:
        if event_type == 1:  # Arrival
            current_platforms += 1
            current_passengers += passenger_change
        else:  # Departure
            current_platforms -= 1
            current_passengers -= -passenger_change
            
        max_platforms = max(max_platforms, current_platforms)
        max_passengers = max(max_passengers, current_passengers)
    
    return [max_platforms, max_passengers]