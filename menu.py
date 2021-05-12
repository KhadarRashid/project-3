def __init__(self):
    self.text_descriptions = {}
    self.functions = {}

def add_option(self, key, description, funct):
    self.text_descriptions[key] = description
    self.functions[key]= funct

def get_action(self, choice):
    return self.functions.get(choice)

def __str__(self):
    # return menu options/descriptions
    return