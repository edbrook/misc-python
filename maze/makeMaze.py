#!/usr/bin/env python3

from random import choice
from sys import stdout


__all__ = ['MazeBuilder']


class Cell(object):
    def __init__(self,row,col):
        self.row = row
        self.col = col

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.visited = False
        self.start = False
        self.end = False
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "({},{})".format(self.col,self.row)


class MazeBuilder(object):
    """Builds a "perfect maze" with the given number of rows and columns."""

    def __init__(self,rows,cols):
        """Sets the parameters for the maze"""
        self.rows = rows
        self.cols = cols
        self.cells = None
        self._reset_cells()

    def build(self):
        """Builds a new maze based on the current parameters"""
        self._reset_cells()
        self.cells[0][0].start = True
        self.cells[self.rows-1][self.cols-1].end = True
        r = choice(range(self.rows))
        c = choice(range(self.cols))
        path = [self.cells[r][c]]
        #path[0].end = True
        while path:
            current_cell = path.pop()
            current_cell.visited = True
            unseen = self._get_unseen_neighbors(current_cell)
            if unseen:
                path.append(current_cell)
                next_cell = choice(unseen)
                self._remove_wall_between(current_cell,next_cell)
                #current_cell.start = False
                #next_cell.start = True
                path.append(next_cell)

    def display(self):
        """Display a string representation of the maze"""
        stdout.write('+---' * self.cols)
        stdout.write('+\n')
        for r in range(self.rows):
            rl = ""
            cl = ""
            for c in range(self.cols):
                cell = self.cells[r][c]
                se = " "
                if cell.start:
                    se = "S"
                elif cell.end:
                    se = "E"
                if not cell.left:
                    cl += '| {} '.format(se)
                else:
                    cl += '  {} '.format(se)
                if not cell.down:
                    rl += '+---'
                else:
                    rl += '+   '
            stdout.write('{}|\n'.format(cl))
            stdout.write('{}+\n'.format(rl))

    def _remove_wall_between(self,current_cell,next_cell):
        """Removes walls between this next_cell and current_cell"""
        if next_cell.row == current_cell.row:
            # On the same row - remove left/right walls
            if next_cell.col > current_cell.col:
                # next_cell is right of current_cell
                current_cell.right = True
                next_cell.left = True
            else:
                # next_cell is left of current_cell
                current_cell.left = True
                next_cell.right = True
        elif next_cell.col == current_cell.col:
            # In the same col - remove up/down walls
            if next_cell.row > current_cell.row:
                # next_cell is below current_cell
                current_cell.down = True
                next_cell.up = True
            else:
                # next_cell is above current_cell
                current_cell.up = True
                next_cell.down = True
        else:
            raise Exception("Cells are the same or not neighbors!")

    def _get_neighbors(self,cell):
        """Returns a list of all neighboring cells"""
        r = cell.row
        c = cell.col
        neighbors = []
        if cell.col < self.cols - 1:
            neighbors.append(self.cells[r][c+1]) # Right
        if cell.col > 0:
            neighbors.append(self.cells[r][c-1]) # Left
        if cell.row < self.rows - 1:
            neighbors.append(self.cells[r+1][c]) # Down
        if cell.row > 0:
            neighbors.append(self.cells[r-1][c]) # Up
        return neighbors

    def _get_unseen_neighbors(self,cell):
        """Returns a list of neighboring cells that have not yet been visited"""
        unseen_neighbors = []
        for neighbor in self._get_neighbors(cell):
            if not neighbor.visited:
                unseen_neighbors.append(neighbor)
        return unseen_neighbors

    def test(self,r,c):
        self._get_neighbors(self.cells[r][c])

    def _reset_cells(self):
        """Rebuild the list of cells yet to be visited"""
        self.cells = [[Cell(r,c) for c in range(self.cols)] for r in range(self.rows)]


if __name__ == '__main__':
    from sys import argv
    maze = MazeBuilder(int(argv[1]),int(argv[2]))
    maze.build()
    maze.display()
