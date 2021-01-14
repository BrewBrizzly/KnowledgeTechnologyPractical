#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

# Responsible for parsing a goal to the knowledge base
class Goal(object):

    # Assigning the root node, creating a list containing the answers of the xml and running make_goal 
    def __init__(self, goal):
        self.goal = goal
        self.answers = list()
        self.make_goal()

    # Adds a dict pair of each goal to the goal list
    # [[{value : truth}, recommendation]]
    def make_goal(self):
        for answer in self.goal:
            if answer.tag == 'answer':
                self.answers.append([{answer.attrib[list(answer.attrib)[0]]: False}, answer.text])