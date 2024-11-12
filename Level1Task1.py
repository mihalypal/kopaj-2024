def smallest_hole(input_string):
    dimensions = list(map(int, input_string.split(',')))
    sorted_dimensions = sorted(dimensions)
    return f"{sorted_dimensions[0]},{sorted_dimensions[1]}"

input_string = "6,1,0"
smallest_hole(input_string)