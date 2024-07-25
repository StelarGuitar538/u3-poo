import unittest
from prueba import verificar_contraseña

class TestPasswordValidator(unittest.TestCase):
    
    def test_contraseña_corta(self):
        with self.assertRaises(ValueError) as context:
            verificar_contraseña("123445674784784768")
        self.assertEqual(str(context.exception), "La contraseña debe tener al menos 8 caracteres")
    
    def test_sin_numeros(self):
        with self.assertRaises(ValueError) as context:
            verificar_contraseña("abcdefgh")
        self.assertEqual(str(context.exception), "La contraseña debe contener al menos un número")
    
    def test_sin_letras(self):
        with self.assertRaises(ValueError) as context:
            verificar_contraseña("12345678")
        self.assertEqual(str(context.exception), "La contraseña debe contener al menos una letra")
    
    def test_contraseña_valida(self):
        self.assertTrue(verificar_contraseña("abc12345"))
    
if __name__ == "__main__":
    unittest.main()
