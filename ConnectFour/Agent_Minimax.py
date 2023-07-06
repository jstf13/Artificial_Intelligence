from board import Board
from agent import Agent

PLAYER_X = 1
PLAYER_O = 2


class AgentMinimax(Agent):
    def __init__(self, player=1):
        super().__init__(player)

    def next_action(self, obs):
        while True:
            try:
                input_value = int(input())
                return input_value
            except ValueError:
                print("Please insert a number.")

    '''
    Debemos definir la función de evaluación (heuristic_utility) que sea buena
    y que cumpla con los criterios que vimos en el teórico.

    El heuristic_utility ya recibe un tablero (board) actual, donde debemos clonar
    y llamar recurrentemente para poder obtener el próximo estado que nos maximice
    ganar.
    '''
    def heuristic_utility(self, board: Board):
        if board.is_winning_cell((board._last_modified_cell[x], board._last_modified_cell[y])):
            return float('inf') if board.current_player == PLAYER_X else float('-inf')

        if board.is_full():
            return 0

        valid_moves = board.get_posible_actions()
        best_score = float('-inf') if board.current_player == PLAYER_X else float('inf')

        for col in valid_moves:
            temp_board = board.clone()
            temp_board.add_tile(col, board.current_player)
            score = self.heuristic_utility(temp_board)
            if board.current_player == PLAYER_X:
                best_score = max(score, best_score)
            else:
                best_score = min(score, best_score)

        return best_score


    
'''         ended = board.is_final()
        if ended:
            winner = board.winner()
            if winner == self.player:
                return 1
            if winner == self.other_player:
                return -1
            else:
                return 0
        #Casos no base
        actions = board.get_posible_actions()
        random.shuffle(actions)
        action_nodes = []
        for action in actions:
            child_node = board.clone()
            action_nodes.append((action, child_node))
            value = min(value, heuristic_utility(child_node)) '''

'''     def policy(self, board: Board) -> tuple[int, int]:
        self.idx = 0
        pos, _ = self.minimax(board, self.player)
        return pos '''

'''     def minimax(self, board: Board, player: int)-> tuple[tuple[int, int], int]:
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

        return chosen_action, value '''
