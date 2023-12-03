import re


def validate_us_phone_number(phone_number):
    # Define the regular expression pattern for a US telephone number
    pattern = re.compile(r"^(\(\d{3}\)\s?|\d{3}-)\d{3}-\d{4}$")

    # Use the pattern to match the input phone number
    match = pattern.match(phone_number)

    # If there is a match, the phone number is valid
    if match:
        return True
    else:
        return False


# for Example:
phone_number = "(123) 456-7890"
if validate_us_phone_number(phone_number):
    print(f"The phone number {phone_number} is valid.")
else:
    print(f"The phone number {phone_number} is not valid.")
