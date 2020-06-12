"""Guess the value of a dice role and see if you're correct"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(input("What number do you think the dice will roll? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, 6)
  second_roll = randint(1, 6)
  max_val = number_of_sides * 2
  print(str(max_val))
  guess = get_user_guess()
  if guess > int(max_val):
    print ("Your guess exceeds the possible limit")
  else:
    print("Rolling")
    sleep(2)
    print ("Roll 1: %d" %first_roll)
    sleep(1)
    print ("Roll 2: %d" %second_roll)
    sleep(1)
    total_roll = first_roll+second_roll
    print(total_roll)
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("You Won")
    else:
      print("Don't play the lottery")

roll_dice(6)