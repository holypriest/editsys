from datetime import date
from state import State

class Manuscript(object):

    def __init__ (self, num, acc_date = date.today()):
        self.number = num
        self.state = State(acc_date)
        self.eng_rev = False

    def new_state(self, state, date = date.today()):
        '''Indicates that the manuscript reached a new state in the
        publication process'''
        self.state.set_state(state, date)

    def is_revised(self):
        '''Returns true if the manuscript was submitted to language revision'''
        return self.eng_rev

    def set_revised(self):
        '''Informs that a manuscript has been submitted to language revision'''
        self.eng_rev = True

    def __str__(self):
        if self.is_revised():
            eng_status = 'Abstract revised'
        else:
            eng_status = 'Abstract NOT revised'

        return ('\n%s:\n\n%s%s\n' % (self.number, self.state, eng_status))
