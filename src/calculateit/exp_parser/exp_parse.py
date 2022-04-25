## @file exp_parse.py
# @author David Klajbl, Marián Tarageľ
# @brief Parser of expresion
# @version 0.1
# @date 2022-04-10

from ..exp_parser.exp_term import ExpTerm
from curses.ascii import isdigit
import typing

# returns end position of number substring in exp_str beginning on index start
def _get_number_pos(start: int, exp_str: str) -> typing.Tuple[int, int]:
    end = start

    while end < len(exp_str) and isdigit(exp_str[end]):
        end += 1

    if end < len(exp_str) and exp_str[end] == '.':
        end += 1
        while end < len(exp_str) and isdigit(exp_str[end]):
            end += 1

    return end

## @brief Parses expression string into list of \ref exp_term.ExpTerm "ExpTerm" classes.
# @param exp_str Expression string.
# @exception ValueError Raises ValueError expression when expression string can not be converted into \ref exp_term.ExpTerm "ExpTerm" class list
# (invalid representation of number, invalid string character,...).
# @return Returns list of \ref exp_term.ExpTerm "ExpTerm" classes representing expression.
def parse_expression(exp_str: str) -> typing.List[ExpTerm]:
    exp_list = []

    try:
        i = 0
        while i < len(exp_str):
            if isdigit(exp_str[i]):
                end = _get_number_pos(i, exp_str)

                exp_list.append(ExpTerm(float(exp_str[i:end])))

                i = end
            else:
                exp_list.append(ExpTerm(exp_str[i]))

                i += 1
    except:
        raise ValueError("Unable to parse expression.")

    return exp_list
