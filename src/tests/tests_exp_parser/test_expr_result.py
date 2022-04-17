from exp_parser import *

print("Testing expression results:")
expressions = open("./tests/tests_exp_parser/test_exp_results.txt", "r").read().splitlines()
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

    if eval_expression(exp_list) != float(values[1]):
        print(f"FAIL (Result): '{values[0]}'?={values[1]}")
        continue

    print(f"OK: '{values[0]}'={values[1]}")
