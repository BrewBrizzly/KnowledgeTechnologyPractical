#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

from View.Buttons.file_button import *
from View.show_question import *
import tkinter as tk
from sys import exit
from tkinter import messagebox

# Responsible for creating the frame of the UI 
class Knowledge_frame(object):

    # Constructor 
    def __init__(self, parser, solver):
        self.parser = parser
        self.solver = solver
        self.frame()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    # Closing the frame 
    def on_closing(self, check, frame):
        if check:
            frame.destroy()
            sys.exit(0)

    # Fix for closing the frame 
    def donothing(self):
        pass

    # Creating the actual frame 
    def frame(self):
        frame = tk.Tk()
        frame.protocol('WM_DELETE_WINDOW',self.donothing)
        frame.title("Knowledge_frame")
        frame.geometry("800x450") #600x450
        frame.configure(bg = "PaleTurquoise2")

        ex = Window(frame, self.parser)
        print(ex.get_filename())
        Show_question(frame, self.parser, self.solver)
        frame.quit = tk.Button(frame, text = 'Exit', bg = 'yellow',
                                 command = lambda: self.on_closing(1, frame),height = 2, width = 30, highlightbackground='red')

        frame.quit.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
        frame.quit.pack(side=BOTTOM)

        frame.mainloop()
