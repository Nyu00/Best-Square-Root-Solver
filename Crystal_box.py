import unittest


def  has_more_than_17(age):
    if age >= 18:
        return True
    else:
        return False



class Test_of_crystal(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()


