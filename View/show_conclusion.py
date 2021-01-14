#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

from tkinter.font import Font
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk, StringVar
from tkinter import *
from tkinter import messagebox

# Responsible for showing the obtained conclusions 
class Show_conclusion(object):

	# Constructor 
	def __init__(self, window, solver):
		self.solver = solver
		self.window = window
		self.init_window(window, solver)

	# Initializes the window 
	def init_window(self, window, solver):  
		nconclusions = len(self.solver.obtained_goal)
		# If no conclusions found 
		if nconclusions == 0:
			self.label_question = tk.Label(
			    window,
			    text    = "Sorry, no conclusion found! :(\n Press exit",
			    font    = Font(size=20, weight="bold"),
			    width   = 180,#120,
			    height  = 5,
			    bg = 'pink'
			).pack()

		else:
			#looping through the amount of conclusions
			for i in range(nconclusions + 1):
				if i == 0:
					self.show_advise(i, solver, window)
					continue
				okVar = tk.IntVar()
				self.nextButton = tk.Button(window, text = 'Show next advice',
			                       command=lambda: okVar.set(1)).pack()
				window.wait_variable(okVar)
				if i != nconclusions:
					self.show_advise(i, solver, window)
			self.clearFrame(window)
			self.label_question = tk.Label(
			    window,
			    text    = "No remaining advice found, press exit.",
			    font    = Font(size=20, weight="bold"),
			    width   = 180,#120,
			    height  = 5,
			    bg = 'pink',
				wraplength = 600
			).pack()


	# Showing the advise obtained from a conclusion
	def show_advise(self, i, solver, window): 
		self.clearFrame(window)
		self.label_question = tk.Label(
		    window,
		    text    = self.solver.obtained_goal[i],
		    font    = Font(size=10, weight="bold"),
		    width   = 190,#150,
		    height  = 8,#8,
		    bg = 'pink',
			wraplength = 600
		).pack()

	def close_window(self):
		self.destroy()

	def clearFrame(self, window):
	    # destroy all widgets from frame
	    for widget in window.winfo_children():
	       widget.destroy()
