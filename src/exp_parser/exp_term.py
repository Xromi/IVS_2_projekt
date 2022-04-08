import typing

class ExpTerm():
    # valid operators sorted by priority
    operators = ['-', '+', '/', '*', '%', '^', '!']

    type = None # "N" = number, "O" = operator, "(" = left bracket, ")" = right bracket
    val = None  # Depending on type: "N": float number | "O": operator | "(": "(" | ")": ")"

    def __get_type(self, raw_term) -> str:
        if type(raw_term) == float:
            return "N"
        elif type(raw_term) == str:
            if raw_term in self.operators:
                return "O"
            elif raw_term == '(':
                return "("
            elif raw_term == ')':
                return ")"

        raise TypeError("Unknown term.")

    def __init__(self, term_value: typing.Union[str, float]):
        self.type = self.__get_type(term_value)
        self.val = term_value

    def set(self, term_value: typing.Union[str, float]) -> None:
        self.type = self.__get_type(term_value)
        self.val = term_value

    def priority(self) -> int:
        try:
            return (self.operators.index(self.val) + 1)
        except:
            return 0
