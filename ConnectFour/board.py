import numpy as np

empty_cell = 0
int_to_string = [" ", "O", "X"]
x = "x"
y = "y"

class Board:
    def __init__(self, heigth, length):
        self._max_sum = 4
        self._last_modified_cell = {x:0, y:0}
        self._heigth = heigth
        self._length = length
        self._winner = 0
        self._empty_spaces = heigth * length
        self._grid = np.zeros((heigth, length), dtype=np.int64)
        
    def __getitem__(self, item:int) -> int:
        return self._grid[item]
    @property
    def heigth(self):
        return self._heigth
    
    @property
    def length(self):
        return self._length

    @property
    def winner(self):
        return self._winner
    
    def _set_last_modified_cell(self, x_value, y_value):
        self._last_modified_cell[x] = x_value
        self._last_modified_cell[y] = y_value
    
    def is_final(self):
        return self._winner != 0 or self.is_full()
        
    def is_full(self):
        return self._empty_spaces == 0
    
    def occupy_space(self, cell, player):
        pos_x, pos_y = cell
        pos_was_empty = self._grid[pos_x][pos_y] == empty_cell
        
        self._grid[pos_x][pos_y] = player
        self._set_last_modified_cell(pos_x, pos_y)
        self.calculate_winner((pos_x, pos_y))
        
        if pos_was_empty:
            self._empty_spaces -= 1
            # Move outside 'if pos_was_empty:' if chain reactions are allowed
            self._add_connectedd_tiles((pos_x, pos_y))

    
    def _get_player_str(self, cell):
        return int_to_string[cell]
    
    def calculate_winner(self, cell):
        return self.is_winning_cell(cell)
                 
    def is_winning_cell(self, last_cell):
        multiplicands = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        pos_x, pos_y = last_cell
        for (x_mul, y_mul) in multiplicands:
            current_sum = 1
            side = {1:True, -1:True}
            sides = [1, -1]
            for mul in range(1, self._max_sum):
                if not (side[1] or side[-1]):
                    break
                for i in sides:
                    new_pos_x = pos_x + (x_mul * mul *i)
                    new_pos_y = pos_y + (y_mul * mul *i)
                    if self._pos_are_valid(new_pos_x, new_pos_y) and side[i] \
                            and self._grid[new_pos_x][new_pos_y] == self._grid[pos_x][pos_y]:
                        current_sum += 1
                        if current_sum == self._max_sum:
                            self._winner = self._grid[pos_x][pos_y]
                            return True
                    else:
                        side[i] = False
        return False
    
    def add_tile(self, pos_y, player):
        pos_x = self._heigth - 1
        while pos_x >= 0:
            if self._grid[pos_x][pos_y] == empty_cell:
                cell = (pos_x, pos_y)
                self.occupy_space(cell, player)
                self._add_connectedd_tiles(cell)
                
                return True
            pos_x -= 1
        
        return False
                        
    def _add_connectedd_tiles(self, cell):
        pos_x, pos_y = cell
        player = self._grid[pos_x][pos_y] 
        
        # Can't add vertical eating because game is trivial (first player always wins adding always in the same col)
        multiplicands = [(0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]#, (1, 0)]
        
        for (x_mul, y_mul) in multiplicands:
            first_pos_x = pos_x + x_mul
            second_pos_x = pos_x + x_mul * 2
            
            first_pos_y = pos_y + y_mul 
            second_pos_y = pos_y + y_mul  * 2
            
            if self._pos_are_valid(first_pos_x, first_pos_y) \
            and self._grid[first_pos_x][first_pos_y] != player \
            and self._grid[first_pos_x][first_pos_y] != empty_cell:
                if self._pos_are_valid(second_pos_x, second_pos_y) \
                and self._grid[second_pos_x][second_pos_y] == player:
                    self.occupy_space((first_pos_x, first_pos_y), player)
    
    def _pos_are_valid(self, pos_x, pos_y):
        x_is_valid = pos_x >= 0 and pos_x < self._heigth
        y_is_valid = pos_y >= 0 and pos_y < self._length
        return x_is_valid and y_is_valid
    
    def get_posible_actions(self):
        actions = []
        for i in range(self._length):
            if self._grid[0][i] == empty_cell:
                actions.append(i)
                
        return actions
    
    def clone(self):
        board_clone = Board(self._heigth, self._length)
        board_clone._winner = self._winner
        board_clone._empty_spaces = self._empty_spaces
        board_clone._last_modified_cell = self._last_modified_cell
        board_clone._grid = np.copy(self._grid)
        return board_clone
    
    def render(self):
        print(" ", end=" ")
        for i in range(self._length):
            print(" "+str(i)+" ", end=" ") 
        print("")
        for row in self._grid:
            for cell in row:
                player = self._get_player_str(cell)
                print(" | " + player, end="")
            print(" |")
        print("-", end="")
        for _ in self._grid:
            print("-----", end="")
        print("")
    
    