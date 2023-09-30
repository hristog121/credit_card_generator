import random

# Pre-defined BIN number for the different cards
BIN_VISA = [4, 5, 3, 9]
BIN_Master = [5, 1, 0, 5]
BIN_AMEX = [3, 4,8,2]
card_number = []

# Initial empty lists
card_number_visa = []
card_number_master = []
card_number_amex = []

# Append the BINs
card_number_visa = BIN_VISA + card_number_visa
card_number_master = BIN_Master + card_number_master
card_number_amex = BIN_AMEX + card_number_amex




# Generate card Numbers VISA & Mastercard & AMEX
# This is the number after the BIN untill position 15
# Also it calculates the check digit and appends it to the first 15
def generate_numbers_rest(card_number_2):
    # print(card_number_2)
    z = 0
    y = 0
    multiplied_by_two = []

    new_number = ''

    for i in range(len(card_number_2) - 1, 15):
        rand_num = random.randint(0, 9)
        card_number_2.append(rand_num)
    # print(card_number_2)

    for i in card_number_2[0:16:2]:
        i *= 2
        if len(card_number_2) == 2:
            for x in i:
                y += x

            i = y
        multiplied_by_two.append(i)
        y = 0

    remaining_numbers = []
    for i in card_number_2[1:15:2]:
        remaining_numbers.append(i)

    # Luhn's algorithm - generate last digit
    last_digit = ((sum(multiplied_by_two) + sum(remaining_numbers)) * 9) % 10

    for i in card_number_2:
        new_number += str(i)

    return new_number
    # print('New Number: ' + new_number)

# Lugn algorithm for the check digit (last in the number)
def checkLuhn(card_number):
    nDigits = len(card_number)
    nSum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(card_number[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False


# Driver code
if __name__ == "__main__":

    # Menu for the user
    menu = """Please select one of the following options:
                1) Generate VISA card.
                2) Generate MASTER card.
                3) Generate AMEX card.
                4) Verify if existing card is valid."""
    welcome = "Lets do some cards: "

    # Print the menu on the CLI
    print(menu)

    # Initialize the counter for failed attempts
    count = 0

    #Take the user input
    user_input = input()
    if user_input == '1':
        print('Generating VISA')
        generate_numbers_rest(card_number_visa)
        # Convert the array to a string
        new = ''.join(map(str, card_number_visa))
        print('Visa card number: ' + new)
        print('Checking validity.....\n')
        not_valid = True
        while not_valid:
            if checkLuhn(new):
                print("The card is valid!")
                break
            else:
                count += 1
                print(f'Failed: ', count, ' attempts', end='\r')
                new = generate_numbers_rest(card_number_visa)

    elif user_input == '2':
        print('Generating MASTER')
        generate_numbers_rest(card_number_master)
        # Convert the array to a string
        new = ''.join(map(str, card_number_master))
        print('Visa card number: ' + new)
        print('Checking validity.....\n')
        not_valid = True
        while not_valid:
            if checkLuhn(new):
                print("The card is valid!")
                break
            else:
                count += 1
                print(f'Failed: ', count, ' attempts', end='\r')
                new = generate_numbers_rest(card_number_master)

    elif user_input == '3':
        print('Generating AMEX')
        generate_numbers_rest(card_number_amex)
        
        # Convert the array to a string
        new = ''.join(map(str, card_number_amex))
        print('Visa card number: ' + new)
        print('Checking validity.....\n')
        not_valid = True
        while not_valid:
            if checkLuhn(new):
                print("The card is valid!")
                break
            else:
                count += 1
                print(f'Failed: ', count, ' attempts', end='\r')
                new = generate_numbers_rest(card_number_amex)
    elif user_input == '4':
        card_from_user = input('Enter your card number: ')
        if checkLuhn(card_from_user):
            # valid_card = True
            print("This is a valid card: " + card_from_user)
        else:
            # Display the number of failed attempts
            count += 1
            print(f'Failed: ', count, ' attempts', end='\r')

