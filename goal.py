
# Responsible for parsing a goal to the knowledge base
class Goal(object):

	# Constructor
    def __init__(self, goal):
        print("I'm a goal")
        self.goal = goal
        self.answers = list()
        self.make_goal()
        print(self.answers)

    # Adds a dict pair of each goal to the goal list
    def make_goal(self):
        for answer in self.goal:
            if answer.tag == 'answer':
                self.answers.append({answer.text: False})
