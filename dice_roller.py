import random 



def main():
  dice_rolls = int(input("How many dice would you like to roll? "))
  dice_size = int(input("How many sides are the dice? "))
  dice_sum = 0
  
  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    dice_sum += roll  # this can also be written as: dice_sum = dice_sum + roll / x += y /

    if roll == 1:
      print(f"You rolled a {roll}! Critical fail!")
    elif roll == 6:
      print("You rolled a {roll}! Critical Success!")
    else:
      print(f"You rolled a {roll}...")
  print(f"You have rolled a total of: {dice_sum}")
if __name__== "__main__":
  main()        