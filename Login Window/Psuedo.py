# psuedocode for the login window.

attempts = 3

FAIL = "please check if username and password is correct"

SUCCESS = next module

LOCKOUT = "you have been locked out. please contact technical support."

ERROR MESSAGE = "there has been an error"

input USERNAME 

input PASSWORD


if (USERNAME == FILE:USERS.USERNAME && PASSWORD == FILE:USERS.PASSWORD) then:
    SUCCESS

else:
    Attempts = Attempts – 1
    FAIL

if Attempts > 0:
    LOCKOUT

else:
    ERROR MESSAGE
    QUIT

