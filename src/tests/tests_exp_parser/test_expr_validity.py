from exp_parser import *

print("Testing VALID expressions:")
valid_expressions = open("./tests/tests_exp_parser/test_exp_valid.txt", "r").read().splitlines()
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
invalid_expressions = open("./tests/tests_exp_parser/test_exp_invalid.txt", "r").read().splitlines()
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
