# 4.01.2022
# While loop

# i = 1
# while i<=5:
#     print("*" * i)
#     i+=1
# print("Done")

# secretNumber = 9
# guessCount = 1
# guessLimit = 3
# while guessCount <= guessLimit:
#     guess = int(input("Guess: "))
#     guessCount += 1
#     if guess == secretNumber:
#         print("You Won")
#         break
# else:
#     print("SORRY YOU FAILED")

# CAR GAME
 
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started....")
    elif command == "stop":
        print("Car stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I dont understand that")