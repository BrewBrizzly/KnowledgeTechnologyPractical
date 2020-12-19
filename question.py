
# responsible for parsing a question to the knowledge base
class Question(object):

    # Constructor 
    def __init__(self, question):
        print("I'm a question")
        self.question = question
        self.description = ''
        self.option = list()
        self.make_question()
        print(self.description)
        print(self.option)

    # Makes a question 
    def make_question(self):
        for child in self.question:
            if child.tag == 'description':
                self.description = child.text
            if child.tag == 'option':
                self.make_option(child)

    # Makes a option for a question 
    def make_option(self, parent):
        tmp_option = ''
        tmp_conclusion = {}
        for child in parent:
            if child.tag == 'description':
                tmp_option = child.text
            if child.tag == 'then':
                tmp_conclusion.update(self.make_conclusion(child))
        self.option.append({'option': tmp_option, 'conclusion': tmp_conclusion})

    # Makes a conclusion for a option
    def make_conclusion(self, parent):
        tmp_conclusion = {}
        for child in parent:
            tmp_conclusion.update({child.text : True})
        return(tmp_conclusion)
