N = 20
P = 0

for a in range(N):
  i = 20
  j = 1
  while i > j:
    P = P + (a * i - a * j) ** 2
    i = i - 1
    j = j + 1

print("El valor de p es:", P)
  