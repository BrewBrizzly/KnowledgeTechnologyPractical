

class Rule(object):

    def __init__(self, rule):
        print("I'm a rule")
        self.rule = rule
        self.description = ''
        self.conclusion = list()
        self.make_rule()

    def make_rule(self):
        for node in self.rule:
            if node.tag == 'if':
                self.make_hypothesis(node)
            if node.tag == 'then':
                self.conclusion.append(node)

    def make_hypothesis(self, object):
        for node in object:
            if node.tag == 'and':
                self.and_clause(node)
            if node.tag == 'or':
                self.or_clause(node)
            if node.tag == 'fact':
                print("I'm a fact")

    def and_clause(self, object):
        print("and clause")

    def or_clause(self, object):
        print("or clause")
