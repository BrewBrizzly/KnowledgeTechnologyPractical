import os
import xml.etree.ElementTree as ET
from goal import *
from question import *
from rule import *

# responsible for parsing the knowledge base and the clauses
class XML_Parser(object):

    # creating two lists containing the knowledge base and the clauses
    def __init__(self):
        self.knowledge_base = list()
        self.Clause = list()

    # parsing the actual knowledge base
    def parse_kowledge_base(self, path):
        if os.path.isfile(path) is False:
            Log.e(f"Clause file {inputFile} does not exists")
            return

        tree = ET.parse(path)
        root = tree.getroot()
        for node in root:
            if node.tag == 'rule':
                self.knowledge_base.append(Rule(node))
            if node.tag == 'goal':
                self.knowledge_base.append(Goal(node))
            if node.tag == 'question':
                self.knowledge_base.append(Question(node))
