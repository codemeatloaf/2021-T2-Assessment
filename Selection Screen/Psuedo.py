# Psuedocode for selection screen

BEGIN

FAILURE = "you do not have the permissions for that option"
SUCCESS = next module

input SELECTION

if (SELECTION == FILE:USERS.USERPERMISSIONS) then:
    SUCCESS
    END

else: 
   FAILURE 
   END