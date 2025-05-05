import tkinter as tk
from tkinter import ttk
'''Here's where I'm leaving this. It has the ability
   to be tailored to specific needs, but as it stands
   currently, I cannot add more to this program without
   over-complicating it, and thus compromising its
   reusability.

   TO DO:
   1) Figure out how to store variables from
   tkinter textbox inputs. Implement that.

   2) Figure out how to change the icon image.

   3) Decide whether or not it's worth it to make
   the base class window prettier, or leave that
   responsibility on the user...?

   4) Add more complex logic to loop. This
   program seems as though it can break easily.
   
   notes to self:
   tk.iconify() => minimizes window
   tk.deiconfiy() => un-minimizes window
   tk.withdraw() => super-minimizes window
   tk.state() => returns window state as a string?

   icon = tk.PhotoImage(file=[path to png file])
   s.root.iconphoto(True, icon)

   tk.StringVar() => a way to store variables
   tk.Text() => a way to receive inputs...?
   tk.get("1.0", tk.END) => get inputs...?
   tk.insert("1.0", content) => to "restore inputs"...????

   --Cameron
'''
class Window:
    def __init__(s):
        '''an actual constructor'''
        # Master Window object
        s.root = tk.Tk()
        s.root.title("App")                 # To be changed
        s.root.geometry("600x400")
        s.root.columnconfigure(0, weight=2)
        s.root.columnconfigure(1, weight=0)
        s.root.columnconfigure(2, weight=2)
        s.root.rowconfigure(0, weight=1)
        s.root.rowconfigure(1, weight=1)
        s.root.rowconfigure(2, weight=0)
        s.root.rowconfigure(3, weight=2)

        # Secondary Window object
        s.w = tk.Toplevel(s.root)
        s.w.title("App Window 2")           # To be changed
        s.w.geometry("600x400")
        s.w.columnconfigure(0, weight=2)
        s.w.columnconfigure(1, weight=0)
        s.w.columnconfigure(2, weight=2)
        s.w.rowconfigure(0, weight=1)
        s.w.rowconfigure(1, weight=1)
        s.w.rowconfigure(2, weight=0)
        s.w.rowconfigure(3, weight=2)
        s.w.iconify()

        # Must be at the end
        s.loop()
        s.root.tk.mainloop()

    def clopen(s):
        '''a clopening function'''
        s.state_root = str()
        s.state_secondary = str()
        s.state_root = s.root.state()
        s.state_secondary = s.w.state()
        print(s.state_root)
        print(s.state_secondary)
        if s.state_root == "normal" and s.state_secondary == "iconic":
            s.root.iconify()
            s.w.deiconify()
        elif s.state_root == "iconic" and s.state_secondary == "normal":
            s.root.deiconify()
            s.w.iconify()
        elif s.state_root == s.state_secondary:
            s.root.destroy()
         
    def loop(s):
        '''the main loop to edit for purposes'''
        s.root_btn1 = ttk.Button(s.root,
                          text="Root Button",
                          command=s.clopen      # not a great idea to change this.
                          ).grid(column=1,
                                 row=1,
                                 ipadx=10,
                                 ipady=10
                                 )
        
        s.root_btn2 = ttk.Button(s.root,
                          text="Quit",
                          command=s.root.destroy, # not a great idea to change this.
                          ).grid(column=1,
                                 row=2,
                                 ipadx=5,
                                 ipady=5
                                 )
        # s.w_btn1 is the one to add to in order to tailor this to other purposes.
        s.w_btn1 = ttk.Button(s.w,
                              text="Secondary Button", # add command = whatever to this tuple
                              ).grid(column=1,
                                     row=1,
                                     ipadx=10,
                                     ipady=10
                                     )
        
        s.w_btn2 = ttk.Button(s.w,
                              text="Quit",
                              command=s.clopen      # not a great idea to change this.
                              ).grid(column=1,
                                     row=2,
                                     ipadx=5,
                                     ipady=5
                                     )
app = Window()
