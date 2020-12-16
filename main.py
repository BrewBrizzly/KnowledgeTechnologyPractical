import tkinter as tk
from tkinter import filedialog
from xml_parser import *
from interface import *
from solver import *

if __name__ == "__main__":
    parser = XML_Parser()                                       # Parser object instanciated
    parser.parse_kowledge_base(filedialog.askopenfilename())    # Selecting and parsing the xml file
    interface = Interface()                                     # Asking the questions and obtaining the facts
    solver = Solver()                                           # Solving the knowledge base with the facts obtained
