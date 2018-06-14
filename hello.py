#
#   First Python code
#
#

print("My first simple Python script!")
print ("1+2+4 =") 
print (+1+2+4);
import sys

def write():
   
    name = input('Enter your name: ');# Name
    print('is this correct? ' + name);

    try:
        print('That went well?');
        age = input('so enter your age: ');  
        print('So ' +name + " you are "+ age);
    except:
        print('Something went wrong! Can\'t tell what?')

write()
sys.exit(0)
