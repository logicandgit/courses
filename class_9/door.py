# -*- coding: utf-8 -*- 
class Door(object):
    color = 'brown'

    def __init__(self, number, state):
        self.number = number
        self.state = state

    @classmethod
    def knock(cls):
        print('Knock!Knock!!')

    def open(self):
        self.state = 'open'

    def close(self):
        self.state = 'close'


class SecurityDoor(Door):
    color = 'gray'
    locked = True

    def open(self):
        if not self.locked:
            print('Opening')
            super(SecurityDoor, self).open()


class CompositeDoor(object):
    # color = 'composite'
    locked = True

    def __init__(self, number, state):
        self.door = Door(number, state)

    def open(self):
        if not self.locked:
            self.door.open()

    def close(self):
        self.door.close()

    def __getattr__(self, attr):
        return getattr(self.door, attr)
