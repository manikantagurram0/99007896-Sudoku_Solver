import numpy as np

Grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 0, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]



class Grand:
    def Possible(self, row, column, number):
        pass

    def Solve(self):
        pass


class Parent(Grand):
    def Possible(self, row, column, number):
        global Grid
        # Is the number appearing in the given row?
        for i in range(0, 9):
            if Grid[row][i] == number:
                return False

        # Is the number appearing in the given column?
        for i in range(0, 9):
            if Grid[i][column] == number:
                return False

        # Is the number appearing in the given square?
        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if Grid[y0 + i][x0 + j] == number:
                    return False

        return True


class Main(Parent):
    def Solve(self):

        global Grid

        for row in range(0, 9):
            for column in range(0, 9):

                if Grid[row][column] == 0:

                    for number in range(1, 10):

                        if self.Possible(row, column, number):
                            Grid[row][column] = number
                            self.Solve()
                            Grid[row][column] = 0

                    return

        print(np.matrix(Grid))
        input('More possible solutions')


obj = Main()
obj.Solve()
