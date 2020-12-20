import os
import xml.etree.ElementTree as ET
from goal import *
from question import *
from rule import *

# Responsible for parsing the knowledge base and the clauses
class XML_Parser(object):

    # Creating two lists containing the knowledge base and the clauses
    def __init__(self):
        self.rules = list()
        self.goals = list()
        self.questions = list()

    # Parsing the actual knowledge base
    def parse_kowledge_base(self, path):
        # If file does not exist
        if os.path.isfile(path) is False:
            Log.e(f"Clause file {inputFile} does not exists")
            return

        tree = ET.parse(path)
        root = tree.getroot()
        # Going through first level instances in xml file
        for node in root:
            if node.tag == 'rule':
                self.rules.append(Rule(node))
            if node.tag == 'goal':
                self.goals.append(Goal(node))
            if node.tag == 'question':
                self.questions.append(Question(node))
