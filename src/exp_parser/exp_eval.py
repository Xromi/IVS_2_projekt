## @file exp_eval.py
# @author David Klajbl, Marián Tarageľ
# @brief Evaluator of expressions
# @version 0.3
# @date 2022-04-11

from exp_term import ExpTerm
import typing

# creates deep copy of ExpTerm list
def _create_exp_list_copy(exp_list: typing.List[ExpTerm]) -> typing.List[ExpTerm]:
    exp_list_copy = []
    for term in exp_list:
        exp_list_copy.append(ExpTerm(term.value()))
    return exp_list_copy

# preprocesses expression before eval, whole expression is put in bracket, signedness is applied and implicit multiplication is inserted
def _preprocess_expression(exp_list: typing.List[ExpTerm]) -> None:
    # bracket whole expression
    exp_list.insert(0, ExpTerm("("))
    exp_list.append(ExpTerm(")"))

    # apply signedness
    i = 1
    while i < len(exp_list)-1:
        if exp_list[i].value() in ["+", "-"] and exp_list[i+1].type() == "N":
            if exp_list[i-1].value() in ["(", "^", "/", "*", "%"]:
                # '(+3' -> '(3' | '5^+3' -> '5^3' | '5/+3' -> '5/3' | '5*+3' -> '5*3' | '5%+3' -> '5%3'
                if exp_list[i].value() == "-":
                    exp_list[i+1].set(-exp_list[i+1].value())
                exp_list.pop(i)
        i += 1

    # insert implicit multiplications
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

def find_subexpresion(exp_list: typing.List[ExpTerm]) -> typing.List[ExpTerm]:
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
    
    sub_term = []
    for i in range(open_bracket, close_bracket + 1):
        sub_term.append(exp_list[i])
    
    return sub_term

def find_max_priority_index(expresion: typing.List[ExpTerm]) -> int:
    i = 0
    max_priority = 0
    max_index = 0
    while i < len(expresion):
        if max_priority < expresion[i].priority():
            max_priority = expresion[i].priority()
            max_index = i
        i += 1
    
    return max_index

## @brief Evaluates expression represented by list of \ref exp_term.ExpTerm "ExpTerm" classes and returns its value.
# @param exp_list List of \ref exp_term.ExpTerm "ExpTerm" classes representing expression.
# @exception ValueError Exception ValueError is raised if invalid operations is to be executed (division by zero, factorial of negative number,...).
# @return Returns value of expression represented by list of \ref exp_term.ExpTerm "ExpTerm" classes.
def eval_expression(exp_list: typing.List[ExpTerm]) -> float:
    exp_list_copy = _create_exp_list_copy(exp_list)
    _preprocess_expression(exp_list_copy)
    return 0
