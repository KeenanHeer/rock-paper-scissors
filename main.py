import random
import collections
import copy
from tabulate import tabulate
       

def rockPaperScissors():
    print("\n"*2)
    userinput = input("would you like rock , paper or scissors? ")
    gameOptions  = ['rock','paper','scissors']
    gameWinOptions =  ['paper','scissors','rock']
    randomIntegerGen = random.randint(0,len(gameOptions)-1)

    print(f'The computer guessed {gameOptions[randomIntegerGen]} and you guessed {userinput}')
    if userinput == gameOptions[randomIntegerGen]:
        print("3 points")
        return 3
    elif userinput == gameWinOptions[randomIntegerGen]:
        print('10 points')
        return 10
    else:
        print(f"0 points unlucky, the correct answer was {gameOptions[random.randint(0,len(gameOptions)-1)]}")
        return 0

def startGame():
    totalScore = 0
    for num in range(0,2):
        currentScore = rockPaperScissors()
        totalScore = totalScore + currentScore
        print(f'\n\n The total score is {totalScore}\n')

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
    print("\n"*2)
    age = input("What is your age?")
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
