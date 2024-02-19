import random

MAX_DIGITS = 7              # Max digits
START = 0                   # Start of random number range
END = 9                    # End of random number range

# main function
def main():
    # Create a list
    numbers = [0] * 7
    # Populate the list with random numbers
    for index in range(MAX_DIGITS):
        numbers [index] = random.randint(START, END)
        # Display the random numbers
        print('Hello, here are your lottery numbers:')
        for index in range(MAX_DIGITS):
            print(numbers[index], end = '')
        print()
# Calling main
main()
