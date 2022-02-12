# numbers = [3, 2, 4, 5,  6, 23, 24, 434423]
# max = numbers[0]
 
# for number in numbers:
#     if max < number:
#         max = number
# print(max)

####                              2D LISTS
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for item in row:
#         print(item)             


##                              LIST METHODS
numbers = [5, 2, 7, 4,2322323]
#numbers.append(20) # Listning oxiriga biror qiymat qo'shish uchun
#numbers.sort() #Listdagi barcha objectlarni sartirovka qiladi 
#numbers.reverse() #Listdagi barcha objectlarni kottasidan kichigiga qarab sartirovka qiladi
#numbers.insert(0, 200)# Listning xohlagan joyiga object qo'shish uchun ishlatilati
#numbers.count(5) #Listning tarkibida qavs ichidagi qiymat nechta ekanligi topadi
#numbers.remove(2) # Listdan biror objectni olib tashlash uchun ishlatiladi
# numbers.clear() # Listdagi barcha objectlarni yo'q qilish uchun ishlatiladi
#numbers.pop() # Listning oxirgi objectini tozalash uchun ishlatiladi
#print(30 in numbers) #Mavjud listning tarkibida ushbu kiritilgan qiymat bormi so`rash uchun ishlatiladi
#print(numbers.index(4)) #Kiritilgan index orqali listning shu indexidagi elementni topadi

# print(numbers)






##                              EXERCISES ABOUT REMOVING DUBLICATED OBJECTS

# numbers = [1, 2, 3, 4, 4, 2, 7, 1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)







#######                                     TUPLES
numbers = (1, 2, 3) # THIS IS TUPLE WITH == ()
numbers[0] = 10
print(numbers[0])
# TUPLESning  LISTdan farqi bu -- listning tarkibidagi ma'lumotlarni o'zgartirsa bo'ladi 
#Lekin Tuplesning ma'lumotlarni o'zgartira olmaymiz 