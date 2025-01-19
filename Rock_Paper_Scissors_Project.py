from random import randint
from colorama import init, Fore, Style

init()

request = input("Would you like to start the game of Rock-Paper-Scissors? (Yes or No): ")
player_score, computer_score = 0, 0

while request == "Yes":
    """This is the loop where the player will play against the computer until he/she quits the game"""
    player_move = input("Choose Rock, Paper or Scissors: ")

    if not player_move in ("Rock", "Paper", "Scissors"):
        print(Fore.RED + "Invalid Input. Please try again..." + Style.RESET_ALL)
        request = input("Would you like to continue playing? (Yes or No): ")
        continue

    computer_random_number = randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = "Rock"
    elif computer_random_number == 2:
        computer_move = "Paper"
    else:
        computer_move = "Scissors"

    print(Fore.BLUE + f"The computer chose {computer_move}." + Style.RESET_ALL)

    if (player_move == "Rock" and computer_move == "Scissors") \
            or (player_move == "Paper" and computer_move == "Rock") \
            or (player_move == "Scissors" and computer_move == "Paper"):
        player_score += 1
        print(Fore.GREEN + "You win!" + Style.RESET_ALL)
        print(Fore.CYAN + f"Current scores: {player_score}:{computer_score}" + Style.RESET_ALL)
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!" + Style.RESET_ALL)
        print(Fore.BLUE + f"Current scores: {player_score}:{computer_score}" + Style.RESET_ALL)
    else:
        computer_score += 1
        print(Fore.RED + "You lose!" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + f"Current scores: {player_score}:{computer_score}" + Style.RESET_ALL)

    request = input("Would you like to continue playing? (Yes or No): ")

if request == "No":
    print(Fore.BLUE + "Thank you for playing Rock-Paper-Scissors!" + Style.RESET_ALL)
    print(Fore.GREEN + "Have a nice day!" + Style.RESET_ALL)
else:
    raise SystemExit("Invalid Input")
