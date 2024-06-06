import string

# Custom exceptions
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, character):
        super().__init__(f"The username contains an illegal character: '{character}'")


class UsernameTooShort(Exception):
    def __init__(self):
        super().__init__("Username is too short (must be between 3 and 16 characters)")


class UsernameTooLong(Exception):
    def __init__(self):
        super().__init__("Username is too long (must be between 3 and 16 characters)")


class PasswordMissingCharacter(Exception):
    def __init__(self, missing_char):
        super().__init__(f"The password is missing a character ({missing_char})")


class PasswordTooShort(Exception):
    def __init__(self):
        super().__init__("Password is too short (must be at least 8 characters)")


class PasswordTooLong(Exception):
    def __init__(self):
        super().__init__("Password is too long (must be at most 40 characters)")


def check_input(username, password):
    # Check username
    if not all(char in string.ascii_letters + string.digits + '_' for char in username):
        raise UsernameContainsIllegalCharacter(username)
    if len(username) < 3:
        raise UsernameTooShort()
    if len(username) > 16:
        raise UsernameTooLong()

    # Check password
    if not any(char.isupper() for char in password):
        raise PasswordMissingCharacter('Uppercase')
    if not any(char.islower() for char in password):
        raise PasswordMissingCharacter('Lowercase')
    if not any(char.isdigit() for char in password):
        raise PasswordMissingCharacter('Digit')
    if not any(char in string.punctuation for char in password):
        raise PasswordMissingCharacter('Special')
    if len(password) < 8:
        raise PasswordTooShort()
    if len(password) > 40:
        raise PasswordTooLong()

    print("OK")


def main():
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            check_input(username, password)
            break  # If input is valid, exit loop
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong, PasswordMissingCharacter,
                PasswordTooShort, PasswordTooLong) as e:
            print(e)


if __name__ == "__main__":
    main()
