import json

def validate_credit_card(card_number):
    # Initialize the sum and a list for two-digit numbers
    total_sum = 0
    two_digit_numbers = set()  # Using set to store unique two-digit numbers
    
    # Ensure the card number is 16 digits long
    if len(card_number) != 16 or not card_number.isdigit():
        return json.dumps({"valid": False, "doubleDigitNumbers": []})
    
    # Iterate over each digit starting from the right (reverse index)
    for i in range(16):
        digit = int(card_number[15 - i])
        
        # Add two-digit numbers formed by adjacent pairs of digits
        if i > 0:
            two_digit = int(card_number[15 - i - 1] + card_number[15 - i])
            two_digit_numbers.add(two_digit)
        
        if i % 2 == 1:  # Every second digit (starting from the second-to-last)
            doubled = digit * 2
            if doubled > 9:
                total_sum += (doubled - 9)  # equivalent to subtracting 9
            else:
                total_sum += doubled
        else:
            total_sum += digit
    
    # Check if the total sum is divisible by 10
    is_valid = (total_sum % 10 == 0)
    
    # Return the JSON response
    return json.dumps({
        "valid": is_valid,
        "doubleDigitNumbers": sorted(list(two_digit_numbers))
    })

# Test the function with a sample input
credit_card_number = "1234567812345670"
print(validate_credit_card(credit_card_number))