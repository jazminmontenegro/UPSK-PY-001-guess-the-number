import unittest
from unittest.mock import patch
from game_logic import generate_random_number,get_player_name, player_turn, computer_turn




class Test_generate_random_number(unittest.TestCase): #para verificar el comportamiento de la funcion

    
    def test_generated_number_within_range(self):
        """Verifica que el número generado esté dentro del rango esperado."""
        random_number = generate_random_number()
        self.assertTrue(1 <= random_number <= 100)  # self.assertTrue verifica si la expresión es verdadera

    @patch('builtins.input', return_value='jazmin')
    def test_player_name(self, mock_input):
        """Prueba el nombre del jugador."""
        name= get_player_name()
        self.assertEqual(name, 'jazmin')  # assertEqual para verificar la igualdad

    def test_generated_number_is_integer(self):
        """Verifica que el número generado sea un entero."""
        random_number = generate_random_number()
        self.assertIsInstance(random_number, int)

    @patch('builtins.input', side_effect=['5']) 
    def test_valid_input(self, mock_input): 
        num_Random, attempts, success = player_turn(5, 0,'jazmin') #llama a la funcion con dos argumentos num_ramdow y attempts
        self.assertEqual(num_Random, 5)  
        self.assertEqual(attempts, 1)  
        self.assertEqual(success, True) 


       
    @patch('random.randint', return_value=6) #retona la computadora el numero 5
    def test_computer_turn_correct_guess(self, mock_randint):
        num_Random = 6
        attempts_comp = 0
        result = computer_turn(num_Random, attempts_comp)
        self.assertEqual(result, (num_Random, 1, True))


if __name__ == '__main__':
    unittest.main()