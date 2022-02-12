# 12.02.2022
# Project: Weight Converter

weight = float(input("Weight: "))
type_weight = input("(L)bs or (K)g: ").lower()

if type_weight == "l":
    kilo = weight * 0.45
    print(kilo)
elif type_weight == 'k':
    kilo = weight / 0.45
    print(kilo)
else:
    print("You can only enter k or l")