"""
import re       # possibly unnecessary
import json     # mostly necessary

TO DO:
   1) gotta learn json... i guess?
   2) serial search algo... not looking forward to it
   3) Loop() works, Lookup() doesn't. make it so Lookup() works.
   4) Generalized "type hinting file" or some nonsense dictionary
   this is why JSON is mostly necessary.
   
   If we just have a 'help.json' file to refer to, cuts down on redundancy and
   makes searching more efficient.
"""
class Helper:
    def __init__(s):
        '''The constructor'''
        s.st = False
        s.user = str()
        s.quit_str = "Q"

        # need to add new stuff here
        '''files, attributes, methods here.
           it is easy to see the initial intention,
           but would be difficult to implement in practice.

           In no uncertain terms, "python dictionawies aw scawwy."
           Time to learn the JSON module, I have put it off long
           enough. Also, I was supposed to be doing math today
           for "mathematical mondays". Oh well.
           --Cameron
        '''
        s.files = {
            "array_file": "mainframe/src/python/array_machine_v0.1.py",
            "help_file": "mainframe/src/python/helper_v0.1.py",
            "windows_file": "mainframe/src/python/windows_v0.1.py",
            }
        s.attributes = []   # add to these
        s.methods = []      # add to these
        s.setup()
        s.loop()
        # nothing necessary below here thus far

    def setup(s):
        '''Prints a pretty welcome message to terminal'''
        print()
        print("~"*30,"HELP MENU","~"*30)
        print()
        print("_\t"*10)
        print()
        print("You can type help([filename -.py extension])")
        print("to see the docstrings if this menu proves")
        print("to be unhelpful.")
        print()
        print("_\t"*10)
        print()
        return None

    def loop(s):
        while s.st == False and s.user != s.quit_str.lower():
            print("Welcome to interactive help menu.")
            print("What do you need help with?")
            print("_\t"*10)
            print("Options are:\n'f' for files,\n'm' for methods,\n'a' for attributes,\n'q' to quit")
            print("_\t"*10)
            print()
            s.user = input("Enter option : ")
            if s.user.lower() == 'f':
                print("GREAT SUCCESS!")
            elif s.user.lower() == 'm':
                print("GREAT SUCCESS!")
            elif s.user.lower() == 'a':
                print("GREAT SUCCESS!")
            elif s.user.lower() == 'q':
                print("Exiting interactive help...")
                s.st = True
        return None

test = Helper()
# garbage lookup failure nonsense logic below
"""
    def lookup(s):
        '''The lookup logic for looking for attributes and methods'''
        s.user.lower() = search_item
        if search_item in s.files:
            with search_item as f:
                open(f,'rt')

#this is backwards below.

        with s.user.lower() as f:
            open(f,'rt')
            if s.user.lower() in s.files:
                print("SUPER GREAT SUCCESS!")
        pass
"""
