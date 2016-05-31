from manuscript import Manuscript
from datetime import *
import datelib

class ManuscriptList(object):

    def __init__(self):
        self.mslist = []

    def add(self, manuscript):
        '''Adds a manuscript object to the manuscript list'''
        self.mslist.append(manuscript)

    def search(self, ms_num):
        '''Searches for a manuscript on the list using its number'''
        for ms in self.mslist:
            if ms.number == ms_num:
                return ms
        return None

    def listbystate(self, ms_state):
        '''Lists all manuscripts which final state is ms_state'''
        counter = 0
        for ms in self.mslist:
            if ms.state.state[0] == ms_state:
                print ms.number
                counter += 1
        print 'Total: %d manuscript(s)' % counter

    def listnotrevised(self):
        '''Lists all manuscripts that were not submitted to english revision'''
        counter = 0
        for ms in self.mslist:
            if not ms.is_revised():
                print ms.number
                counter += 1
        print 'Total: %d manuscript(s)' % counter

    def remove(self, ms_num):
        '''Removes a manuscript from the list using its number'''
        ms = self.search(ms_num)
        if ms is not None:
            self.mslist.remove(ms)

    def dump(self):
        '''Copy list contents to a .dat file'''
        f = open('editsys.dat', 'w')
        for ms in self.mslist:
            f.write(ms.number + ' ')
            for h in ms.state.history:
                f.write('%s:%s ' % (h, ms.state.history[h]))
            f.write('%s:%s ' % (ms.state.state[0], ms.state.state[1]))
            if (ms.is_revised()): f.write('er:t\n')
            else: f.write('er:f\n')
        f.close()

    def recover(self):
        '''Recover list contents from a .dat file'''
        f = open('editsys.dat', 'r')
        for line in f:
            msdata = line.split(' ')
            acstate = msdata[1].split(':')
            m = Manuscript(msdata[0], acstate[1])
            for i in range(2, len(msdata) - 1):
                state = msdata[i].split(':')
                m.new_state(state[0], datelib.str_to_date(state[1]))
            engrev = msdata[len(msdata) - 1].split(':')
            if (engrev[1].rstrip() == 't'): m.set_revised()
            self.add(m)
        f.close()

    def __str__(self):
        ms_list = '\n'
        for ms in self.mslist:
            ms_list = ms_list + '%s\n' % ms.number
        return ms_list
