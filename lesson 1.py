"""print (27)
print (57)
print (57+27)
print (27/9)
print ("hello")
print ("hello " + "world")
name = input("what is your name?")
print(name)
print("hello " + name)"""
import random
print ("welcome to our game- guess the number from 1-10")
print ("today, you get three attempts")
number = random.randint (1, 10)
player_number = input("what's your guess?")
player_number = int(player_number)
if player_number<number:
    print ("your number is too low")
if player_number>number:
    print ("your number is too high")
if player_number==number:
    print ("your number is correct")

player_number = input("what's your guess?")
player_number = int(player_number)
if player_number<number:
    print ("your number is too low")
if player_number>number:
    print ("your number is too high")
if player_number==number:
    print ("your number is correct")
    
player_number = input("what's your guess?")
player_number = int(player_number)
if player_number<number:
    print ("your number is too low")
if player_number>number:
    print ("your number is too high")
if player_number==number:
    print ("your number is correct")

