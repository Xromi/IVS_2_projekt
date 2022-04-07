from exp_term import ExpTerm
import typing


def _check_brackets(exp_list: typing.List[ExpTerm]) -> bool:
    bracket_counter = 0

    for i in range(len(exp_list)):
        if exp_list[i].type == "(":
            bracket_counter += 1
        elif exp_list[i].type == ")":
            bracket_counter -= 1

        if bracket_counter < 0:
            return False

    if bracket_counter != 0:
        return False
    else:
        return True


def _check_term_match(term: ExpTerm, pattern: str) -> bool:
    if term == None:
        t = "_"
    elif term.type == "O":
        t = term.val
    else:
        t = term.type

    if pattern != "" and t not in pattern:
        return False
    else:
        return True


def _check_term_syntax(left_term: ExpTerm, term: ExpTerm, right_term: ExpTerm) -> bool:
    left_pattern = ""
    right_pattern = ""

    if term.type == "O":
        if term.val == "!":
            left_pattern = ")N"
        elif term.val in ["+", "-"]:
            left_pattern = "()N!"
            right_pattern = "(N+-"
        elif term.val in ["*", "/", "%", "^"]:
            left_pattern = ")N!*/^%_"
            right_pattern = "(N"
    elif term.type == "(":
        right_pattern = "(N+-"
    elif term.type == ")":
        left_pattern = ")N!"
    elif term.type == "N":
        left_pattern = "()*/%^+-!_"
        right_pattern = "()*/%^+-!_"

    if not _check_term_match(left_term, left_pattern) or not _check_term_match(right_term, right_pattern):
        return False
    else:
        return True


def _check_syntax(exp_list: typing.List[ExpTerm]) -> bool:
    for i in range(len(exp_list)):
        if i > 0:
            left_term = exp_list[i-1]
        else:
            left_term = None

        if i < len(exp_list)-1:
            right_term = exp_list[i+1]
        else:
            right_term = None

        if not _check_term_syntax(left_term, exp_list[i], right_term):
            return False

    return True


def validate_expression(exp_list: typing.List[ExpTerm]) -> bool:
    if not _check_brackets(exp_list) or not _check_syntax(exp_list):
        return False
    else:
        return True
