# oh lord. this is becoming a thing.
'''What was initially supposed to be some quick couple of functions
   quickly became an animal that I could not fathom to tame.

   The original intention was just to be an exercise passing arrays
   between functions...
   Then I started thinking of problems I could solve...
   Then I started making more problems I could solve...
   Now I have too many problems.

   Edited 7/12/25 instead of going to bed. Made one line more pythonic.

TO DO:
   1) The interactive help section sucks thus far. It
   gets into itself and works (except for the else blocks...?)
   possible fix is a lookup function... which i don't wanna do rn

   2) Better organization. __init__ should not have the sheer amount of
   nonsense that it does already. it needs to have like, three arrays tops.

   3) Control flow. I shouldn't have to pass a single argument/parameter
   during the instantiation of the object. My object should have a name,
   and just work.

   4) Possible GUI? original array machine idea had tkinter imported.
   could probably get away with adding a graphical dealio. this would
   likely be achieved in a separate file.

   5) Separate the helper function into its own class in a separate
   file. Make it more general and reusable. More. MORE!!!

   6) Calendar function. yeah idk i just kinda realized that you could
   store like months and days and stuff into arrays. So a different
   file of course.
                    TO REMAIN IN THIS CLASS/FILE
   7) Bubble sort
   8) Merge sort
   9) Reverse sort
   10) Load random array (numerical array with random values)
   11) Couple card games for fun why not?

   --Cameron, 5/3/25
'''
import random as r

class ArrayTest:
    def __init__(s):
        '''constructor for attributes and "mainloop method" <- antiquated idea'''
        s.methods = ['setup',
                    'printer',
                    'prettier_printer',
                    'parallel_printer',
                    'total',
                    'average',
                    'loader',
                    'unloader'
                    ]
        s.attributes = ['a',
                        'num_copy',
                        'txt_copy']
        s.a = []
        s.setup()
        print(s.a)         # Debugging print
        # Attributes

        # Unknown length arrays
        s.num_copy = [0]
        s.txt_copy = ['']

    def setup(s) -> list:
        '''a setup function for pretty terminal interaction
           this is very quickly turning into a main function.'''
        print()
        print("~"*20,"WELCOME TO THE ARRAY MACHINE!!!","~"*20)
        print()
        print("\t\tProgrammed in May 2025 by Cameron Kowalke\t\t")
        print()
        print("_\t"*30)
        print()
        print("Are you dealing with letters or numbers?")
        print("Enter '1' for letters, '2' for numbers, 'H' for help, 'Q' to quit.")
        s.c = str(input("Enter option : "))
        if s.c == '1':
            s.a = ['']
        elif s.c == '2':
            s.a = [0]
        elif s.c.upper() == 'H':
            s.helper()    # not quite done
            s.a = [0]
        else:
            s.a = [0]
        return s.a
        

    def parallel_printer(s, a: list, b: list) -> None:
        '''checks array lengths, then prints parallel arrays only
           A is first parameter. B is second
           If I do come back to change this, I will add an error
           checker dealio that will raise OutOfBounds errors
           depending upon which list length is out of range'''
        s.a = a
        s.b = b
        if len(s.a) == len(s.b):
            for i in range(len(s.a)):
                print(s.a[i]," : ",s.b[i])

    def printer(s, a: list) -> None:
        '''prints a single element of an array at a time.'''
        s.a = a
        for i in range(len(s.a)):
            print(s.a[i])

    def prettier_printer(s, a: list) -> None:
        '''a prettier printer function, still one element
           of the array at a time'''
        s.a = a
        s.idx = int(0)
        s.l = int(len(s.a)-1)   
        if s.l == -1:
            s.l = 0             
        while s.idx < s.l:
            print(s.a[s.idx], end=', ')
            s.idx += 1
        print(s.a[s.idx])
        

    def total(s, a: list) -> float:
        '''total of the array'''
        s.a = a
        s.t = float()
        for i in range(len(s.a)):
            s.t += s.a[i]
        return s.t
                
    def average(s, a: list) -> float:
        '''average of the array.'''
        s.a = a
        s.avg = float()
        for i in range(len(s.a)):
            s.avg += s.a[i]
        s.avg = s.avg / len(s.a)
        return s.avg

    def loader(s, a: list, b: int) -> list:
        '''insert elements into a user defined array.
           a is the empty num/txt array, b is length'''
        s.a = a
        s.b = b
        s.a = s.a * s.b
        s.data = str(type(s.a[0]))
        if s.data == "<class 'int'>" or s.data == "<class 'float'>":
            for i in range(len(s.a)):
                s.a[i] = float(input("Enter # : "))
        else:
            for i in range(len(s.a)):
                s.a[i] = input("Enter text :\t")
        print("~"*20,"Loaded Array","~"*20)
        s.prettier_printer(s.a)
        return s.a

    def unloader(s, a: list):
        '''deletes all the elements from an array'''
        s.a = a
        s.__resetter(s.a)
        return s.a

    def __resetter(s, a: list) -> list:
        '''the actual deletion logic of unloader
           a very convoluted solution, aka stupid.
           however, guarantees an empty array for
           loading purposes and works better than
           built-in del method.'''
        s.a = a
        s.data = str(type(s.a[0]))
        if s.data == "<class 'int'>" or s.data == "<class 'float'>":
            s.a = s.num_copy
        elif s.data == "<class 'str'>":
            s.a = s.txt_copy
        else:
            s.a = s.num_copy  # default to numbers if we don't know datatype
        return s.a

    def helper(s) -> None:
        '''a help procedure that prints helpful things to the screen'''
        s.st = False
        s.u = str()
        print()
        print("~"*30,"HELP MENU","~"*30)
        print()
        print("_\t"*10)
        print()
        print("\tYou can type help(ArrayTest) in the terminal to see docstrings")
        print("\tIf this menu proves jarring to look at.")
        print()
        print("_\t"*10)
        print()
        while s.st == False and s.u != ('Q' or 'q'):
            print("Welcome to the interactive help menu!", end=', ')
            print("What do you need help with?")
            print("_\t"*10)
            print("Options are:\n'm' for methods,\n'a' for attributes,\n'u' for usage,\n'q' to quit.")
            print("_\t"*10)
            print()
            s.u = input("Enter option : ")
            if s.u == 'm' or s.u == 'M':
                print("_\t"*10)
                for i in range(len(s.methods)):
                    print(s.methods[i])
                print("_\t"*10)
                print("Enter the name of the method without quotes exactly as you see it if\nyou would like to learn more.")
                print("Or, simply enter 'q' to quit.")
                s.u = input("Enter option : ")
                if s.u in s.methods:
                    print("GREAT SUCCESS!")
                elif s.u == 'q' or s.u == 'Q':
                    print("Exiting interactive help...")
                    s.u = 'Q'
                    s.st = True
                else:
                    print("Please enter a valid option.")
            elif s.u == 'a' or s.u == 'A':
                print("_\t"*10)
                for i in range(len(s.attributes)):
                    print(s.attributes[i])
                print("_\t"*10)
                print("Enter the name of the attribute without quotes exactly as you see it if\nyou would like to learn more.")
                print("Or, simply enter 'q' to quit.")
                s.u = input("Enter option : ")
                if s.u in s.attributes:
                    print("GREAT SUCCESS!")
                elif s.u == 'q' or s.u == 'Q':
                    print("Exiting interactive help...")
                    s.u = 'Q'
                    s.st = True
                else:
                    print("Please enter a valid option.")
            elif s.u == 'u' or s.u == 'U':
                print("_\t"*10)
                for i in range(len(s.methods)):
                    print(s.methods[i])
                for i in range(len(s.attributes)):
                    print(s.attributes[i])
                print("_\t"*10)
                print("Enter the name of the option to see its usage.")
                print("Or, simply enter 'q' to quit.")
                s.u = input("Enter option : ")
                if s.u in s.attributes or s.u in s.methods:
                    print("GREAT SUCCESS!")
                elif s.u == 'q' or s.u == 'Q':
                    print("Exiting interative help...")
                    s.u = 'Q'
                    s.st = True
                else:
                    print("Please enter a valid option.")
                    '''dude at a certain point i should just make an
                       entire class just for this stupid interactive help
                       because now it's like, ridiculously complex.

                       it literally needs its own lookup method to dig
                       through its own methods and attribute... which
                       is insane. The level of recursive depth this nonsense
                       will have to achieve...

                       god. I'm gonna play oblivion remastered.'''
             
# test code        
test = ArrayTest()
"""
print(test.days)
print(test.known)
print(test.total(test.known))
print(test.average(test.known))
test.printer(test.known)
test.parallel_printer(test.days, test.known)
test.prettier_printer(test.days)
test.loader(test.num,3)
#test.loader(test.txt,3)
#test.unloader(test.txt)
test.loader(test.a,3)
print(test.a)
test.unloader(test.a)
print(test.a)
test.loader(test.a,3)
print(test.a)

That's all for now.
"""
