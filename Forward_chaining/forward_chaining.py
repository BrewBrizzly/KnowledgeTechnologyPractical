#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

from Parser.xml_parser import *

class Solver(object):

    # Creating a list containing obtained conclusions
    def __init__(self):
        self.obtained_goal = list()

    # Checks all rules their value, if true the conclusion is returned and the rule is deleted
    def forward_chain_query(self, knowledge_base, answer):
        rule_true = False
        for rule in knowledge_base.get_rules():
            if self.forward_chain_rule(rule.conditional, knowledge_base.get_goals(), answer, rule.conclusion[0]):
                knowledge_base.get_rules().remove(rule)
                return True
        return False

    # Goes through a rule and checks if a single instance is true given the answer of the user
    def forward_chain_rule(self, conditionals, goals, answer, conclusion):
        for condition in conditionals:
            instance_true = True
            for instance in condition:
                # Casting instance to a list so that the key value of the dict is obtained and by which the token also can be obtained
                if list(instance)[0] == answer and not instance[list(instance)[0]]:
                    instance[list(instance)[0]] = True
                if not instance[list(instance)[0]]:
                    instance_true = False
            if instance_true:
                conclusion[list(conclusion)[0]] = True
                self.find_goal(goals, list(conclusion)[0])
                temp_return = True
                break
            else:
                temp_return = False
        return temp_return

    # Finds the linked goal from the obtained fact
    def find_goal(self, goals, conclusion):
        for goal in goals:
            for answer in goal.answers:
                if list(answer[0])[0] == conclusion:
                    tmp_dict = answer[0]
                    tmp_dict[list(tmp_dict)[0]] = True
                    advise = answer[1]
                    self.obtained_goal.append(advise)
