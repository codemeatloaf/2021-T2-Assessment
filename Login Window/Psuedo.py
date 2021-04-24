# Psuedocode for the login window.

Attempts = 3

input USERNAME 

input PASSWORD

if (USERNAME == FILE:USERS.USERNAME && PASSWORD == FILE:USERS.PASSWORD) then:

    login success

    go to next module

else:

    Attempts = Attempts – 1

if Attempts > 0:

    login fail

    error message

    return to login

else:

    error message

    quit
