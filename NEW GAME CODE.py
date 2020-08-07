import time
uname = input("Hello, Please enter the name you want to use : " )
print("Hello! ", uname + ".")

question = str(input("Do you want to play a game?[Y/N]"))
Cyes = 'Y'
Syes = 'y'
Cno = 'N'
Sno = 'n'
#Conditional Code! It evaluates the answer given by the user.
if question == Cno or Sno:
    print("Oh Okay. Don't Play!")
else:
    time.sleep(0.1)    
if question == Cyes or Syes:
    print ("Great! Let's play.")
else:
    time.sleep(0.1)
time.sleep(2)
