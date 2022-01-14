import csv
import re

print("Welcome to SMS abbreviation Translator")
print("A Basic Slang Translator Program")
print("Remember not to use any void character in continuation")

print('===================================================')

def translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    for _str in user_string:

        fileName = "D:\\All\\Projects\\SlangTrans\\slang.txt"

        accessMode = "r"
        with open(fileName, accessMode) as myCSVfile:
            
            dataFromFile = csv.reader(myCSVfile, delimiter="=")

            _str = re.sub('[^a-zA-Z0-9-_.]', '', _str)
            for row in dataFromFile:

                if _str.upper() == row[0]:

                    user_string[j] = row[1]
            myCSVfile.close()
        j = j + 1

    print(' '.join(user_string))
    print('===================================================')
    print('')

while True:
    print("Provide Input below or print exit or EXIT to end script")

    user = input()

    if user.upper() == 'EXIT':
        print("Exiting Script")
        break
    translator(user)