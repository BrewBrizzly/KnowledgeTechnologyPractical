
# Responsible for parsing a question to the knowledge base
class Question(object):

    # Constructor 
    def __init__(self, question):
        print("I'm a question")
        self.question = question
        self.description = ''
        self.option = list()
        self.make_question()
        print("description")
        print(self.description)
        print("options")
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
        tmp_option = list()
        for child in parent:
            # description of the option always appended to the first index of the list 
            if child.tag == 'description':
                tmp_option.append(child.text)
            # the consequence of the option is appended after the description of the option
            if child.tag == 'then':
                for conclusion in child:
                    tmp_option.append({conclusion.text: True})
        self.option.append(tmp_option)
