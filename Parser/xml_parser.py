import os
import xml.etree.ElementTree as ET
from Parser.Goals.goal import *
#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

from Parser.Questions.question import *
from Parser.Rules.rule import *

# Responsible for parsing the knowledge base and the clauses
class XML_Parser(object):

    # Creating three lists containing the rules, goals and questions stated in the knowledge base xml
    def __init__(self):
        self.rules = list()
        self.goals = list()
        self.questions = list()

    def get_rules(self):
        return self.rules

    def get_goals(self):
        return self.goals

    def get_questions(self):
        return self.questions

    # Parsing the actual knowledge base xml
    def parse_knowledge_base(self, path):
        if os.path.isfile(path) is False:
            print("Clause file does not exists")
            return 0

        tree = ET.parse(path)
        root = tree.getroot()
        # Going through first level instances in xml file
        count = 0
        for node in root:
            if node.tag == 'rule':
                self.rules.append(Rule(node))
                count += 1
            if node.tag == 'goal':
                self.goals.append(Goal(node))
            if node.tag == 'question':
                self.questions.append(Question(node))
        return 1 