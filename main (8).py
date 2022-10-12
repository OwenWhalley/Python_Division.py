#Created by: Owen Whalley
#Created on: 2022/10/12

#This asks the user the value of the number that is being divided and the value of the number that it is being divided by. It then puts these values into the variables x and y.
x = int(input("What number is being divided?: "))
y = int(input("What is this number divided by?: "))

#Every time it loops, count is increased by 1, showing how many times this while loop has ran. The amount of time it loops is the quotient. These lines of code loops subtracting the first value by the second value without it being a negative remainder. 
if x < 10:
  count = -1
else:
  count = 0
  
while x > 0:
  x -= y
  count += 1
  
if x < 0:
  for i in range(1):
    x += y
    break

#This shows the user the quotient and the remainder of this equation.
print("The quotient is "+str(count))
print("The remainder is "+str(x))
