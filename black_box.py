import unittest

def addition(num_1, num_2):
    return abs(num_1) + num_2

class black_box_test(unittest.TestCase):

    def test_addition_positve(self):
        num_1 = 10
        num_2 = 56

        result = addition (num_1,num_2)

        self.assertEqual(result,66)
    
    def test_addition_two_negatives(self):
        num_1 = -10
        num_2 = -6

        result = addition (num_1,num_2)
        print(result)

        self.assertEqual(result,-16)


if __name__ == '__main__':
    unittest.main()
