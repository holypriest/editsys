import datetime as dt
from statelist import statelist

class State(object):

    def __init__(self, acc_date):
        self.state = ('ac', acc_date)
        self.history = {}

    def set_state(self, newstate, acc_date = dt.datetime.now()):
        '''Updates the current state of a manuscript'''
        self.history[self.state[0]] = self.state[1]
        self.state = (newstate, acc_date)

    def get_state(self):
        '''Returns a string representing the current state of a manuscript'''
        return ('%s at %s\n' % (statelist[self.state[0]], self.state[1]))

    def __str__(self):
        state = ''
        for h in self.history:
            state = state + ('%s at %s\n' % (statelist[h], self.history[h]))
        state = state + '%s' % self.get_state()
        return state
