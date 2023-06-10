import numpy as np
import gym
from gym import spaces
from board import Board

player_one = 1
player_two = 2
x = "x"
y = "y"

class ConnectFourBaseEnv(gym.Env):
    
    def __init__(self):
        self._length = 7
        self._heigth = 6
        self.action_space = spaces.Discrete(self._length)
        self._current_player = player_one
        self._reset_grid()
    
    def step(self, action):
        assert (self.action_space.contains(action))
        
        movement_played = self._grid.add_tile(action, self._current_player)
        
        if movement_played:
            self._next_player()
            
        done = self._is_done()
        return self._grid, self._get_reward(), done, None
    
    def reset(self):
        self._current_player = player_one
        self._reset_grid()
        return self._grid
    
    def render(self):
        self._grid.render()
        
    def _get_reward(self):
        return 100 if self._grid.winner != 0 else 0
        
    def _is_done(self):        
        return self._grid.is_final()
        
    def _next_player(self):
        self._current_player = player_one if self._current_player == player_two \
                                    else player_two
        
    def _reset_grid(self):
        self._grid = Board(self._heigth, self._length)