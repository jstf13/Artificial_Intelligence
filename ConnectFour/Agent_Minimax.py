from Tic_Tac_Toe import TicTacToe
from Agent import Agent
import random

animation = [
    "[=     ]",
    "[ =    ]",
    "[  =   ]",
    "[   =  ]",
    "[    = ]",
    "[     =]",
    "[    = ]",
    "[   =  ]",
    "[  =   ]",
    "[ =    ]",
]


class AgentMinimax(Agent):
    def __init__(self, player=1):
        super().__init__(player)

    def policy(self, board: TicTacToe) -> tuple[int, int]:
        self.idx = 0
        pos, _ = self.minimax(board, self.player)
        return pos

    def minimax(self, board: TicTacToe, player: int)-> tuple[tuple[int, int], int]:
        # Animación para que se vea lindo
        print(animation[int(self.idx/300) % len(animation)], end="\r")
        self.idx += 1
        # Fin de animacion

        #TODO: Completar

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
            pass

        else: #max (player == self.player)
            #Buscar acción que maximiza el valor
            pass

        return chosen_action, value