
# responsible for parsing a rule to the knowledge base
class Rule(object):

    # Constructor 
    def __init__(self, rule):
        self.rule = rule
        self.description = ''
        self.conditional = {}
        self.conclusion = {}
        self.make_rule()
        print(self.conditional)
        print(self.conclusion)

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
                self.conditional.update({'fact': {child.text: False}, 'fact_value': False})
            if child.tag == 'or':
                self.make_or(child)
            if child.tag == 'and':
                self.make_and(child)
            if child.tag == 'not':
                self.make_not(child)

    # Making a or clause of a rule 
    def make_or(self, parent):
        tmp_and = {}
        tmp_or = {}
        for child in parent:
            if child.tag == 'fact':
                tmp_or.update({child.text: False})
            if child.tag == 'and':
                tmp_and.update(child)
        if bool(tmp_and) and not bool(tmp_or):
            self.conditional.update({'or_and': tmp_and, 'or_and_value': False})
        if bool(tmp_and) and bool(tmp_or):
            self.conditional.update({'fact_and': {'and': tmp_and, 'and_value': False, 'fact': tmp_or, 'fact_value': False}, 'fact_and_value': False})
        if not bool(tmp_and) and bool(tmp_or):         
            self.conditional.update({'or': tmp_or, 'or_value': False})

    # Returning the and clause in case of or clause
    def or_and_clause(self, parent):
        tmp_and = {}
        for child in parent:
            if child.tag == 'fact':
                tmp_and.update({child.text: False})
        return {'and': tmp_and, 'and_value': False}

    # Making a and clause of a rule 
    def make_and(self, parent):
        tmp_and = {}
        tmp_or = {}
        for child in parent:
            if child.tag == 'fact':
                tmp_and.update({child.text: False})
            if child.tag == 'or':
                tmp_or.update(self.and_or_clause(child))
        if bool(tmp_or):
            self.conditional.update({'and_or': {'and': tmp_and, 'and_value': False, 'or': tmp_or, 'or_value': False}, 'and_or_value': False})
        else:         
            self.conditional.update({'and': tmp_and, 'and_value': False})

    # Returning the or clause in case of and clause
    def and_or_clause(self, parent):
        tmp_or = {}
        for child in parent:
            if child.tag == 'fact':
                tmp_or.update({child.text : False})
        return tmp_or

    # Making a not clause of a rule 
    def make_not(self, parent):
        for child in parent:
            if child.tag == 'fact':
                self.conditional.update({'not': {child.text : False}, 'not_value': False})

    # Making a conclusion of a rule 
    def make_conclusion(self, parent):
        for child in parent:
            if child.tag == 'fact':
                self.conclusion.update({'conclusion' : {child.text : False}})
