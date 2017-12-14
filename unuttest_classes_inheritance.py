import unittest
from Classes_inheritance import *

def setUpModule():
    print "Setup before all"


def tearDownModule():
    print "Tear Down after all"


class TestAnimals(unittest.TestCase):

    def setUp(self):
        self.some_animal = Animal()
        self.doggy = Dog()
        self.kitty = Cat()
        self.gib = SphynxCat()
        self.petya = Rooster()

    def tearDown(self):
        print "Delete instances after all tests"
        del self.some_animal
        del self.doggy
        del self.kitty
        del self.gib
        del self.petya


    def test_some_animal_paw(self):
        print "In the test"
        some_animal = Animal()
        self.assertEqual(self.some_animal.paw, 4)

    def test_some_animal_tail(self):
        self.assertEqual(self.some_animal.tail, 1)

    def test_some_animal_wool(self):
        self.assertTrue(self.some_animal.wool)

    def test_doggy_paw(self):
        self.assertEqual(self.doggy.paw, 4)

    def test_doggy_tail(self):
        self.assertEqual(self.doggy.tail, 1)


class TestNewAnimals(unittest.TestCase):

    def setUp(self):
        self.some_animal = Animal()
        self.doggy = Dog()
        self.kitty = Cat()
        self.gib = SphynxCat()
        self.petya = Rooster()

    def tearDown(self):
        print "Delete instances after all tests"
        del self.some_animal
        del self.doggy
        del self.kitty
        del self.gib
        del self.petya

    def test_doggy_wool(self):
        self.assertTrue(self.doggy.wool)

    def test_doggy_say_something(self):
        self.assertEqual(Dog.say_something(), "Woof - woof")

    def test_kitty_paw(self):
        self.assertEqual(self.kitty.paw, 4)

    def test_kitty_tail(self):
        self.assertEqual(self.kitty.tail, 1)

    def test_kitty_wool(self):
        self.assertTrue(self.kitty.wool)

    def test_kitty_say_something(self):
        self.assertEqual(Cat.say_something(), "Meow - meow")

    def test_gib_paw(self):
        self.assertEqual(self.kitty.paw, 4)

    def test_gib_tail(self):
        self.assertEqual(self.kitty.tail, 1)

    def test_gib_wool(self):
        self.assertFalse(SphynxCat.wool)

    def test_gib_say_something(self):
        self.assertEqual(SphynxCat.say_something(), "Murr - murr")

    def test_petya_paw(self):
        self.assertEqual(self.petya.paw, 2)

    def test_petya_tail(self):
        self.assertEqual(self.petya.tail, 1)

    def test_petya_wool(self):
        self.assertFalse(Rooster.wool)

    def test_petya_say_something(self):
        self.assertEqual(Rooster.say_something(), "Cocorico")


if __name__ == '__main__':
    unittest.main()
