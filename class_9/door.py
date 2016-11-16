# -*- coding: utf-8 -*- 
class Door(object):
    color = 'brown'

    def __init__(self, number, state):
        self.number = number
        self.state = state

    def open(self):
        self.state = 'open'

    def close(self):
        self.state = 'close'
