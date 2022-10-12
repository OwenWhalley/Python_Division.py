x = int(input("What number is being divided?: "))
y = int(input("What is this number divided by?: "))

count = -1

while x > 0:
  x -= y
  count += 1
  
if x < 0:
  for i in range(1):
    x += y
    break

print("The quotient is "+str(count))
print("The remainder is "+str(x))