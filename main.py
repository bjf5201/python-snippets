
# Main module
#
# Purpose: Calls all modules in this section depending on user input
#
# Variables: option
#

def main():
  '''
  Asks the user which function they would like to see and then returns that function to them
  '''
# give options to User
print('-'*10+'Welcome'+'-'*10)
print('='*30)
print('-'*10+'Options'+'-'*10)
print('1) Dictionary')
print('2) Lab 8')
print('3) Phone Number')
print('4) Turtle')
option = int(input('Which function would you like to see? (Choose 1-4)'))
if option == 1:
  import dictionary
elif option == 2:
  import lab8
  option = int(input('Which function would you like to see? (Choose 1-4)'))
elif option == 3:
  import phoneNumber
  option = int(input('Which function would you like to see? (Choose 1-4)'))
else:
  import turtleLab
  option = int(input('Which function would you like to see? (Choose 1-4)'))


main()