from exp_parser import *

print("Testing expression results:")
expressions = open("./tests/exp_parser_tests/td_results.txt", "r").read().splitlines()
for exp in expressions:
    values=exp.split('=')
    try:
        exp_list = parse_expression(values[0])
    except:
        print(f"FAIL (Parsing): '{values[0]}'")
        continue

    if validate_expression(exp_list) == False:
        print(f"FAIL (Validation): '{values[0]}'")
        continue

    if eval_expression(exp_list) != values[1]:
        print(f"FAIL (Result): '{values[0]}'={values[1]}")
        result = eval_expression(exp_list)
        print(f"Result is->{result}")
        print(f"")
        continue

    print(f"OK: '{values[0]}'={values[1]}")
