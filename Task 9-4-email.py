# Email Validation
import re


def validate_email(email):
    pattern = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,4}"

    result = re.search(pattern, email)

    if result is not None:
        return True
    else:
        return False


print(validate_email("ruban@gmail.com"))
print(validate_email("ruban.com"))
print(validate_email("@gmail.com"))
