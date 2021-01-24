import random
import collections
import copy
from tabulate import tabulate
NUMBER_OF_GAMES = 5

def rockPaperScissors():
    print("\n"*2)
    userinput = input("Choose out of the following options \n 1.rock \n 2.paper \n 3.scissors?")
    print("\n"*100)
    gameOptions  = ['rock','paper','scissors']
    gameWinOptions =  ['paper','scissors','rock']
    randomIntegerGen = random.randint(0,len(gameOptions)-1)

    print(f'\n The computer guessed {gameOptions[randomIntegerGen]} \n you guessed {userinput}')
    if userinput == gameOptions[randomIntegerGen]:
        print("\n3 points good effort\n")
        return 3
    elif userinput == gameWinOptions[randomIntegerGen]:
        print("\n10 points well done\n")
        return 10
    else:
        print(f"\n 0 points unlucky, \nThe correct answer was {gameOptions[random.randint(0,len(gameOptions)-1)]}\n")
        return 0

def startGame():
    totalScore = 0
    for num in range(0,NUMBER_OF_GAMES):
        currentScore = rockPaperScissors()
        totalScore = totalScore + currentScore
        print(f'\n\n The total score so far is {totalScore}\n but you can still improve')

        with open("newscore.txt","a") as myNewFile:
            myNewFile.write(str(currentScore)+",") 

    with open("newscore.txt","a") as myNewFile:
        myNewFile.write('\ntotalScore:' + str(totalScore)+"\n")


def getScores():
    scores = []
    with open('newscore.txt','r') as myNewFile:
        tempDictionaryValues = {}
        for lineIndex,line in enumerate(myNewFile):
            if((lineIndex+1) % 2 == 0 and (lineIndex+1) % 4 != 0 ):#This extracts the name
                tempDictionaryValues['name'] = line.split(';')[1].split(':')[1].replace('\n','')
            if((lineIndex+1) % 2 == 0 and (lineIndex+1) % 4 != 0 ):#This extracts the age
                tempDictionaryValues['age'] = line.split(';')[0].split(':')[1].replace('\n','')   
            if((lineIndex) % 2 == 0 and lineIndex % 4 != 0 ):
                arrayOfStrings = line.split(':')[1].replace('\n',"").split(',')
                score = []
                for index in range(len(arrayOfStrings)-1):
                    score.append(int(arrayOfStrings[index]))
                tempDictionaryValues['score'] = score.copy()
            if((lineIndex+1) % 4 == 0 ):#This extracts the total score
                scores.append((int(line.split(':')[1]),tempDictionaryValues.copy()))
                # data[int(line.split(':')[1])] = tempDictionaryValues.copy()
    return scores
      

def sortedData(data):
    data.sort(key=lambda  s:s[0],reverse=True)
    inAData = []
    for totalScore,scoreData in data:
        inAData.append([scoreData['name'],scoreData['age'],scoreData['score'],totalScore])
    print(tabulate(inAData, headers=['Name', 'Age','Scores','Total Score']))

def getNewUserData():
    name = input("What is your name?")
    print("\n"*50)
    age = input("What is your age?")
    print('\n'*50)
    with open("newscore.txt","a") as myNewFile:
        myNewFile.write("#################################\n")
        myNewFile.write("age:"+ age + ";name:" + name +"\n" + "Score:")


def main():
    #Menu code 
    howWouldYouLikeToPlay = ""
    while howWouldYouLikeToPlay != "X":
        howWouldYouLikeToPlay = input("Press any of the following for the appropraite actions: \n Z -> to play normally \n Y -> to view all scores \n X -> to quit the game \n").upper()
        print("\n"*50)
        if howWouldYouLikeToPlay == "Z":
            getNewUserData()
            startGame()
            print("\n"*1)
        elif howWouldYouLikeToPlay == "Y":
            scoreData = getScores()
            sortedData(scoreData)
            print("\n"*1)
            howWouldYouLikeToPlay = input("\nWould you like to go to the menu (X otherwise)...").upper()
            print("\n"*1)
        elif howWouldYouLikeToPlay == "X":
            break
        print("\n"*50)
    
main()
