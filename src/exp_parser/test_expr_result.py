import exp_parse
import exp_validate
import exp_eval

print("Testing expression results:")
expressions = open("test_exp_results.txt", "r").read().splitlines()
for exp in expressions:
    values=exp.split('=')
    try:
        exp_list = exp_parse.parse_expression(values[0])
    except:
        print(f"FAIL (Parsing): '{values[0]}'")
        continue

    if exp_validate.validate_expression(exp_list) == False:
        print(f"FAIL (Validation): '{values[0]}'")
        continue

    if exp_eval.eval_expression(exp_list) != float(values[1]):
        print(f"FAIL (Result): '{values[0]}'?={values[1]}")
        continue

    print(f"OK: '{values[0]}'={values[1]}")
