import re
import json
from arena import Arena

class Game(object):
    # 1.    Setup chess
    # 2.    Read from moves.txt / Read instruction
    # 3.    Let an instruction run in a round
    # 3.1   Move knight, check drowned or alived
    # 3.2   Try to pickup a equipment
    # 3.3   Try to fight, winner kill loser
    # 3.4   (print map)
    arena = Arena()
    arena.setup_chess()     # 1. Setup

    def start(self):
        def moves_list():
            moves = []
            with open('moves.txt') as f:
                for line in f:
                    moves.append(line.strip())
                f.close()
            return moves

        # 2. Read from moves.txt
        moves = moves_list()
        for move in moves:
            match = re.fullmatch(r"(\w+):(\w+)", move)
            if match:
                # <knight_name>:<move>
                self.round_handler(match[1], match[2])  # 3. Round
        # 4. Generate final state json file
        self.gen_final_state_file()

    def round_handler(self, knight=None, movement=None):
        kn_name = { 'r': 'red', 'g': 'green', 'b': 'blue', 'y': 'yellow' }
        if knight[0].lower() in kn_name.keys():
            print('>>>> round start')
            knight_name = kn_name[knight[0].lower()]
            self.arena.move(knight_name, movement)  # 3.1 Move knight
            self.arena.pickup(knight_name)          # 3.2 Try to pickup
            self.arena.battle(knight_name)          # 3.3 Try to fight
            self.arena.show_board()                 # 3.4 Print Map 
            print('<<<< round   end')

    def gen_final_state_file(self):
        filename = 'final_state.json'
        content = self.arena.final_state()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=4)


game = Game()
game.start()
