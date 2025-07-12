# isbn_checker .py
# version 0.2
# updates; fixed up the variable names. 
# Renamed "main" to isbn_check, and promptly commented it out.
# Tried to add TODO #7... realized it was a fruitless endeavor this late at night lol.
'''TODO:
   1) Figure out re. Too lazy to do so right now.
   2) Figure out some webscraping nonsense to compare
      the text of each book.
   3) Turning this into part of the regular expression chemistry
      parser turing machine garbage project that's a total dumpster
      fire. Can't stop the unhinged comments in my code lol.
   4) Also going to need some sort of web address search algorithm. 
      Needs to search a few common book re-selling websites.
   5) What's a python?
   6) This is just so that I don't waste any money
      on a textbook that I don't need. I literally just want
      to confirm the book, but since they have different covers,
      they have different ISBNs and I can't f***in' see a
      preview of the d**n book. I'm literally going insane.
   7) Now I need to do input validation lmao.
   8) I also need to find that tiny notebook I wrote all my notes in...
      but that's not really a github thing lol.'''

def isbn_check():
  isbn_1 = int(input("Enter first ISBN with no dashes:  "))
   #if isbn_1.len() > 13:
      #raise nevermind this wont work, trying to parse an int as a string. gotta love alphanumerics and PEP-8 standards.
  isbn_2 = int(input("Enter second ISBN with no dashes:  "))
  if isbn_1 == isbn_2:
    print("Same Book.")
  else:
    print("Different Book.")

#isbn_check()     <------ uncomment for usage purposes.
#'Tis but a scratch.
