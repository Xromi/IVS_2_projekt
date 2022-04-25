from calculateit.exp_parser.exp_parse import parse_expression
from calculateit.exp_parser.exp_validate import validate_expression
from calculateit.exp_parser.exp_eval import eval_expression

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
    
    result = eval_expression(exp_list)

    try: # convert result to either float (with 8 decimals) or to int and then back to string
        result = float(result)
        if(result != int(result)):
            result = round(result, 8)
        else:
            result = int(result)
        result = str(result)
    except:
        pass

    if result != values[1]:
        print(f"FAIL (Result): '{values[0]}'={values[1]}")
        print(f"Result is->{result}")
        print(f"")
        continue

    print(f"OK: '{values[0]}'={values[1]}")
