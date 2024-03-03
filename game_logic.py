import random

from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

lis_num_Player = [] # Lista para almacenar los números ingresados por el jugador
lis_computer_guess=[]# Lista para almacenar los números ingresados por el computador


def get_player_name():
    """Obtiene el nombre del jugador."""
    name = input(f"{Fore.MAGENTA} Digita tu nombre: {Style.RESET_ALL}")
    return name

def generate_random_number():
    """Genera un número aleatorio entre 1 y 100."""
    return random.randint(1, 100)


# def player_turn(num_Random, attempts,name):

   
#     """Realiza el turno del jugador, solicitando la entrada y comparando con el número secreto."""
#     try:
        
#         num_Player = int(input(f"{Fore.BLUE}{name}:Guess the number: {Style.RESET_ALL}"))
#         attempts += 1
#         lis_num_Player.append(num_Player)

#     except ValueError:
#         print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")
#         return num_Random, attempts, False

#     if num_Player == num_Random:
#      print(f"{Fore.MAGENTA}Congratulations, ¡ you guessed the number in {attempts} attempts!,\n list the numbers {lis_num_Player}{Style.RESET_ALL}\n")
                
#      return num_Random, attempts, True
    
#     elif num_Player < num_Random:
#         print(f"{Fore.YELLOW}The secret number is greater >. Try again!{Style.RESET_ALL}")

#     else:
#         print(f"{Fore.YELLOW}The secret number is smaller <. Try again!{Style.RESET_ALL}")

#     return num_Random, attempts, False
# 

def player_turn(num_Random, attempts, name):
    """Realiza el turno del jugador, solicitando la entrada y comparando con el número secreto."""
    while True:
        try:
            num_Player = int(input(f"{Fore.BLUE}{name}: Guess the number (1-100): {Style.RESET_ALL}"))

            if 1 <= num_Player <= 100:
                lis_num_Player.append(num_Player)
                attempts += 1

                if num_Player == num_Random:
                    print(f"{Fore.MAGENTA}Congratulations, you guessed the number in {attempts} attempts!\nList of numbers entered: {lis_num_Player}{Style.RESET_ALL}\n")
                    return num_Random, attempts, True

                elif num_Player < num_Random:
                    print(f"{Fore.YELLOW}The secret number is greater >. Try again!{Style.RESET_ALL}\n")

                else:
                    print(f"{Fore.YELLOW}The secret number is smaller <. Try again!{Style.RESET_ALL}\n")

                break  # Sal del bucle si todo está correcto
            else:
                print(f"{Fore.RED}Please enter a number between 1 and 100.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

    return num_Random, attempts, False



def computer_turn(num_Random, attempts_comp):

    """Realiza el turno de la computadora, generando una suposición aleatoria y comparándola con el número secreto."""
    computer_guess = random.randint(1, 100)
    print(f"{Fore.CYAN}{Style.BRIGHT}The computer makes a guess: {computer_guess}{Style.RESET_ALL}")
    attempts_comp += 1
    lis_computer_guess.append(computer_guess)

    if computer_guess == num_Random:
        print(f"{Fore.CYAN}{Style.BRIGHT}Congratulations, ¡ you guessed the number in Computer {attempts_comp} attempts! Entered numbers: {lis_computer_guess}{Style.RESET_ALL}")

        return num_Random, attempts_comp, True

    elif computer_guess < num_Random:
        print(f"{Fore.YELLOW}The secret number is greater >. Try again!{Style.RESET_ALL}\n")
    else:
        print(f"{Fore.YELLOW}The secret number is smaller <. Try again!{Style.RESET_ALL}\n")

    return num_Random, attempts_comp, False

def guess_new():
     
     result = input(f"{Fore.BLUE} Play Again Y/N => {Style.RESET_ALL}\n").lower()
     
     if result != 'y' and result != 'n':
        input(f"{Fore.BLUE}Enter correctly Y/N => {Style.RESET_ALL}\n")
        return False
     
     elif result == 'y':
        lis_num_Player.clear()
        lis_computer_guess.clear()
        return True
     
     elif result == 'n':
        print("I finish the game")
        return False
        
        

