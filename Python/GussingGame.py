import random


class player_guess:
  def guess (x):
      random_number = random.randint(1, x)
      guess = 0
      while guess != random_number:
          guess = int(input(f"guess a number between  1 and {x}: "))
          if guess < random_number:
              print("your guess is too low ")
          elif guess > random_number:
              print("your guess is too high")
      print(f"Congrats, you guessed it right {random_number}")

class comp_guess:
  def computer_guess (x):
      low = 1
      high = x
      feedback = " "
      while feedback != 'c' : 
          if low != high:
              guess= random.randint(low, high)
          else:
            guess = low #also high because low = high
          
          feedback = input(f"Is {guess} too high 'h' , too low 'l' , or correct'c': ").lower()
          
          if feedback == 'l':
            low = guess - 1
          elif feedback == 'h':\
              high = guess + 1 
      print(f"well played the computer have done it {guess} ")

class option :
  def choic ():
    ask = "1-you guess the number\n2-computer guesses your number: "
    choic = int(input(ask))
    while True:
      if choic == 1:
        player_guess.guess(100)
      elif choic == 2: 
        comp_guess.computer_guess(100)
      else :
        print("invalid input pleas chose correctly")
        return choic
game = option
game.choic()

