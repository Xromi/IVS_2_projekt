
class ExpTerm():
    operators = ['!', '^', '%', '*', '/', '+', '-']

    type = None
    val = None

    def __init__(self, term):
        if type(term) == float:
            self.type = "N"
            self.val = term
        elif type(term) == str:
            if term in self.operators:
                self.type = "O"
                self.val = term
            elif term == '(' or term == ')':
                self.type = term
            else:
                raise ValueError("Wrong term value.")
        else:
            raise TypeError("Wrong term type.")

    def priority(self):
        if self.type == "O":
            try:
                return self.operators.index(self.val)
            except:
                return None
        else:
            return None
