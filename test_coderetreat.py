import unittest
from coderetreat import *

def GameFactory():
    return Game(5, 5)


class TestCoderetreat(unittest.TestCase):
    def test_init_size(self):
        game = Game(6, 6)
        self.assertEqual(game.width, 6)
        self.assertEqual(game.height, 6)

    def test_create_matrix(self):
        matrix = Game.create_matrix(5, 5)
        self.assertEqual(len(matrix), 5)
        for row in matrix:
            self.assertEqual(len(row), 5)
            for cell in row:
                self.assertEqual(cell, 0)

    def test_set_cell(self):
        game = GameFactory()
        game.set_cell(row=1, column=0, is_alive=True)
        self.assertEqual(game.matrix[1][0], 1)
        game = GameFactory()
        game.set_cell(row=0, column=1, is_alive=True)
        self.assertEqual(game.matrix[0][1], 1)
        game.set_cell(row=0, column=1, is_alive=False)
        self.assertEqual(game.matrix[0][1], 0)

    def test_get_neighbors(self):
        game = GameFactory()
        game.set_cell(row=0, column=1, is_alive=True)





if __name__ == '__main__':
    unittest.main()
