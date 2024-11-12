input = [[659, 678, 40], [441, 474, 67], [664, 690, 28], [1157, 1159, 44], [779, 800, 26], [388, 415, 19], [729, 761, 94], [114, 132, 11], [664, 677, 64], [292, 301, 69], [630, 657, 55], [738, 761, 3], [804, 831, 91], [1177, 1199, 89], [1044, 1069, 39], [348, 382, 12], [771, 794, 61], [355, 376, 81], [381, 386, 45], [624, 636, 36], [182, 216, 9], [1408, 1413, 82], [1082, 1118, 61], [71, 86, 97], [337, 361, 26], [38, 76, 43], [1255, 1291, 47], [685, 693, 43], [741, 771, 39], [1061, 1093, 11], [391, 417, 99], [1093, 1094, 46], [1248, 1252, 21], [740, 776, 93], [640, 647, 83], [497, 508, 19], [152, 159, 53], [1405, 1423, 50], [74, 74, 47], [580, 612, 5], [463, 485, 62], [671, 698, 5], [1193, 1217, 44], [1294, 1316, 95], [1401, 1416, 26], [807, 823, 86], [994, 1006, 4], [875, 882, 57], [1377, 1391, 34], [1090, 1121, 30], [241, 258, 18], [273, 278, 97], [1042, 1043, 72], [811, 825, 36], [927, 932, 51], [348, 382, 92], [58, 69, 13], [581, 589, 31], [90, 122, 51], [608, 621, 9]]

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

print([needed_platforms, max_passengers])
