import re


def validate_mobile_number(number):
    # Regular expression for a valid mobile number in Bangladesh
    # Assumes a 11-digit number starting with 01 or +8801
    pattern = r"^(?:\+8801|01)[3-9]\d{8}$"

    # Use the re.match() function to search the string for a match
    match = re.match(pattern, number)

    # Check if the match object is not None (indicating a match)
    if match:
        return True
    else:
        return False


# Example usage:
mobile_number_to_check = "+801712345678"
if validate_mobile_number(mobile_number_to_check):
    print(f"{mobile_number_to_check} is a valid mobile number for Bangladesh.")
else:
    print(f"{mobile_number_to_check} is not a valid mobile number for Bangladesh.")
