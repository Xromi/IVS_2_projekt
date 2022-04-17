from exp_parser.exp_term import ExpTerm
import math_lib as math_lib
import typing

def _evaluate_constants(exp_list: typing.List[ExpTerm]) -> None:
    i = 0
    while i < len(exp_list):
        if exp_list[i].type() == "C":
            if exp_list[i].value() == "e":
                exp_list[i].set(math_lib.e)
            elif exp_list[i].value() == "π":
                exp_list[i].set(math_lib.pi)
        i += 1

def _apply_signedness(exp_list: typing.List[ExpTerm]) -> None:
    i = 1
    while i < len(exp_list)-1:
        if exp_list[i].value() in ["+", "-"] and exp_list[i+1].type() == "N":
            if exp_list[i-1].value() in ["(", "^", "/", "*", "%"]:
                # '(+3' -> '(3' | '5^+3' -> '5^3' | '5/+3' -> '5/3' | '5*+3' -> '5*3' | '5%+3' -> '5%3'
                if exp_list[i].value() == "-":
                    exp_list[i+1].set(-exp_list[i+1].value())
                exp_list.pop(i)
        i += 1

def _insert_implicit_multiplication(exp_list: typing.List[ExpTerm])  -> None:
    i = 1
    while i < len(exp_list):
        if exp_list[i].type() == "(" and (exp_list[i-1].type() == "N" or exp_list[i-1].value() in [")", "!"]):
            # '3()' -> '3*()' | '()()' -> '()*()' | '3!()' -> '3!*()'
            exp_list.insert(i, ExpTerm("*"))
            i += 1
        elif exp_list[i].type() == "N" and exp_list[i-1].value() in [")", "!"]:
            # '()3' -> '()*3' | '2!3' -> '2!*3'
            exp_list.insert(i, ExpTerm("*"))
            i += 1
        i += 1

# preprocesses expression before eval, whole expression is put in brackets, constants are replaced by their values, signedness is applied and implicit multiplication is inserted
def preprocess_expression(exp_list: typing.List[ExpTerm]) -> typing.List[ExpTerm]:
    # bracket whole expression
    exp_list.insert(0, ExpTerm("("))
    exp_list.append(ExpTerm(")"))

    _evaluate_constants(exp_list)

    _apply_signedness(exp_list)

    _insert_implicit_multiplication(exp_list)

    return exp_list