## @file exp_term.py
# @author David Klajbl
# @brief Implementation of ExpTerm class
# @version 0.1
# @date 2022-04-09

import typing

## @brief ExpTerm class representing expression term.
# Expression term is represented by its **type** and **value**. 
# - **type**
#       - can be either number, operator, left bracket or right bracket
#       - each type is represented by corresponding string value:
#           - "N" = number
#           - "O" = operator
#           - "(" = left bracket
#           - ")" = right bracket
# - **value**
#       - representation depends on ExpTerm type:
#           - if type is "N", value is represented as float number
#           - if type is "O", value is either "-", "+", "/", "*", "%", "^" or "!" string
#           - if type is "(", value is "(" string
#           - if type is ")", value is ")" string
class ExpTerm():

    # valid operators sorted by priority
    __operators = ["-", "+", "/", "*", "%", "^", "!"]

    # returns ExpTerm type of term_value, if value does not correspond to any type ValueError is raised
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

        raise ValueError("Unknown term.")

    ## @brief ExpTerm constructor.
    # Initialises ExpTerm type and value.
    # @param term_value Initial value of ExpTerm.
    # @exception ValueError Raises ValueError exception if term_value does not correspond to any ExpTerm type.
    def __init__(self, term_value: typing.Union[str, float]):
        self.set(term_value)

    ## @brief Sets new ExpTerm type and value.
    # @param new_term_value New value of ExpTerm.
    # @exception ValueError Raises ValueError exception if new_term_value does not correspond to any ExpTerm type.
    def set(self, new_term_value: typing.Union[str, float]) -> None:
        self.__type = self.__get_type(new_term_value)
        self.__value = new_term_value

    ## @brief Returns value of ExpTerm.
    # @return Value of ExpTerm.
    def value(self) -> typing.Union[str, float]:
        return self.__value

    ## @brief Returns type of ExpTerm.
    # @return Type of ExpTerm.
    def type(self) -> str:
        return self.__type

    ## @brief Returns priority of ExpTerm.
    # @return   If ExpTerm type is operator, positive, non zero integer is returned (bigger number represents higher priority).
    #           If ExpTerm type is not operator, zero is returned.
    def priority(self) -> int:
        try:
            return (self.__operators.index(self.__value) + 1)
        except:
            return 0

    ## @brief Returns string representation of ExpTerm value.
    def __str__(self) -> str:
        return str(self.__value)
