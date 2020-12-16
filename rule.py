
# responsible for parsing a rule to the knowledge base
class Rule(object):

    def __init__(self, rule):
        print("I'm a rule")
        self.rule = rule
        self.description = ''
        self.conditional = list()
        self.conclusion = list()
        self.make_rule()

    def make_rule(self):
        for node in self.rule:
            if node.tag == 'if':
                self.conditional.append(node)
            if node.tag == 'then':
                self.conclusion.append(node)
