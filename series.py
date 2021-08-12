n = int(input("Ingrese un número N: "))

#Seríe A
print("|Serie A|")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = "")
    print()
    
#Serie B
print("|Serie B|")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end = "")
    print()

#Serie C
print("|Serie C|")
for i in range (1, n + 1):
    for j in range (i, i + 4):
        print(j, end="")
    print()

#Serie D
print("|Serie D|")
for i in range(1 , n + 1):
    for j in range(1, i):
        print(j, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()
    
#Serie E
print("|Serie E|")
for i in range(1, n + 1):
    for j in range(i, n + 1):
        print(j, end="")
    for j in range(1, i):
        print(j, end="")
    print()