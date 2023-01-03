import string
import random
import smtplib

# email server credentials
EMAIL_ADDRESS = "dsapassgenv2@gmail.com"
EMAIL_PASSWORD = "acxxgqnoachegcpg"

while True:
  # Getting password length
  length = int(input("Enter password length: "))

  print('''Choose character set for password from these :
           1. Letters
           2. Digits
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
           2. Save
           3. Send via email''')

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
      elif (choice == 3):
          # email details
          TO_EMAIL = input("Enter your email(gmail only): ")
          SUBJECT = "The random password is"
          # create the email message
          message = f"Subject: {SUBJECT}\n\n{''.join(password)}"
          # send the email
          with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
              smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
              smtp.sendmail(EMAIL_ADDRESS, TO_EMAIL, message)
          print("Email sent successfully!")
          break
      else:
          print("Please pick a valid option!")

  # ask the user if they want to continue
  user_input = input("Do you want to generate another password? (Y/N) ")
  if user_input.lower() != "y":
    break
