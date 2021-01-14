#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

# Responsible for parsing a rule to the knowledge base
class Rule(object):

    # Assigning the root node, creating a list containing one or more instances of a list containig a conditional, creating a list containming the conclusion(s) and running make_rule
    def __init__(self, rule):
        self.rule = rule
        self.description = ''
        self.conditional = list()
        self.conclusion = list()
        self.make_rule()
        count = 0
        for x in self.conditional:
            count += len(x)
    # Making a rule
    def make_rule(self):
        for child in self.rule:
            if child.tag == 'if':
                self.make_conditional(child)
            if child.tag == 'then':
                self.make_conclusion(child)
            if child.tag == 'description':
                self.description = child.text

    # Making the conditional of the rule with the idea that when one list containing a conditional is true, the whole rule is true and the conclusion is obtained.
    # Example format of (A and B) or (C and D) : [[{A: False}, {B: False}], [{C: False}, {D: False}]]
    def make_conditional(self, parent):
        for child in parent:
            if child.tag == 'fact':
                self.conditional.append([{child.text: False}])
            if child.tag == 'or':
                self.make_or(child)
            if child.tag == 'and':
                self.make_and(child)

    # Making a or clause for a rule
    def make_or(self, parent):
        for child in parent:
            if child.tag == 'fact':
                self.conditional.append([{child.text: False}])
            if child.tag == 'and':
                self.make_and(child)

    # Making a and clause for a rule
    def make_and(self, parent):
        tmp_clause = list()
        # Keeping track of the amount of or clauses
        count_or = 0
        for child in parent:
            if child.tag == 'fact':
                tmp_clause.append({child.text: False})
            if child.tag == 'or' and count_or >= 1:
                tmp_clause = self.demorgan(tmp_clause, child, True)
            if child.tag == 'or' and count_or < 1:
                count_or += 1
                tmp_clause = self.demorgan(tmp_clause, child, False)
        if count_or:
            for clauses in tmp_clause:
                self.conditional.append(clauses)
        else:
            self.conditional.append(tmp_clause)

    # Applying the deMorgan law, inverse is instantiated when more than 2 or clauses are detected
    def demorgan(self, clause1, clause2, inverse):
        tmp_clause = list()
        # If only one or clause has been read
        if clause1 and not inverse:
            #for atom1 in clause1:
            for atom2 in clause2:
                temp = clause1.copy()
                temp.insert(len(clause1), {atom2.text: False})
                tmp_clause.append(temp)
                #tmp_clause.append([clause1, {atom2.text: False}]) #problem with the nested for loop, shouldnt be nested, try with print outs, should save all facts of and + one fact of or
            return tmp_clause
        # If more than one or clause has been read
        if clause1 and inverse:
            for atom1 in clause1:
                for atom2 in clause2:
                    #print(atom2.text)
                    temp = atom1.copy()
                    temp.insert(len(atom1), {atom2.text: False})
                    #print(temp)
                    tmp_clause.append(temp)
                    #tmp_clause.append(atom1 + [{atom2.text: False}])
            return tmp_clause
        # If no or clause has been read yet
        if not clause1:
            for atom in clause2:
                tmp_clause.append({atom.text: False})
            return tmp_clause

    # Making a conclusion for a rule
    def make_conclusion(self, parent):
        for child in parent:
            if child.tag == 'fact':
                self.conclusion.append({child.text : False})
