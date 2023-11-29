import math

print(math.gcd(12, 15))  # now we can calculate gcd, just remember to put math dot not infront,moth=library gcd=function
print(math.factorial(3))
print(math.sin(0))
print(math.asin(0))
print(math.log(2,7))
print(math.exp(1))
print(math.pi)
print(math.sqrt(9))
print(math.remainder(10,3))

import random

print("you rolled a die and got:")
print(random.randint(1, 6)) # a random number form 1 to 6
print("you filpped a coin and got:")
flip = random.randint(1,2)
if flip == 1:
    print("heads")
else:
    print("tails")

import time

print("hello please wait for 3 seconds")
time.sleep(3)
print("Thank you")

for x in range(0,11):
    print(10-x)
    time.sleep(1)
    print("python has a clock inside of it")
    print(time.time())
    print("this is the time in python")  # numbers of seconds since 1970


import random
import math
import time
hard = input("Do you want a hard game? Type 'yes' for hard: ")
if hard.lower() == "yes":
   L = 200
   T = 30
else:
    L = 20
    T = 60
score = 0
lives = 3
time_start = time.time()
time_end = time_start + T

while lives > 0 and time.time() < time_end:
  print("--------------------------------------------")

  # Generate numbers
  x = random.randint(1,L)
  y = random.randint(1,L)
  while math.gcd(x,y) == 1:
    x = random.randint(1, L)
    y = random.randint(1, L)

# Ask the question
print("What is the GCD of" ,x,"and",y,"?")
z = int(input("> "))

# Calculate the answer
if z == math.gcd(x,y):
   print("Correct :)")
   score += 1
   print("Score:",score)
else:
  print("Wrong :( the answer was", math.gcd(x,y))
  print("You have", lives, "lives le􏰁")
  lives -= 1
# End of game
print("That is the end of the game, you scored,", score)
quit()

