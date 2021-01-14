#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

from Parser.xml_parser import *
from View.knowledge_frame import *
from Forward_chaining.forward_chaining import *

if __name__ == "__main__":
    parser = XML_Parser()                                       # Parser object instanciated
    solver = Solver()                                     		# Solving the knowledge base with the facts obtained
    frame = Knowledge_frame(parser, solver)                     # Creating the frame of the ui

