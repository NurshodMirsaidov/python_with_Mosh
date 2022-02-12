    #             ////////     WHILE LOOPS     ////////

# i = 1
# while i <= 5:
#     print("+" * i)
#     i = i+1
# print('Done')

          #  GUESS GAME
# secret_number = 9
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("YOU WON! ")
#         break
# else:
#     print("You lose!")                         

#               CAR GAME                                         

# command =""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         elif started == True:
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = True
#             print("Car stopped...")
#     elif command == "help":
#         print("""
# start - to start the car 
# stop - to stop the car
# quit - to quit
#         """) 
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand this..")

#               FOR LOOPS

# for item in "PYTHON":
#     print(item)

# for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print(item)

# for i in range(10, 100, 4):
#     print(i)

# prices =[10, 20, 30]
# total = 0
# for i in prices:
#     total+= i
# print(f"Total: {total}")

# for x in range(40):
#     for y in range(43):
#         print(f"({x}, {y})")

# numbers =[5, 2, 5, 2, 2]
# for x in numbers:
#     output = ""
#     for count in range(x):
#         output+="x"
#     print(output)


#                               LISTS

# names = ['john', 'bob', 'mosh', 'nurshod']
# names[3] = "NURSHOD"
# print(names[1:])
# print(names)

# numbers = [3, 4, 22, 21, 543, 35343]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

#               2D LISTS 

# matrix = [
#     [1, 2, 3], 
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][1])
# for row in matrix:
#     for item in row: 
#         print(item)

