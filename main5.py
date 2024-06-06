def check_id_valid(id_number):
    # Function to check the validity of an Israeli ID number
    # Takes an ID number as input and returns True if valid, False otherwise
    id_str = str(id_number)
    total = sum(int(digit) for digit in id_str[:-1])  # Sum of all digits except the last one (check digit)
    for i, digit in enumerate(id_str[:-1]):
        if (i + 1) % 2 == 0:  # Checking if the digit is in an even position
            total += sum(int(digit) for digit in str(int(digit) * 2))  # Doubling the digit and summing its digits
        else:
            total += int(digit)  # Summing the digit as is
    return total % 10 == 0  # Checking if the sum is divisible by 10 without remainder, indicating a valid ID


class IDIterator:
    def __init__(self, id_number):
        # Class representing an iterator that yields valid Israeli ID numbers
        # Initializes the iterator with the given ID number
        self.id_number = id_number + 1  # Initialize the next ID number to be checked

    def __iter__(self):
        # Function returning the iterator itself
        return self

    def __next__(self):
        # Function returning the next valid ID number in the range
        if self.id_number > 999999999:  # Checking if we reached the end of the range
            raise StopIteration
        while not check_id_valid(self.id_number):  # Checking for a valid ID number
            self.id_number += 1  # Continue checking numbers until a valid ID is found
        id_number = self.id_number
        self.id_number += 1  # Move to the next ID number to be checked
        return id_number


def id_generator(id_number):
    # Generator function yielding valid Israeli ID numbers
    id_number += 1
    while id_number <= 999999999:  # Checking all numbers in the range until the end
        if check_id_valid(id_number):  # Checking if the ID number is valid
            yield id_number
        id_number += 1  # Move to the next ID number to be checked


id_input = int(input("Enter ID: "))  # Getting input from the user for the ID number
type_input = input("Generator or Iterator? (gen/it)? ")  # Getting input for the type of access

if type_input == "it":
    id_iter = IDIterator(id_input)  # Creating an iterator
    for _ in range(10):
        print(next(id_iter))  # Printing 10 valid ID numbers using the iterator
elif type_input == "gen":
    id_gen = id_generator(id_input)  # Creating a generator function
    for _ in range(10):
        print(next(id_gen))  # Printing 10 valid ID numbers using the generator
else:
    print("Invalid input. Please enter 'gen' or 'it'.")  # Error message for invalid input
