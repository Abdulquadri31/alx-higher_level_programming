#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Parse the arguments
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Map of operators to functions
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    # Check if the operator is valid
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform the operation and print the result
    result = operations[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
