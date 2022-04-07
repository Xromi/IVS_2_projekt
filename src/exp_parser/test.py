import exp_parse
import exp_validate

expressions = open('test.txt', 'r').read().splitlines()

for exp in expressions:
    exp_list = exp_parse.parse_expression(exp)
    if not exp_list and exp:
        print(f"Unable to parse expression string [{exp}].")
        exit(1)

    if not exp_validate.validate_expression(exp_list):
        print(f"Expression [{exp}] has invalid syntax.")
        exit(1)

    print(f"Expression [{exp}] is valid.")
