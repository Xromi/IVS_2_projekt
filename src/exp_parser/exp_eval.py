## @file exp_eval.py
# @author David Klajbl, Marián Tarageľ
# @brief Evaluator of expressions
# @version 0.5
# @date 2022-04-12

from exp_preprocess import preprocess_expression
from math_lib import *
from exp_term import ExpTerm
import typing

def find_max_priority_index(expresion: typing.List[ExpTerm]) -> int:
    i = 0
    max_priority = 0
    max_index = 0
    while i < len(expresion):
        if max_priority < expresion[i].priority():
            max_priority = expresion[i].priority()
            max_index = i
        i += 1
    
    if max_priority == 0:
        return -1
    else:
        return max_index

def eval_subexp(sub_exp: typing.List[ExpTerm], index: int) -> typing.List[ExpTerm]:
    if sub_exp[index].value() == "+":
        result = my_add(sub_exp[index - 1].value(), sub_exp[index + 1].value())
    elif sub_exp[index].value() == "-":
        result = my_subtract(sub_exp[index - 1].value(), sub_exp[index + 1].value())
    elif sub_exp[index].value() == "*":
        result = my_multiply(sub_exp[index - 1].value(), sub_exp[index + 1].value())
    elif sub_exp[index].value() == "/":
        result = my_divide(sub_exp[index - 1].value(), sub_exp[index + 1].value())
    elif sub_exp[index].value() == "^":
        result = my_power(sub_exp[index - 1].value(), sub_exp[index + 1].value())
    elif sub_exp[index].value() == "%":
        result = my_modulo(sub_exp[index - 1].value(), sub_exp[index + 1].value())
    elif sub_exp[index].value() == "!":
        if sub_exp[index - 1].value() == int(sub_exp[index - 1].value()):
            result = my_factorial(int(sub_exp[index - 1].value()))
        else:
            result = my_factorial(sub_exp[index - 1].value())
        result = float(result)

    if sub_exp[index].value() == "!":
        sub_exp.pop(index - 1)
        sub_exp.pop(index - 1)
        sub_exp.insert(index - 1, ExpTerm(result))
    else:
        sub_exp.pop(index)
        sub_exp.pop(index)
        sub_exp.pop(index - 1)
        sub_exp.insert(index - 1, ExpTerm(result))

    return sub_exp

## @brief Evaluates expression represented by list of \ref exp_term.ExpTerm "ExpTerm" classes and returns its value.
# @param exp_list List of \ref exp_term.ExpTerm "ExpTerm" classes representing expression.
# @exception ValueError Exception ValueError is raised if invalid operations is to be executed (division by zero, factorial of negative number,...).
# @return Returns value of expression represented by list of \ref exp_term.ExpTerm "ExpTerm" classes.
def eval_expression(exp_list: typing.List[ExpTerm]) -> float:
    exp_list = preprocess_expression(exp_list)

    while True:
        i = 0
        open_bracket = 0
        close_bracket = 0
        while i < len(exp_list):
            if exp_list[i].type() == "(":
                open_bracket = i
            elif exp_list[i].type() == ")":
                close_bracket = i
            if open_bracket and close_bracket:
                break
            i += 1
        
        sub_exp = []
        for i in range(open_bracket, close_bracket + 1):
            sub_exp.append(exp_list[i])
        
        index = find_max_priority_index(sub_exp)
        while index != -1:
            sub_exp = eval_subexp(sub_exp, index)
            index = find_max_priority_index(sub_exp)
        
        count = 0
        while count < close_bracket - open_bracket + 1:
            exp_list.pop(open_bracket)
            count += 1
        exp_list.insert(open_bracket, sub_exp[1])

        if len(exp_list) == 1:
            break

    result = exp_list[0].value()
    
    return result
