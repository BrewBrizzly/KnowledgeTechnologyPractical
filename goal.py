

class Goal(object):

    def __init__(self, goal):
        print("I'm a goal")
        self.goal = goal
        self.answers = list()
        self.make_goal()

    def make_goal(self):
        for answer in self.goal:
            if answer.tag == 'answer':
                self.answers.append(answer)
