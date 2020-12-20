# Responsible for parsing a rule to the knowledge base
class Rule(object):

    # Constructor 
    def __init__(self, rule):
        self.rule = rule
        self.description = ''
        self.conditional = list()
        self.conclusion = list()
        self.make_rule()
        print("I'm a rule")
        print("the conditionals")
        print(self.conditional)
        print("the conclusion")
        print(self.conclusion)
        print("\n")

    # Making a rule
    def make_rule(self):
        for child in self.rule:
            if child.tag == 'if':
                self.make_conditional(child)
            if child.tag == 'then':
                self.make_conclusion(child)
            if child.tag == 'description':
                self.description = child.text

    # Making the conditional of the rule 
    def make_conditional(self, parent):
        for child in parent:
            if child.tag == 'fact':
                self.conditional.append([{child.text: False}])
            if child.tag == 'or':
                self.make_or(child)
            if child.tag == 'and':
                self.make_and(child)

    # Making a or clause of a rule 
    def make_or(self, parent):
        for child in parent:
            if child.tag == 'fact':
                self.conditional.append([{child.text: False}])
            if child.tag == 'and':
                self.make_and(child)

    # Making a and clause of a rule 
    def make_and(self, parent):
        tmp_and = list()
        or_clause = False
        for child in parent:
            if child.tag == 'fact':
                tmp_and.append({child.text: False})
            if child.tag == 'or':
                or_clause = True 
                # appending the facts of an or clause 
                for fact in child:
                    self.conditional.append(tmp_and + [{fact.text: False}])
        if not or_clause:
            self.conditional.append(tmp_and)

    # Making a conclusion of a rule 
    def make_conclusion(self, parent):
        for child in parent:
            if child.tag == 'fact':
                self.conclusion.append({child.text : False})
