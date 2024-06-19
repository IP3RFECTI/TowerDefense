import unittest

class TestMyFunctions(unittest.TestCase):
    def setUp(self):
        # Здесь можно подготовить данные для тестов
        pass

    def test_my_function(self):
        self.assertEqual(my_function(2, 3), 5)