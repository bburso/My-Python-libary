# comment

print("My first simple Python script!")
print("Just edited")

import sys

def write():

   name = input('Enter your name: \n')
   print('is this correct? ' + name)
   confirmation = input()

   while not (confirmation == 'Y' or confirmation == 'y') :
     name = input('Enter your name again please: \n')
     print('is this correct? ' + name)
     confirmation = input()


   age = input('That went well so enter your age: \n')
   print('So ' +name + " you are "+ age)

write()
sys.exit(0)
