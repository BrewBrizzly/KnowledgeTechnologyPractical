
# responsible for parsing a question to the knowledge base
class Question(object):

    def __init__(self, question):
        print("I'm a question")
        self.question = question
        self.description = ''
        self.fact = ''
        self.attributes = list()
        self.make_question()

    def make_question(self):
        for node in self.question:
            if node.tag == 'description':
                self.description = node.text
            if node.tag == 'option':
                self.attributes.append(node)
