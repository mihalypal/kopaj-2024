input = body
def findPlatform(arr, dep, passengers, n):
    plat_needed = 1
    result = 1
    max_passengers = passengers[0]  # Initialize with the passengers of the first train
    current_passengers = passengers[0]

    i = 1  # Start from the second train
    j = 0  # Start from the first departure

    while i < n and j < n:
        # If the next event is an arrival (train arrives before or at the same time the previous departs)
        if arr[i] <= dep[j]:
            plat_needed += 1
            current_passengers += passengers[i]
            max_passengers = max(max_passengers, current_passengers)
            i += 1  # Move to the next train arrival
        else:  # A train departs
            plat_needed -= 1
            current_passengers -= passengers[j]
            j += 1  # Move to the next train departure

        result = max(result, plat_needed)

    return result, max_passengers

var1 = [x[0] for x in input]
var2 = [x[1] for x in input]
passengers = [x[2] for x in input]

needed_platforms, max_passengers = findPlatform(var1, var2, passengers, len(var1))

#print(f"Minimum platforms required: {needed_platforms}")
#print(f"Maximum passengers at any time: {max_passengers}")

return [needed_platforms, max_passengers]
