import random
# BINs provided by the client
BIN_1 = [] # needs to be 6 ints separated by (,)
BIN_2 = [] # needs to be 6 ints separated by (,)
# Array to keep the new card number
card_number=[]

#Append the provided values 
#Add menu for BIN to be chosen 
card_number  = BIN_2 + card_number



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
        d = card_number[i] - 0
     
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
    #print(card_number)
    final = generate_visa_numbers(card_number)
    print('Final Number: ' + final)
    
    count = 0 
    valid_card = False
    while not valid_card:
        if (checkLuhn(final)):
            valid_card = True
            print("This is a valid card")
            
        else:
            valid_card = False
            count += 1
            #print(count)
            print(f'Failed: ', count, ' attempts', end='\r' )
     
    

#Print the card number generated 
#print(card_number)
#print(len(card_number))