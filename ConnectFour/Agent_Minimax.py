from board import Board
from agent import Agent
import random



class AgentMinimax(Agent):
    def __init__(self, player=1):
        super().__init__(player)

    def policy(self, board: Board) -> tuple[int, int]:
        self.idx = 0
        pos, _ = self.minimax(board, self.player)
        return pos

    def minimax(self, board: Board, player: int)-> tuple[tuple[int, int], int]:
        #Caso base
        ended, winner = board.is_end()
        if ended:
            if winner == self.player:
                return None, 1
            if winner == self.other_player:
                return None, -1
            else:
                return None, 0

        #Casos no base
        actions = board.get_available_cells()
        random.shuffle(actions)
        action_nodes = []
        for action in actions:
            child_node = board.clone()
            child_node.play(action, player)
            action_nodes.append((action, child_node))

        value = 0
        chosen_action = None  
        
        if player != self.player: # mini
            #Buscar acción que minimiza el valor
            #Del chatGPT sale:
            value = float('inf')
            for col in valid_moves:
                temp_board = board.copy()
                row = get_next_open_row(temp_board, col)
                drop_piece(temp_board, row, col, PLAYER_O)
                value = min(value, minimax(temp_board, depth - 1, True))

        else: #max (player == self.player)
            #Buscar acción que maximiza el valor
            #Del chatGPT sale:
            value = float('-inf')
            for col in valid_moves:
                temp_board = board.copy()
                row = get_next_open_row(temp_board, col)
                drop_piece(temp_board, row, col, PLAYER_X)
                value = max(value, minimax(temp_board, depth - 1, False))

        return chosen_action, value
    
    def next_action(self, obs):
        while True:
            try:
                input_value = int(input())
                return input_value
            except ValueError:
                print("Please insert a number.")

    def heuristic_utility(self, board: Board):
        return 0
