import re


def validate_password(password):
    # Define the regular expression pattern for a 16-character alpha-numeric password
    pattern = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$"
    )

    # Use the pattern to match the input password
    match = pattern.match(password)

    # If there is a match, the password is valid
    if match:
        return True
    else:
        return False


# For Example:
password = "Abcd1234!@#$5678"
if validate_password(password):
    print(f"The password {password} is valid.")
else:
    print(f"The password {password} is not valid.")
