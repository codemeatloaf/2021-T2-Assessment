# Psuedocode for the login window.

import os

Attempts = 3

clear = lambda: os.system('cls')

print("enter username: ")
a1 = input()

print("enter password: ")
a2 = input()

if (a1 == FILE:USERS.USERNAME && a2 == FILE:USERS.PASSWORD) then:

    login success

    go to next module

else:

    Attempts = Attempts – 1

if Attempts > 0:

    LOGIN FAILED

    ERROR MESSAGE

    RETURN TO LOGIN WINDOW

else:

    ERROR MESSAGE

    quit()
