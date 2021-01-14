#Authors: Stephan Nijdam (S3690970), Lennard Bornemann (S3576981), Sophie van Schaik (s3363937)

# Responsible for parsing a question to the knowledge base
class Question(object):

    # Assigning the root node, creating a list option containing the option(s) of a question and running make_question
    def __init__(self, question):
        self.question = question
        self.description = ''
        self.option = list()
        self.make_question()

    # Makes a question with the idea that each question contains one description, the actual question, and one or more options.
    # A questions object thus only contains one description, and a list containing one or more lists in which, on the zeroth index, the description of
    # the option is stored and, on the first index, a dict is stored with the consequence of the option included its truth value.
    # Example of the option list: [['description', {consequence: truth value}], ['description', {consequence: truth value}]]
    def make_question(self):
        for child in self.question:
            if child.tag == 'description':
                self.description = child.text
            if child.tag == 'option':
                self.make_option(child)

    # Makes a option for a question in the form: ['description', {consequence: truth value}]
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
