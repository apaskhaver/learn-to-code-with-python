import unittest
from unittest.mock import MagicMock

class Actor():
    def jump_out_of_helicopter(self):
        return "Nope, not doing it!"
    
    def light_on_fire(self):
        return "Heck no, where's my agent?"

class Movie():
    def __init__(self, actor):
        self.actor = actor

    def start_filming(self):
        # this method's only responsibility is to call 2 other methods.
        # if you comment one of these out, the below test fails
        # because assert_called() will fail on these methods
        self.actor.jump_out_of_helicopter()
        self.actor.light_on_fire()

class MovieTest(unittest.TestCase):
    def test_start_filming(self):
        # don't need an Actor object to test if the start_filming()
        # method called jump_out_of_helicopter() and light_on_fire()
        stuntman = MagicMock()
        movie = Movie(stuntman)

        movie.start_filming()

        # testing if start_filming() called those two methods
        # Were they called? assert_called() will let us know.
        stuntman.jump_out_of_helicopter.assert_called()
        stuntman.light_on_fire.assert_called()

if __name__ == "__main__":
    unittest.main()