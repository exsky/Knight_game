class Chess(object):
    def __init__(self, name, attack_pt, defence_pt):
        self.name = name
        self._attack = attack_pt
        self._defence = defence_pt

    def __str__(self):
        return "<Chess: %s, ATK: %s, DEF: %s>" % (self.name, self.atk_pts,
                                                  self.def_pts)

    def __repr__(self):
        # return self.name[0].upper()
        return "<Chess: %s>" % self.name

    @property
    def atk_pts(self):
        return self._attack

    @atk_pts.setter
    def atk_pts(self, attack_pt):
        self._attack = attack_pt

    @property
    def def_pts(self):
        return self._defence

    @def_pts.setter
    def def_pts(self, defence_pt):
        self._defence = defence_pt


class Item(Chess):
    def __init__(self, name, attack, defence, order):
        super().__init__(name, attack, defence)
        self.equipped = False
        self.order = order

    def __str__(self):
        return "<Item: %s, ATK: %s, DEF: %s>" % (self.name, self.atk_pts,
                                                 self.def_pts)

    def __repr__(self):
        # return self.name[0].upper()
        return "<Item: %s>" % self.name

class Knight(Chess):
    def __init__(self, name, attack=1, defence=1):
        super().__init__(name, attack, defence)
        self._equipment = None
        self.status = 'LIVE'

    def __str__(self):
        return "<Knight: %s, ATK: %s, DEF: %s>" % (self.name, self.atk_pts,
                                                   self.def_pts)

    def __repr__(self):
        # return self.name[0].upper()
        return "<Knight: %s>" % self.name

    @property
    def equip(self):
        return self._equipment

    @equip.setter
    def equip(self, equipment_item):
        self._equipment = equipment_item
