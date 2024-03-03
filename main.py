from game_logic import generate_random_number, player_turn, computer_turn,get_player_name,guess_new
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)



def play_Random():
    num_Random = generate_random_number()
    attempts = 0
    attempts_comp = 0
    name = get_player_name()

    while True:
        num_Random, attempts, player_won = player_turn(num_Random, attempts, name)
        if player_won:
            break

        num_Random, attempts_comp, computer_won = computer_turn(num_Random, attempts_comp)
        if computer_won:
            break

    while guess_new():
        play_Random()     

print(f"{Fore.GREEN}********************************************************{Style.RESET_ALL}")
print(f"{Fore.GREEN}*             ¡Welcome to the                          *{Style.RESET_ALL}")
print(f"{Fore.GREEN}*             Guess the Number Game!                   *{Style.RESET_ALL}")
print(f"{Fore.GREEN}********************************************************{Style.RESET_ALL}")
# Llamada a la función principal
play_Random()

# Print the welcome message in green
