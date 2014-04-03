#Computing Exam 2014

## Task 3a Questions

1. The function responsible for getting the players name is the GetPlayerName() function
2. To make sure that the name is asked for repeatedly I will put the input in a while loop and while the name is not valid it will ask for a name.
3. A boolean variable (accepted) which will store true if the name is accepted and false if otherwise. 

##Psuedo Code


FUNCTION GetPlayerName():
nameAccepted: Boolean
nameAccepted <- False

WHILE nameAccepted != True DO:
	INPUT PlayerName
	IF PlayerName != "" DO:
		nameAccepted <- True
	END IF
	ELSE DO:
		OUTPUT "Your name must not be left blank!"
	END ELSE
	
RETURN PlayerName
END FUNCTION