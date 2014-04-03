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

##Question 3b - Adding your score to the high score table

1. The function which is responsible for adding the scores to the table is the UpdateRecentScores() function

## Task 5 - Date of recent scores

1. The datetime module will need to be imported to use the date/time functions in python.
2. The four functions that will need to be changed for the date to be added is the DisplayRecentScores, UpdateRecentScores, ResetRecentScores and adding a attribute to the TRecentScore class (record)
3. To convert a string to a datetime object you need to use the strptime function within the datetime module - "time.strptime("30 Nov 00", "%d %b %y")"

##Additional Task - Variable Roles

### Variable Roles

#### Fixed Value 
A value that does not change and has a fixed value. E.g. a constant like the number of Recent scores to display - "NO_OF_RECENT_SCORES"
#### Stepper 
A stepper variable keeps count of the number of iterations currently completed and can be used to identify which iteration the loop is currently on. E.g in this program an
example would be the Count Variable used in the displayRecentScores function. 

#### Most Recent Holder

#### Most wanted holder

#### Gatherer

#### Transformation

#### Follower

#### Temporary
