# psuedocode for the login window.

attempts = 3

login fail = "please check if username and password is correct"

login success = go to next module

lock out = "you have been locked out. please contact technical support."

input USERNAME 

input PASSWORD


if (USERNAME == FILE:USERS.USERNAME && PASSWORD == FILE:USERS.PASSWORD) then:

    login success

else:

    Attempts = Attempts – 1

    login fail

if Attempts > 0:

    lock out

else:

    error message

    quit 
