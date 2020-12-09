import tkinter as tk
from tkinter import filedialog
from xml_parser import *

if __name__ == "__main__":
    parser = XML_Parser()
    parser.parse_kowledge_base(filedialog.askopenfilename())
