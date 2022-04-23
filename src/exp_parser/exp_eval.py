## @file exp_eval.py
# @author David Klajbl, Marián Tarageľ
# @brief Evaluator of expressions
# @version 0.6
# @date 2022-04-21

from exp_parser.exp_preprocess import preprocess_expression
from exp_parser.exp_validate import validate_expression
from exp_parser.exp_term import ExpTerm
from math_lib import *
import typing

##
# @brief Function finds operator with the highest priority
# 
# @param expression list to search for operator
#
# @return position of operator with highest priority in list or -1 when opearator is not in list
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

## 
# @brief Fuction to evaluate subexpression
# subexpersion is expression with one operator which position is specified by index and numbers before and after operator
# 
# @param exp_list whole expresion list
# @param index position in exp_list where opearator can be found
#
# @return exp_list with operator and numbers replaced by their value or error rised from math_lib
def eval_subexp(exp_list: typing.List[ExpTerm], index: int) -> typing.List[ExpTerm]:
    if exp_list[index].value() == "+":
        try:
            result = my_add(exp_list[index - 1].value(), exp_list[index + 1].value())
        except TypeError:
            return TypeError
    elif exp_list[index].value() == "-":
        try:
            result = my_subtract(exp_list[index - 1].value(), exp_list[index + 1].value())
        except TypeError:
            return TypeError
    elif exp_list[index].value() == "*":
        try:
            result = my_multiply(exp_list[index - 1].value(), exp_list[index + 1].value())
        except ZeroDivisionError:
            return ZeroDivisionError
    elif exp_list[index].value() == "/":
        try:
            result = my_divide(exp_list[index - 1].value(), exp_list[index + 1].value())
        except TypeError:
            return TypeError
        except ZeroDivisionError:
            return ZeroDivisionError
    elif exp_list[index].value() == "^":
        try:
            result = my_power(exp_list[index - 1].value(), exp_list[index + 1].value())
        except TypeError:
            return TypeError
        except ValueError:
            return ValueError
        except OverflowError:
            return OverflowError
    elif exp_list[index].value() == "%":
        try:
            result = my_modulo(exp_list[index - 1].value(), exp_list[index + 1].value())
        except TypeError:
            return TypeError
    elif exp_list[index].value() == "!":
        if exp_list[index - 1].value() == int(exp_list[index - 1].value()):
            try:
                result = my_factorial(int(exp_list[index - 1].value()))
                result = float(result)
            except TypeError:
                return TypeError
            except OverflowError:
                return OverflowError
        else:
            try:
                result = my_factorial(exp_list[index - 1].value())
                result = float(result)
            except TypeError:
                return TypeError
            except OverflowError:
                return OverflowError

    if exp_list[index].value() == "!":
        exp_list.pop(index - 1)
        exp_list.pop(index - 1)
        exp_list.insert(index - 1, ExpTerm(result))
    else:
        exp_list.pop(index)
        exp_list.pop(index)
        exp_list.pop(index - 1)
        exp_list.insert(index - 1, ExpTerm(result))

    return exp_list

## 
# @brief Evaluates expression represented by list of \ref exp_term.ExpTerm "ExpTerm" classes.
#
# @param exp_list List of \ref exp_term.ExpTerm "ExpTerm" classes representing expression.
#
# @return Returns value of expression represented by list of \ref exp_term.ExpTerm "ExpTerm" classes or Error message.
def eval_expression(exp_list: typing.List[ExpTerm]) -> str:
    if validate_expression(exp_list) == False:
        return "InvalidExpression"

    if len(exp_list) == 0:
        return ""

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
            if sub_exp == ZeroDivisionError:
                return "ZeroDivisionError"
            elif sub_exp == TypeError:
                return "InvalidExpression"
            elif sub_exp == ValueError:
                return "InvalidExpression"
            elif sub_exp == OverflowError:
                return "OverflowError"
            index = find_max_priority_index(sub_exp)
        
        count = 0
        while count < close_bracket - open_bracket + 1:
            exp_list.pop(open_bracket)
            count += 1
        exp_list.insert(open_bracket, sub_exp[1])

        if len(exp_list) == 1:
            break

    result = exp_list[0].value()
    if result == int(result):
        try:
            result = int(result)
        except ValueError:
            return "InvalidExpression"

    result = str(result)
    
    return result
