import argparse

from app import calculator

OPERATIONS = {
    "add" : calculator.add,
    "substract": calculator.subtract,
    "multiply" : calculator.multiply,
    "divide" : calculator.divide,
}

def main(argv: list[str] | None= None) -> int:
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("operation", choices=OPERATIONS.keys(), help="Operation to perform")
    parser.add_argument("a", type=float, help="First operand")
    parser.add_argument("b", type=float, help="Second operand")

    args = parser.parse_args(argv)

    operation_func = OPERATIONS[args.operation]
    result = operation_func(args.a, args.b)
    print(f"Result: {result}")

    return 0

    try:
        result = OPERATIONS[args.operation](args.a, args.b)
    except ValueError as error:
        print(f"Error: {error}")
        return 1

    print(f"{result:g}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
