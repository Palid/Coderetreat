class Game(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = Game.create_matrix(self.width, self.height)


    def set_cell(self, row, column, is_alive):
        self.matrix[row][column] = int(is_alive)
        cell = self.matrix[row][column]
        return cell

    def get_previous_or_last_neighbour(self, row, column):
        row_is_behind = row == 0
        row_behind_conditionals = {
            True: self.width - 1,
            False: row,
        }
        row_is_after = row == self.width - 1
        row_after_conditionals = {
            True: self.width - 1,
            False: 0,
        }
        column_is_behind = column == 0
        column_is_after = column == column.height - 1
        column_conditionals = {
            True: self.height - 1,
            False: 0,
        }


    def get_neighbors(self, row, column):
        pass

    @staticmethod
    def create_matrix(width, height):
        rows = range(height)
        columns = lambda x: list(map(lambda x: 0, range(width)))
        matrix = list(map(columns, rows))
        return matrix
