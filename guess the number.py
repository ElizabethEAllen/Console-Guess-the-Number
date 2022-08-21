import random
min_num = 1
max_num = 1000
attempts = 20
print (f"welcome to our game- guess the number from {min_num}-{max_num}")
print (f"today, you get {attempts} attempts")
number = random.randint (min_num, max_num)
while attempts > 0:
    player_number = input("what's your guess?")
    player_number = int(player_number)
    if player_number<number:
        print ("your number is too low")
    if player_number>number:
        print ("your number is too high")
    if player_number==number:
        print (f"your number is correct, {attempts} attempts remain")
        break
    attempts = attempts - 1
    if attempts == 0:
        print ("game over!")
