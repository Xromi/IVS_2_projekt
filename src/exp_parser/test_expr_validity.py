import exp_parse
import exp_validate
import exp_eval

print("Testing VALID expressions:")
valid_expressions = open("test_exp_valid.txt", "r").read().splitlines()
for exp in valid_expressions:
    try:
        exp_list = exp_parse.parse_expression(exp)
    except:
        print(f"FAIL: {exp}")
        continue

    if exp_validate.validate_expression(exp_list) == False:
        print(f"FAIL: {exp}")
        continue

    print(f"OK: {exp}")

# separator
print(28* "-")

print("Testing INVALID expressions:")
invalid_expressions = open("test_exp_invalid.txt", "r").read().splitlines()
for exp in invalid_expressions:
    try:
        exp_list = exp_parse.parse_expression(exp)
    except:
        print(f"OK: {exp}")
        continue

    if exp_validate.validate_expression(exp_list) == False:
        print(f"OK: {exp}")
        continue

    print(f"FAIL: {exp}")
