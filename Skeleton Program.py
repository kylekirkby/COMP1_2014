# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# This code should be used in conjunction with the Preliminary Material
# Written by the AQA Programmer Team
# Developed in the Python 3.2 programming environment
# Version 2 edited 06/03/2014

import random, datetime

ACE_HIGH = False

NO_OF_RECENT_SCORES = 3



class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ''

Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo):
  Rank = ''
  if ACE_HIGH == False:
    if RankNo == 1:
      Rank = 'Ace'
    elif RankNo == 2:
      Rank = 'Two'
    elif RankNo == 3:
      Rank = 'Three'
    elif RankNo == 4:
      Rank = 'Four'
    elif RankNo == 5:
      Rank = 'Five'
    elif RankNo == 6:
      Rank = 'Six'
    elif RankNo == 7:
      Rank = 'Seven'
    elif RankNo == 8:
      Rank = 'Eight'
    elif RankNo == 9:
      Rank = 'Nine'
    elif RankNo == 10:
      Rank = 'Ten'
    elif RankNo == 11:
      Rank = 'Jack'
    elif RankNo == 12:
      Rank = 'Queen'
    elif RankNo == 13:
      Rank = 'King'
  else:
    if RankNo == 1:
      Rank = 'Two'
    elif RankNo == 2:
      Rank = 'Three'
    elif RankNo == 3:
      Rank = 'Four'
    elif RankNo == 4:
      Rank = 'Five'
    elif RankNo == 5:
      Rank = 'Six'
    elif RankNo == 6:
      Rank = 'Seven'
    elif RankNo == 7:
      Rank = 'Eight'
    elif RankNo == 8:
      Rank = 'Nine'
    elif RankNo == 9:
      Rank = 'Ten'
    elif RankNo == 10:
      Rank = 'Jack'
    elif RankNo == 11:
      Rank = 'Queen'
    elif RankNo == 12:
      Rank = 'King'
    elif RankNo == 13:
      Rank = 'Ace'

  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit
def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  print()
  newChoice = Choice[0]
  newChoice = newChoice.lower()
  return newChoice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  print()
  nameAccepted = False
  
  while nameAccepted != True:
    PlayerName = input('Please enter your name: ')
    if PlayerName != "":
      nameAccepted = True
    else:
      print("Your name must not be blank!")
    
    print()
    
  return PlayerName

def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  newChoice = Choice.lower()
  yes = "y"
  no = "n"
  if newChoice == "y":
    return yes
  elif newChoice == "yes":
    return yes
  elif newChoice == "no":
    return no
  elif newChoice == "n":
    return no

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = ''

    
def BubbleSortScores(RecentScores):
  swapped = True
  listLength = len(RecentScores) + 1
  
  while swapped:
      listLength -= 1
      swapped = False
      for count in range(listLength):
          count + 1
          if RecentScores[count].Score > RecentScores[count + 1].Score:

              #temp values
            
              temp = RecentScores[count].Score
              tempName = RecentScores[count].Name
              tempDate = RecentScores[count].Date
              
              #Change Over
              
              RecentScores[count].Score = RecentScores[count + 1].Score
              RecentScores[count].Name = RecentScores[count + 1].Name
              RecentScores[count].Date = RecentScores[count + 1].Date
              
              RecentScores[count + 1].Score = temp
              RecentScores[count + 1].Name = tempName
              RecentScores[count + 1].Date = tempDate
              
              swapped = True
  return RecentScores


def DisplayRecentScores(RecentScores):

  RecentScores = BubbleSortScores(RecentScores)

  print(RecentScores)
  for each in RecentScores:
    print(each.Name,each.Date,each.Score)
    print()

    
  print()
  print('Recent Scores: ')
  print('{0:<10}{1:<10}{2:<10}'.format("Name","Score","Date"))

  for each in RecentScores:
    print('{0:<10}{1:<10}{2:<10}'.format(each.Name,each.Score,each.Date))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  choice = input("Do you wish to add your score to the results table?(y/n): ")
  choice = choice.lower()
  choice = choice[0]

  
  if choice == "y":
    add = True
  elif choice == "n":
    add = False
  else:
    add = False
    
  if add == True: 
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
        RecentScores[Count].Date = RecentScores[Count + 1].Date
      Count = NO_OF_RECENT_SCORES
      
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    CurrentDate = datetime.datetime.now()
    RecentScores[Count].Date = CurrentDate.strftime('%d/%m/%y')
def GetOptionChoice():
  ChoiceOption = False
  while ChoiceOption != True:
    choice = input("Please choose an option: ")
    if choice == "":
      print("Choice must not be blank!")
    else:
      choice = choice.lower()
      choice = choice[0]
      ChoiceOption = True

  return choice






def SetAceHighOrLow():
  global ACE_HIGH
  valid = False
  while valid != True:
    AceSetting = input("Do you want the Ace to be (h)igh or (l)ow: ")
    if AceSetting == 'h':
      
      ACE_HIGH = True
      valid = True
    elif AceSetting == 'l':
      ACE_HIGH = False
      valid = True
    else:
      print("Not a valid setting!")
  
def SetOptions(option):
  if option == '1':
    SetAceHighOrLow()
  else:
    print("Not a valid option!")

    
def DisplayOptions():
  print("OPTIONS MENU")
  print()
  print("1.Set Ace to be HIGH or LOW")
  ValidOption = False
  while ValidOption != True:
    NewChoice = GetOptionChoice()
    if NewChoice == '1':
      ValidOption = True
    else:
      ValidOption = False
      print("Please choose a valid option!")
  SetOptions(NewChoice)


def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())

  #Creates the recent score list
    
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())

    
  Choice = ''
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
    
