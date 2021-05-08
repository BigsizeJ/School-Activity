import random

def gameover():
    print("Game Over!")

def intro():
    print("Betting game")
    
def main():
    intro()
    money = 100
    Playing_isTrue = True
    name = input("Whats your name?: ")
    print(f"{name}, you have {money}")
    ask = input("Do you wanna play a betting game?(y/n): ")
    if ask == 'y' or ask == 'Y':
        while Playing_isTrue:
            bet = int(input("Place your bet: "))
            Playing_isFalse = int(bet) > money or int(bet) < -1
            while Playing_isFalse:
                print("Please fix your bet")
                bet = int(input("Fix your bet: "))
                Playing_isFalse = int(bet) > money or int(bet) < -1
            bet = int(bet)
            guessThis = random.randint(1, 2)
            guess = int(input("Guess 1 to 2: "))
            if guess == guessThis:
                money = money + bet
                print(f"You win, your money as of now is {money}")
            else:
                money = money - bet
                print(f"You lose, your money as of now is {money}")
            if money <= 0:
                print("You're out of money!")
                Playing_isTrue = False
                gameover()
            else:
                ask = input("Do you wanna play again?(y/n): ")
                if ask == 'Y' or ask == 'y':
                    Playing_isTrue = True
                else:
                    print(f"You got {money}.")
                    Playing_isTrue = False
    else:
        print("Okay")
                
                
main()
