from os import path
from manuscriptlist import ManuscriptList
from manuscript import Manuscript
import statelist
import datelib
import readline

def main():
    mslist = ManuscriptList()
    if path.isfile('editsys.dat'):
        mslist = ManuscriptList()
        mslist.recover()
    exit = False
    while not exit:
        inputs = raw_input('[editsys]: ').split()
        if len(inputs) == 1:
            if inputs[0] == 'exit':
                exit = True
            elif inputs[0] == 'ner':
                mslist.listnotrevised()
            elif inputs[0] in statelist.statelist:
                mslist.listbystate(inputs[0])
            else:
                print mslist.search(inputs[0])
        elif len(inputs) == 2:
            ms = mslist.search(inputs[0])
            if ms is None:
                ms = Manuscript(inputs[0])
                mslist.add(ms)
            else:
                if inputs[1] == 'er':
                    ms.set_revised()
                else:
                    ms.new_state(inputs[1])
        else:
            ms = mslist.search(inputs[0])
            if ms is None:
                ms = Manuscript(inputs[0], datelib.str_to_date(inputs[2]))
                mslist.add(ms)
            else:
                ms.new_state(inputs[1], datelib.str_to_date(inputs[2]))
    mslist.dump()

if __name__ == '__main__':
    main()
