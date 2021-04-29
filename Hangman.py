import string
import random

def hangman():
    turns=int(input("\nIn how many turns do you want to guess the string : "))
    print()
    length=int(input("\nhow many letters word do you wanna guess? "))
    word=''.join(random.choice(string.ascii_lowercase) for x in range(length))
    w1=word
    #print(word)
    guesses=""
    previous_guesses=""
    points=0
    failed=0
    while turns>0:
        print()
        x=input("Guess a letter: ")
        
        previous_guesses+=x
        if x in w1:
            print()
            print("status:Correct")
            guesses+=x
            points+=1
            w1=w1.replace(x,'',1)
            if len(guesses)==len(word):
                break
        else:
            
            points-=1
            print()
            print("Status: Wrong")
            failed+=1
        print("no.of attempts left : {}".format(turns))
        print("no.of Failure attempts: {}".format(failed))
        print("previously guessed letters: {}".format(previous_guesses))
        turns-=1
    if turns!=0 and points>0:
        print("\nyou won the game by {} points out of {}".format(points,length))
    else:
        print("\nsorry {} you lost the game with {} points".format(Name,points))
    print("\nThe word is: {}".format(word))
    x=input("\nDo you wanna play one more(y/n): ")
    if x=="y":
        hangman()
Name=input("Enter your Name: ")
print("\nHello!!! {} ,Let\'s play hangman".format(Name))
print(" ")
hangman()
