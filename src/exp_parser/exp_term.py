import typing

class ExpTerm():
    # valid operators sorted by priority
    __operators = ['-', '+', '/', '*', '%', '^', '!']

    # "N" = number, "O" = operator, "(" = left bracket, ")" = right bracket
    # Depending on type: "N": float number | "O": operator | "(": "(" | ")": ")"

    def __get_type(self, term_value) -> str:
        if type(term_value) == float:
            return "N"
        elif type(term_value) == str:
            if term_value in self.__operators:
                return "O"
            elif term_value == '(':
                return "("
            elif term_value == ')':
                return ")"

        raise TypeError("Unknown term.")

    def __init__(self, term_value: typing.Union[str, float]):
        self.__type = self.__get_type(term_value)
        self.__value = term_value

    def set(self, term_value: typing.Union[str, float]) -> None:
        self.__type = self.__get_type(term_value)
        self.__value = term_value

    def value(self) -> typing.Union[str, float]:
        return self.__value

    def type(self) -> str:
        return self.__type

    def priority(self) -> int:
        try:
            return (self.__operators.index(self.__value) + 1)
        except:
            return 0

    def __str__(self) -> str:
        return str(self.__value)
