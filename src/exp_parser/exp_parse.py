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
