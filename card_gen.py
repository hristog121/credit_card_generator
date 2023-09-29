import random
import sys

# BINs provided by the client
BIN_1 = [4,0,2,0,0,7] # needs to be 6 ints separated by (,)
BIN_2 = [] # needs to be 6 ints separated by (,)
# Array to keep the new card number
card_number=[]

#Append the provided values 
#Add menu for BIN to be chosen 
card_number  = BIN_1 + card_number



def generate_visa_numbers(card_number_2):
    #print(card_number_2)
    z = 0
    y = 0
    multiplied_by_two = []

    new_number = ''


    for i in range (0,9):
        rand_num = random.randint(0,9)
        card_number_2.append(rand_num)
    #print(card_number_2)    

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
    
    # Luhn's algorithm
    last_digit = ((sum(multiplied_by_two) + sum(remaining_numbers)) * 9) % 10

    for i in card_number_2:
        new_number += str(i)
        
    return new_number
    #print('New Number: ' + new_number)




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
if __name__=="__main__":
    menu = """Please select one of the following options:
                1) Generate VISA card.
                2) Generate MASTER card.
                3) Generate AMEX card.
                4) Verify if existing card is valid-

                Your selection: """
    welcome = "Lets do some cards: "
    print(menu)

    user_input= sys.argv[0]

    if user_input == '1':
        print('Input 1')


    # print(card_number)
    # final = generate_visa_numbers(card_number)
    # print('Final Number: ' + final)
    #
    # count = 0
    # valid_card = False
    # while not valid_card:
    #     if (checkLuhn(final)):
    #         valid_card = True
    #         print("This is a valid card: " + final)
    #
    #     else:
    #         valid_card = False
    #         count += 1
    #         #print(count)
    #         print(f'Failed: ', count, ' attempts', end='\r' )
    #
    #

#Print the card number generated 
#print(card_number)
#print(len(card_number))