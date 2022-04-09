import typing
from exp_term import ExpTerm

def _create_exp_list_copy(exp_list: typing.List[ExpTerm]) -> typing.List[ExpTerm]:
    exp_list_copy = []
    for term in exp_list:
        exp_list_copy.append(ExpTerm(term.value()))
    return exp_list_copy

def _preprocess_expression(exp_list: typing.List[ExpTerm]) -> None:
    # bracket whole expression
    exp_list.insert(0, ExpTerm("("))
    exp_list.append(ExpTerm(")"))

    # apply signedness
    i = 1
    while i < len(exp_list)-1:
        if exp_list[i].value() in ["+", "-"] and exp_list[i+1].type() == "N":
            if exp_list[i-1].value() in ["(", "^", "/", "*", "%"]:
                if exp_list[i].value() == "-":
                    exp_list[i+1].set(-exp_list[i+1].value())
                exp_list.pop(i)
        i += 1

    # insert implicit multiplications
    i = 1
    while i < len(exp_list):
        inserted = False
        if exp_list[i].type() == "(":
            if exp_list[i-1].type() == "N" or exp_list[i-1].value() in [")", "!"]:
                exp_list.insert(i, ExpTerm("*"))
                i += 1
        elif exp_list[i].type() == "N" and exp_list[i-1].value() in [")", "!"]:
            exp_list.insert(i, ExpTerm("*"))
            i += 1
        
        i += 1

def eval_expression(exp_list: typing.List[ExpTerm]) -> bool:
    exp_list_copy = _create_exp_list_copy(exp_list)
    _preprocess_expression(exp_list_copy)
