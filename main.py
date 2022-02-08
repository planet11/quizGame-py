print("Welcome to the Quiz game!")

playing = input("Would you like to play the game? ")

if playing.lower() != "yes":
    print("Bye, hope to see you soon!")
    quit()

print("Lets play!")
score = 0

answer = input("Which is the 8th planet from the Sun? ")
if answer.lower() == "neptune":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")

answer = input("Which is the largest ocean?")
if answer.lower() == "pacific":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")

answer = input(f'Who devised the "theory of evloution?" ')
if answer.lower() == "charles darwin":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")

answer = input("Which continent is considered as the cradle of humanity?")
if answer.lower() == "africa":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")

print(f'\nFinal Score: {score}/40')
print(f'\nYou got {(score/40) * 100} % correct!')