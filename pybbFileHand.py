#
#   File handling Python code
#
#

#print('Create a file and write to it')

#bbdirectory = r'C:\Users\brynb\Google Drive\My documents\BB SRC code\My Python libary\test'
from typing import List

BBSRCCODE = r'C:\Users\brynb\Google Drive\My documents\BB SRC code'

#BBfile1= bbdirectory + '\BBpytestfile1'

#BBfile1= bbdirectory + '\BBpytestfile1'
#BBfile2= bbdirectory + '\BBpytestfile2'
#BBfile3= bbdirectory + '\BBpytestfile3'

#f1 = open(BBfile1,'w')
#f2 = open(BBfile2,'w')
#f3 = open(BBfile3,'w')

#f1.write('This is File1\n')
#f1.write('This is line 100\n')
#f2.write('This is File 2\n')
#f2.write('This is line 200\n')
#f3.write('This is File 3\n')
#f3.write('This is line 300\n')
#f1.close()
#f2.close()
#f3.close()


#f1 = open(BBfile1,'r')
#f2 = open(BBfile2,'r')
#f3 = open(BBfile3,'r')

import os
#listdiris = os.listdir(bbdirectory)


ld = os.listdir(BBSRCCODE)
for flnm in ld :
    if flnm != ".metadata":
        print(flnm)

print('finished')



#print(BBfile1 + ' contents is:')
#print(f1.read())
#print(BBfile2 + ' contents is:')
#print(f2.read())
#print(BBfile3 + ' contents is:')
#print(f3.read())

#f1.close()
#f2.close()
#f3.close()


