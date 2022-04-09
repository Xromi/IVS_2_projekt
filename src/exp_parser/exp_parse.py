## @file exp_parse.py
# @author David Klajbl, Marián Tarageľ
# @brief Parser of expresion
# @version 0.2
# @date 2022-04-09

from exp_term import ExpTerm
from curses.ascii import isdigit
import typing


def _get_number_pos(start: int, exp_str: str) -> typing.Tuple[int, int]:
    end = start

    while end < len(exp_str) and isdigit(exp_str[end]):
        end += 1

    if end < len(exp_str) and exp_str[end] == '.':
        end += 1
        while end < len(exp_str) and isdigit(exp_str[end]):
            end += 1

    return start, end


def parse_expression(exp_str: str) -> typing.List[ExpTerm]:
    exp_list = []

    try:
        i = 0
        while i < len(exp_str):
            if isdigit(exp_str[i]):
                start, end = _get_number_pos(i, exp_str)

                exp_list.append(ExpTerm(float(exp_str[start:end])))

                i = end
            else:
                exp_list.append(ExpTerm(exp_str[i]))

                i += 1
    except:
        raise ValueError("Unable to parse expression.")

    return exp_list

def prepare_expresion_to_eval(exp_list: typing.List[ExpTerm]) -> typing.List[ExpTerm]:
    before = "None"
    length = len(exp_list)
    i = 0
    while i < length:
        if exp_list[i].type() == "(":
            if before == "N" or before == ")":
                exp_list.insert(i, ExpTerm("*"))
                length += 1

        if before == "None" or before == "(":
            if exp_list[i].value() == "+":
                exp_list.pop(i)
                length -= 1
            elif exp_list[i].value() == "-":
                exp_list.pop(i)
                value = exp_list[i].value()
                exp_list.pop(i)
                exp_list.insert(i, ExpTerm(-value))
                length -= 1
        
        before = exp_list[i].type()
        i += 1

    return exp_list
