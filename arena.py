from chess import Item, Knight

class Arena(object):
    def __init__(self):
        self.size = 8
        self.knight_chess = {}
        self.item_chess = {}

    def setup_chess(self):
        # Create Knights
        # Knight( name, position )
        kn_map = {
            'red': (0, 0),
            'yellow': (0, 7),
            'blue': (7, 0),
            'green': (7, 7)
        }
        for kname, pos in kn_map.items():
            kn = Knight(kname)
            self.knight_chess[kname] = { 'position': pos, 'knight': kn }

        # Create Items
        # Item( name, position, attack, defence, order )
        item_map = {
            'axe': [(2, 2), 2, 0, 1],
            'dagger': [(2, 5), 1, 0, 3],
            'maggic_staff': [(5, 2), 1, 1, 2],
            'halmet': [(5, 5), 0, 1, 4]
        }
        for itname, attr in item_map.items():
            it = Item(itname, attr[1], attr[2], attr[3])
            self.item_chess[itname] = { 'position':attr[0], 'item':it }

    def get_pts(self, knight_name):
        knight = self.knight_chess[knight_name]['knight']
        ap = knight.atk_pts
        dp = knight.def_pts
        if knight.equip:
            ap += knight.equip.atk_pts
            dp += knight.equip.def_pts
        # print("{} has ATK {}, DEF {}".format(knight, ap, dp))
        return (ap, dp)

    # move('red', 'S') or move('red', d)
    def move(self, knight_name, direct):
        kpos = self.knight_chess[knight_name]['position']
        knight = self.knight_chess[knight_name]['knight']

        def drowned(self):
            self.knight_chess[knight_name]['position'] = None  # Drowned pos
            knight.atk_pts = 0
            knight.def_pts = 0
            knight.status = 'DROWNED'
            knight.equip = None
            # Drop item if equipped
            if knight.equip:
                knight.equip.equipped = None
            knight.equip = None

        # if knight not in self.knight_chess:  # not exist knight name
        #     return
        if knight.status != 'LIVE':
            return
        direction = direct[0].lower()
        allowed_direction = ('n', 'e', 's', 'w', 'u', 'r', 'd', 'l')
        if direction not in allowed_direction:  # illegal direction
            return

        # Get knight position by its name
        x, y = kpos
        if direction == 'n' or direction == 'u':
            x -= 1
        elif direction == 's' or direction == 'd':
            x += 1
        elif direction == 'e' or direction == 'r':
            y += 1
        elif direction == 'w' or direction == 'l':
            y -= 1

        # Check if drowned
        if x < 0 or y < 0 or x > self.size-1 or y > self.size-1:
            drowned(self)
        else:
            # Write new position to the knight
            print('Move {} to ({}, {})'.format(knight, x, y))
            self.knight_chess[knight_name]['position'] = (x, y)
            knight_equ = self.knight_chess[knight_name]['knight'].equip
            if knight_equ:
                self.item_chess[knight_equ.name]['position'] = (x, y)

    def pickup(self, knight_name):
        # check knight stand_on tile items and try to equip
        # {(2, 2): 'axe', (2, 5): 'dagger', ... }
        knight = self.knight_chess[knight_name]['knight']
        if knight.status != 'LIVE':
            return
        kpos = self.knight_chess[knight_name]['position']
        item_candidates = {}
        for it in self.item_chess.items():
            if it[1]['position'] == kpos:
                item = it[1]['item']
                if not item.equipped:
                    item_candidates[item.order] = it[0]
        print(item_candidates)
        for order in item_candidates:
            item_name = item_candidates[order]
            item = self.item_chess[item_name]['item']
            if knight.equip is None:
                knight.equip = item
                knight.atk_pts, knight.def_pts = self.get_pts(knight_name)
                item.equipped = knight
            elif knight.equip.order > order:  # swap item
                knight.equip.equipped = None    # Drop equipment
                knight.atk_pts, knight.def_pts = (1, 1)
                knight.equip = item
                knight.atk_pts, knight.def_pts = self.get_pts(knight_name)
                item.equipped = knight

    def battle(self, knight_name):
        # check stand_on tile knight and try to fight
        knight = self.knight_chess[knight_name]['knight']
        if knight.status != 'LIVE':
            return
        stand_on = self.knight_chess[knight_name]['position']
        enemy = None
        for k in self.knight_chess.items():
            if k[0] == knight_name:
                continue
            if k[1]['position'] == stand_on:
                enemy = k[1]['knight']
        print("Battle: {} - {}".format(knight, enemy))
        if not enemy:
            return

        # Attacker get 0.5 atk_pts bouns
        # Attacker atk_pts + 0.5 - Defencer def_pts
        battle_pts = knight.atk_pts + 0.5 - enemy.def_pts
        print("Detail: {} - {}".format(knight.name, enemy.name))
        print("Attacker: {}, attack: {}".format(knight.name, knight.atk_pts +
                                                0.5))
        print("Defencer: {}, defence: {}".format(enemy.name, enemy.def_pts))
        if battle_pts > 0:  # Attacker win
            self.killed(enemy)
        else:   # Defencer win
            self.killed(knight)

    def killed(self, knight):
        knight.atk_pts = 0
        knight.def_pts = 0
        knight.status = 'DEAD'
        if knight.equip:
            knight.equip.equipped = None
        knight.equip = None
        print("{} has been killed.".format(knight))

    def show(self):
        print(self.knight_chess)
        print(self.item_chess)

    def showk(self):
        print(self.knight_chess)

    def showi(self):
        print(self.item_chess)

    def show_board(self):
        item_map = {}
        knight_map = {}
        drowned_list = []

        # Items map
        for it in self.item_chess.values():
            if it['position'] not in item_map:
                item_map[it['position']] = it['item'].name[0].upper()
            else:
                item_map[it['position']] = '*'

        # Knights map
        for kn in self.knight_chess.values():
            if kn['position'] not in knight_map:
                knight_map[kn['position']] = kn['knight'].name[0].upper()
            else:
                item_map[kn['position']] = '*'

        # Those not shown in map are drowned knights
        for kn in self.knight_chess.values():
            if kn['position'] is None:
                drowned_list.append('({})'.format(kn['knight'].name[0]))

        # topbar
        drowned_str = ' '.join(drowned_list)
        print('  _ ' * ( 8-len(drowned_list) ) + ' ' + drowned_str)
        for i in range(self.size):
            row = ""
            for j in range(self.size):
                character = '_'
                if (i, j) in item_map:
                    character = item_map[(i, j)]
                if (i, j) in knight_map:
                    character = knight_map[(i, j)]
                row += "| {} ".format(character)
            row += "|"
            # tile container
            print(row)
        # bottom border
        # print('  _ '*8+' ')
        return
