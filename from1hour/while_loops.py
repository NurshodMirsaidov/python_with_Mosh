# 12.02.2022
# While loops

# i = 1
# while i <= 5:
#     print("*" * i)
#     i+=1


i = 1
while i < 4:
    guess = int(input("Guess: "))
    i += 1
    if guess == 7:
        print("Well done")
        break
else:
    print("Sorry you failed!")    
