## @file exp_eval.py
# @author David Klajbl, Marián Tarageľ
# @brief Evaluator of expressions
# @version 0.4
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

    i = 1
    while i < len(exp_list):
        if exp_list[i].value() == "^" and exp_list[i + 1].value() != "(":
            exp_list.insert(i + 1, ExpTerm("("))
            exp_list.append(ExpTerm(")"))

        i += 1



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
    if sub_exp[index].value() == "-":
        result = sub_exp[index - 1].value() - sub_exp[index + 1].value()
    elif sub_exp[index].value() == "+":
        result = sub_exp[index - 1].value() + sub_exp[index + 1].value()
    elif sub_exp[index].value() == "/":
        result = sub_exp[index - 1].value() / sub_exp[index + 1].value()
    elif sub_exp[index].value() == "*":
        result = sub_exp[index - 1].value() * sub_exp[index + 1].value()
    elif sub_exp[index].value() == "%":
        result = sub_exp[index - 1].value() % sub_exp[index + 1].value()
    elif sub_exp[index].value() == "^":
        result = sub_exp[index - 1].value() ** sub_exp[index + 1].value()
    
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
    exp_list_copy = _create_exp_list_copy(exp_list)
    _preprocess_expression(exp_list_copy)

    while True:
        i = 0
        open_bracket = 0
        close_bracket = 0
        while i < len(exp_list_copy):
            if exp_list_copy[i].type() == "(":
                open_bracket = i
            elif exp_list_copy[i].type() == ")":
                close_bracket = i
            if open_bracket and close_bracket:
                break
            i += 1
        
        sub_exp = []
        for i in range(open_bracket, close_bracket + 1):
            sub_exp.append(exp_list_copy[i])
        
        index = find_max_priority_index(sub_exp)
        while index != -1:
            sub_exp = eval_subexp(sub_exp, index)
            index = find_max_priority_index(sub_exp)
        
        count = 0
        while count < close_bracket - open_bracket + 1:
            exp_list_copy.pop(open_bracket)
            count += 1
        exp_list_copy.insert(open_bracket, sub_exp[1])

        if len(exp_list_copy) == 1:
            break

    result = exp_list_copy[0].value()
    
    return result
