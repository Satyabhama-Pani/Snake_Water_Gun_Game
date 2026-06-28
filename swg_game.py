'''
Snake Water Gun game
1 for snake
-1 for water
0 for gun
'''
# import modules
import random
import pyttsx3 as p
engine = p.init()

#  data 
choices = ["snake", "water", "gun"]
computer= random.choice(choices)

#  welcome note
print("\n" + "*"*40)
print(f"{"Welcome to Snake\U0001F40D Water\U0001F4A7 Gun\U0001F52B":^40}")
print("*"*40)
engine.say("Welcome to Snake water gun game")
engine.runAndWait()


# score of computer and player
your_score = 0
comp_score = 0
# main logic
choice = "yes"
while choice == "yes":

    # enter your choice and display
    you= input("Choose one among snake, water and game:")
    print(f"You choose {you}\nComputer choose {computer} ")
    engine = p.init()
    engine.say(f"you choose {you} and computer choose {computer}")
    engine.runAndWait()

    if(you.lower() not in choices):
        print("You choose wrong option !!!")
    elif(you == computer):
        print("Draw")
        your_score +=1
        comp_score +=1
    else:
        if( you== "snake" and computer=="water"):
            print("Win\U0001F389")
            engine.say("Congrats!! you win")
            your_score +=1
            engine.runAndWait()
        elif(you=="snake" and computer=="gun"):
            print("Loose\u274C")
            engine.say("You loose! try one more time")
            comp_score +=1
            engine.runAndWait()
        elif(you=="water" and computer=="snake"):
            print("Loose\u274C")
            engine.say("You loose! try one more time")
            comp_score +=1
            engine.runAndWait()
        elif(you=="water" and computer=="gun"):
            print("Win\U0001F389")
            engine.say("Congrats!! you win")
            your_score +=1
            engine.runAndWait()
        elif(you=="gun" and computer=="snake"):
            print("Win\U0001F389")
            engine.say("Congrats!! you win")
            your_score +=1
            engine.runAndWait()
        elif(you=="gun" and computer=="water"):
            print("Loose\u274C")
            engine.say("You loose! try one more time")
            comp_score +=1
            engine.runAndWait()
    choice = input("Do you want to continue? ").lower()
    
# scoreboard
print("\n"+"="*40)
print(f"{"Scoreboard\U0001F4CA":^40}")
print("="*40)
if your_score > comp_score:
    print(f"""\U0001F464Player: {your_score}\U0001F3C6
\U0001F4BBComputer: {comp_score}
""")
else:
    print(f"""\U0001F464Player: {your_score}
\U0001F4BBComputer: {comp_score}\U0001F3C6
""")
print("\n" + "*"*20 + " GAME ENDS " + "*"*20)