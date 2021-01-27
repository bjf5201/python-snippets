# Lab 18
# Bethany Fannin
# CSC 131-007
# Purpose: To practice programing with dictionary data type. Create a program that takes in a phone number with
# letters and returns the corresponding numerical phone number.
#
# Variables: valid_num, phone_num, phone_spell, phone_keys, phone_string, return_string, beg_string, char, terminate, response

def getPhoneSpell():
    """
        Return entered phone spell in the form 123-456-abcd
        and check it is in valid form
        for example:
        - the length of the input must be exactly 12 characters
        - the fourth and eighth characters must be '-'
        - the first three characters must be numbers (e.g., 123)
        - the fifth-seventh characters must be numbers (e.g., 456)
        - the ninth-twelfth characters must be letters (e.g., abcd)
        
        - hint: you can use any of the following functions
            - isdigit()
            - isalpha()
            - len()
    """
    valid_num = False

    # prompt for phone number

    while not valid_num:
        phone_num = input('Enter a phone number in the form of 123-4567-abcd, choosing your own numbers and letters: ')

        # check if valid form
        if len(phone_num) != 13 or phone_num[3] != '-' or phone_num[8] != '-':
            print("Invalid entry - Must be in the form of xxx-xxxx-xxxx")
        elif not phone_num[:3].isdigit() or not phone_num[4:7].isdigit():
            print("Invalid entry - The first eight characters must be integers plus one dash, ie 123-4567")
        elif not phone_num[9:].isalpha():
            print("Invalid entry - The last four characters must be letters.")
        else:
            valid_num = True
    return phone_num
    
def displayPhoneNumber(phone_spell):
    """ Display the possible phone number with the last four
        character replaces with the corresponding number from
        the phone keys.
        print the phone number.
        
        Search: The standard 12-key telephone keypad,
                character layout follows the ITU E.161 standard
                or look at the keypad on your phone.        
        Example: 123-456-abcd becomes 123-456-2223

        - hint: you don't need to change any of the first eight
                characters. You only need to convert the last
                four letters to numbers and then print the full
                phone-number.
                you can use string slicing and concatination to
                create the phone number.
    """
    phone_keys = {'a':2, 'b':2, 'c':2, 'd':3, 'e':3, 'f':3, 'g':4, 'h':4, 'i':4, 'j':5, 'k':5, 'l':5, 'm':6, 'n':6, 'o':6,
    'p':7, 'q':7, 'r':7, 's':7, 't':8, 'u':8, 'v':8, 'w':9, 'x':9, 'y':9, 'z':9}

    phone_string = phone_spell[8:]
    return_string = ''
    for char in phone_string:
        if char in phone_keys:
            return_string += str(phone_keys[char])
    beg_string = phone_spell[:8]
    print(beg_string + return_string)
            
        
    

def main():

    # Program welcome
    print('-'*51)
    print('This program allows the user to enter a spelled')
    print('phone number for the last four digits and generates')
    print('the phone number that produces that spelling')
    print('-'*51)

    # get phone number and display spelling
    terminate = False

    while not terminate:
        phone_spell = getPhoneSpell()
        displayPhoneNumber(phone_spell)

        # Continue
        response = input('\nEnter another phone spell? (y/n): ')
        if response.lower() == 'n':
            terminate = True


main()


