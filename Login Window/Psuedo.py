# psuedocode for the login window.

BEGIN

attempts = 3

FAIL = "Please check if username and password is correct"

SUCCESS = next module

LOCKOUT = "You have been locked out. please contact technical support."

ERROR MESSAGE = "There has been an error"

input USERNAME 

input PASSWORD


if (USERNAME == FILE:USERS.USERNAME && PASSWORD == FILE:USERS.PASSWORD) then:
    SUCCESS
    END

else:
    Attempts = Attempts – 1
    FAIL

if Attempts > 0:
    LOCKOUT
    END

else:
    ERROR MESSAGE
    QUIT
    END
