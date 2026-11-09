print ("Welcome to my quiz  game, Hey There!")

playing = input ("Do you want to play? ")

if playing.lower() != "yes":
    quit()

else:
    print ("Awsome, let's get into it!")

score = 0

#Question and Answer Section
answer = input ("What does GPU stand for? ")
    
if answer.lower() == "graphics processing unit":
        print ("Correct!")
        score += 1

else:
    print ("Incorrect!")

answer = input ("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print ("Correct!")
    score += 1

else:
    print ("Incorrect!")

answer = input ("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print ("Correct!")
    score += 1

else:
    print("Incorrect!")

answer = input ("What does the term CLI mean? ")

if answer.lower() == "command line interface":
    print ("Correct!")
    score += 1

else:
    print ("Incorrect!")

print ("Thank you for playing my quiz, your score will be displayed below :)")
print ("You have " + str(score) + " points")
print ("you have " + str(score / 4 * 100) + "%")