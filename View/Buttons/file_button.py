#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk, StringVar
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter.font import Font

# Responsible for selecting the knowledge_base file 
class Window(tk.Frame):

    # Constructor 
    def __init__(self, master, parser):
        tk.Frame.__init__(self, master)
        self.master = master
        self.parser = parser
        self.init_window()
        self.filename = ''

    # Initializes the window 
    def init_window(self): 
        # The start window, with browsing button and start button
        self.master.title("Start")
        self.pack(fill = 'both', expand = 1)
        self.configure(bg = "PaleTurquoise2")
        self.filepath = tk.StringVar()
        self.label_explanation = tk.Label(
                self,
                text    = "This knowledge based system works as follows:\n 1.) Browse the knowledge base\n 2.) Click on start\n 3.) Fill out the questions, you can choose multiple options for one question\n 4.) Get your advise\n 5.) Press exit at the end to exit the knowledge based system! ",
                font    = Font(size=11),
                width   = 120,
                height  = 18,
                bg = 'pink'
            ).pack(side = BOTTOM)
        
        self.browseButton = tk.Button(self, text = 'Click here to browse your knowledge base!', bg = 'red',
                                 command = self.first_browser,height = 2, width = 30, highlightbackground='#3E4149' )
        okVar = tk.IntVar() #the okVar variable is used so it waits before a button is clicked
        self.browseButton.place(relx=0.3, rely=0, anchor='n')
        self.startButton = tk.Button(self, text = 'Start Questions',
                               command=lambda: okVar.set(1), height = 5, width = 20, highlightbackground='red')
        self.startButton['state'] = 'disable'
        self.startButton.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.startButton.config(background = 'red')
        self.wait_variable(okVar)
        self.destroy()

    def get_filename(self):
        return self.filename

    # When file_button is pressed, gets and sets path
    def first_browser(self):
        file = self.show_file_browser()
        self.filepath.set(file)
        
    # Responsible for the file selection interface 
    def show_file_browser(self):
        self.filename = askopenfilename()
        if self.parser.parse_knowledge_base(self.filename):
            self.browseButton.destroy()
            self.startButton['state'] = 'normal'
