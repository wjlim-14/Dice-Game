import os
import psphelper
import random

#Define both players' score
P1 = [None]*9
P2 = [None]*9
score = [P1, P2]

#Define total score
score1 = 0
score2 = 0
totalscore=[score1,score2]

#Define Input Option
def input_option():
    #Global variables
    global ans
    #Print option
    print("Input Option: ")
    print(" SAVE         : - Accept these dice.")
    print(" ROLL         : - Re-roll ALL dice.")
    print(" ROLL d1...dn : - Re-roll specified dice only.")
    print("")

    #User input option
    print("Input > ", end="")

    option = input("")
    #Generate all input as lowercase
    ans = option.lower()
    #Check error option
    error_option()

#Define Error Option
def error_option():
    global ans

    #Declare (save,roll)
    checkans = ["save", "roll"]
    #Check option
    while ans not in checkans:
        print("Error : Invalid Input")
        #User input
        print("Input > ", end="")
        option = input("")
        ans = option.lower()
            
#Define error desired
def choosecate():
    global turn,realdes,ctgy,totalscore,score
    j = True
    k = 0
    while j:
        desans = input("Enter your desired category: ")
        #Make ans2 to lowercase
        realdes = desans.lower()
        #Make a list for the category as stg
        catet = ["1s","2s","3s","4s","trio","quartet","band","doremi","orchestra"]
        add_cate = [Ones,Twos,Threes,Fours,Trio,Quartet,Band,Doremi,Orchestra]
        i = 0
        
        while realdes not in catet:
            print(f"ERROR: Category \"{realdes}\" does not exist.")
            desans = input("Enter your desired category: ")
            realdes = desans.lower()

        if turn % 2 != 0:
            while i < 9:
                if realdes == catet[i]:
                    if score[0][i] is None:
                        score[0][i] = add_cate[i]
                        totalscore[0] += add_cate[i]
                        j = False
                    else:
                        print(f"ERROR: Category '{realdes}' has been used.")        
                i += 1
        elif turn % 2 == 0:
            while i < 9:
                if realdes == catet[i]:
                    if score[1][i] is None:
                        score[1][i] = add_cate[i]
                        totalscore[1] += add_cate[i]
                        j = False
                    else:
                        print(f"ERROR: Category '{realdes}' has been used.") 
                i += 1


#Function to check category score
def dicecate():
     global Ones,Twos,Threes,Fours,Trio,Quartet,Doremi,Band,Orchestra
     
     Ones = 0
     Twos = 0
     Threes = 0
     Fours = 0
     Trio = 0
     Quartet = 0
     Doremi = 0
     Band = 0
     Orchestra = 0

#1S
     if 1 in dice:
        Ones = 1*dice.count(1)

#2S
     if 2 in dice:
        Twos = 2*dice.count(2)

#3S
     if 3 in dice:
        Threes = 3*dice.count(3)

#4S
     if 4 in dice:
        Fours = 4*dice.count(4)

#Trio
     trios=0
     while trios<5:
         if dice.count(trios)>=3:
             Trio = sum(dice)
         trios += 1

#Quartet        
     quartet = 0
     while quartet<5:
         if dice.count(quartet)>=4:
             Quartet = sum(dice)
         quartet += 1

#Band
     bands=0
     band=0
     while bands<5:
         if dice.count(bands)==3:
             while band<5:
                 if dice.count(band)==2:
                     Band = 30
                 band += 1
         bands += 1 
#Doremi
     if 1 in dice and 2 in dice and 3 in dice and 4 in dice:
         Doremi=20  

#Orchestra    
     orchestras=0
     while orchestras<5:
         if dice.count(orchestras) == 5:
             Orchestra = 40
         orchestras += 1 

###################################################################

#Clear Screen
psphelper.ClearScreen()

#Identify player turns
turn = 1
while turn < 19:

  #Show Title 
  title = "Battle Of The Sexes (B.O.T.S)"
  fillchar="="
  print(title.center(80,fillchar))

  #Show Scoreboard Interface
  names = ["Player 1", "Player 2"]
  subjects = ["1S", "2S", "3S", "4S", "Trio", "Quartet", "Band", "Doremi", "Orchestra"]
  psphelper.ShowTableByList("Scoreboard",names,subjects,score);

  #Show Total Score of Player1 & Player2
  
  print(f"Player 1: {totalscore[0]}")
  print(f"Player 2: {totalscore[1]}")
  print("")

  #Current Player
  if turn % 2 == 0:
        print("Player 2")
  else:
        print("Player 1")
  print("========")

  #Generate 5 random number / Roll Dice Prompt
  input("Press ENTER to roll dice.\n")

  #Roll 5 dice
  dice = []
  for i in range(0,5):
    auto = random.randrange(1,5)
    dice.append(auto)

  #Print result
  roll = 1
  print (f"Roll#{roll}: {dice}")
  print("")
  
  #Print table and show scores
  dicecate()
  ctgy = [[Ones,Twos,Threes,Fours,Trio,Quartet,Band,Doremi,Orchestra]]
  psphelper.ShowTableByList("Category Score",[],subjects,ctgy)


#Declare function to check user input option and error desired option
  input_option()
  if ans == "save":
    choosecate()

  elif ans == "roll":
    roll = 2
    while roll < 4:
      dice = []
      for i in range(0,5):
          auto = random.randrange(1,5)
          dice.append(auto)

      if ans == "save":
        break

      print(f"\nRoll# {roll}: {dice}\n")

      dicecate()
      ctgy = [[Ones,Twos,Threes,Fours,Trio,Quartet,Band,Doremi,Orchestra]]
      psphelper.ShowTableByList("Category Scores", [] , subjects , ctgy)
            
      #break the loop when roll reach three bcs each player only can re_roll 3 times
      if roll==3:
        break
      input_option()
      roll+=1
    choosecate()



  turn += 1

#Overall result and choose winner
#Option 1 : Winner Player 1
  if (score1 > score2 ):
     print("Player 1 wins !")
#Option 2 : Winner Player 2
  elif (score2 > score1):
     print("Player 2 wins !")
#Option 3 : Tie match
  else:
     print("It's a tie.")