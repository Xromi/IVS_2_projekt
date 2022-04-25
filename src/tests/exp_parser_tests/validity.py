from calculateit.exp_parser.exp_parse import parse_expression
from calculateit.exp_parser.exp_validate import validate_expression

print("Testing VALID expressions:")
valid_expressions = open("./tests/exp_parser_tests/td_valid.txt", "r").read().splitlines()
for exp in valid_expressions:
    try:
        exp_list = parse_expression(exp)
    except:
        print(f"FAIL: {exp}")
        continue

    if validate_expression(exp_list) == False:
        print(f"FAIL: {exp}")
        continue

    print(f"OK: {exp}")

# separator
print(28* "-")

print("Testing INVALID expressions:")
invalid_expressions = open("./tests/exp_parser_tests/td_invalid.txt", "r").read().splitlines()
for exp in invalid_expressions:
    try:
        exp_list = parse_expression(exp)
    except:
        print(f"OK: {exp}")
        continue

    if validate_expression(exp_list) == False:
        print(f"OK: {exp}")
        continue

    print(f"FAIL: {exp}")
