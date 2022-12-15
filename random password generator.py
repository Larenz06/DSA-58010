import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these :
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

characterList = ""

# Getting character set for password
while (True):
    choice = int(input("Pick a number "))
    if (choice == 1):

        # Adding letters to possible characters
        characterList += string.ascii_letters
    elif (choice == 2):

        # Adding digits to possible characters
        characterList += string.digits
    elif (choice == 3):

        # Adding special characters to possible
        # characters
        characterList += string.punctuation
    elif (choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    # Picking a random character from our
    # character list
    randomchar = random.choice(characterList)

    # appending a random character to password
    password.append(randomchar)

print("The random password is: " + "".join(password))

print('''Do you want to save the password? :
         1. Delete
         2. Save''')

passwordsave = ""

while (True):
    choice = int(input("Pick a number "))
    if (choice == 1):
        password.clear()
        break
    elif (choice == 2):
        p = open("password.txt", "a")
        p.write("\nThe random password is: " + "".join(password))
        p.close()

        p = open("password.txt", "r")
        print(p.read())
        break
    else:
        print("Please pick a valid option!")

