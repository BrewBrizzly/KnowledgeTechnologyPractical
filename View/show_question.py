#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

from tkinter.font import Font
from View.show_conclusion import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk, StringVar
from tkinter import *

# Responsible for showing the questions and the next button in the panel 
class Show_question(object):

    # Constructor 
    def __init__(self, window, parser, solver):
        i = 0
        self.parser = parser
        self.solver = solver
        self.window = window
        self.facts = list()
        self.init_window(window, parser)

    # Initializes the window 
    def init_window(self, window, parser):  
        nquestions = len(self.parser.questions)
        #looping through the amount of questions and eventually showing them in order 
        for i in range(nquestions + 1):
            if i == 0:
                self.show_question(i, parser, window)
                continue
            okVar = tk.IntVar()
            self.nextButton = tk.Button(window, text = 'Next',
                               command=lambda: [okVar.set(1), self.set_state()]).pack()
            window.wait_variable(okVar)
            if i != nquestions:
                self.show_question(i, parser, window)
        self.clearFrame(window)
        show_conclusion = Show_conclusion(self.window, self.solver)

    # Showing the questions
    def show_question(self, i, parser, window):
        self.clearFrame(window)
        self.label_question = tk.Label(
            window,
            text    = self.parser.questions[i].description,
            font    = Font(size=20, weight="bold"),
            width   = 120,
            height  = 5,
            bg = 'pink'
        ).pack()

        self.option_list(i, window, parser)

    # Creating a list which contains all the options of the question 
    def option_list(self, n, window, parser):
        options = {}
        keys = range(len(self.parser.questions[n].option))
        var1 = tk.BooleanVar()
        for k, op in zip(keys, self.parser.questions[n].option):
            options[k] = list(op[1])[0]
            checkbox = self.check_box(window,options, k, var1, op)

    # Creating the checkboxes for the question 
    def check_box(self,window, options, k, var1, op): 
        var1 = tk.IntVar()
        var1.set(0)
        save_facts = list()
        checkbox = Checkbutton(window, text = op[0], variable=var1, command = lambda: self.append_facts(options, k), onvalue=1, offvalue=0, bg = "PaleTurquoise2").pack()
        return checkbox

    # Allows only passing a fact from a question when a box has been selected at the time of pressing next 
    def append_facts(self, options, k):
        if options[k] in self.facts: 
            self.facts.remove(options[k])
        else:
            self.facts.append(options[k])

    # After a question has been answered, parse the facts obtain and clear the facts from the list 
    def set_state(self):
        if self.facts:
            for fact in self.facts:
                # print(fact)
                self.solver.forward_chain_query(self.parser, fact)
            self.facts.clear()


    def close_window(self):
        self.destroy()

    def clearFrame(self, window):
        # destroy all widgets from frame
        for widget in window.winfo_children():
           widget.destroy()
