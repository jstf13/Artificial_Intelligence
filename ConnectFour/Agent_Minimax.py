from board import Board
from agent import Agent

player_one = 1
player_two = 2
x = "x"
y = "y"

class AgentMinimax(Agent):
    def next_action(self, obs):
        while True:
            try:
                input_value = int(input())
                return input_value
            except ValueError:
                print("Please insert a number.")

    def heuristic_utility(self, board: Board):
        if board.is_winning_cell((board._last_modified_cell[x], board._last_modified_cell[y])):
            return float('inf') if board.winner == player_one else float('-inf')

        if board.is_full():
            return 0

        valid_moves = board.get_posible_actions()
        best_score = float('-inf') if board._get_player_str == player_one else float('inf')

        for col in valid_moves:
            temp_board = board.clone()
            temp_board.add_tile(col, board._get_player_str)
            score = self.heuristic_utility(temp_board)
            if board._get_player_str == player_one:
                best_score = max(score, best_score)
            else:
                best_score = min(score, best_score)

        return best_score