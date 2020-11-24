import json
import operator
import argparse

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}


def convert(quantity, unit_1, unit_2):
    with open('data/conversions.json') as f:
        data = json.load(f)
    try:
        data[unit_1]
    except Exception:
        print("Unexpected error: The unit you entered is not available")
        raise
    calculation_type = data[unit_1][unit_2][0]
    return ops[calculation_type](float(quantity), float(data[unit_1][unit_2][1:]))


def si(physical_quantity, options=False):
    with open('data/si.json') as f:
        data = json.load(f)
    if options:
        return [key for key in data.keys()]
    else:
        try:
            data[physical_quantity]['unit_name']
        except Exception:
            print("Unexpected error: The quantity you entered is not available")
            raise
        return (data[physical_quantity]['unit_name'], data[physical_quantity]['symbol'],
                data[physical_quantity]['definition'])


def parse_arguments():
    parser = argparse.ArgumentParser(description="script for command line base calculations")
    tasks = parser.add_subparsers(
        title="subcommands", description="available tasks",
        dest="task", metavar="")
    system_unit = tasks.add_parser("si", help="basic SI unit ")
    system_unit.add_argument("-i", "--input", help="physical quantity")
    system_unit.add_argument("--options", action="store_true", help="help")
    conversions = tasks.add_parser("convert", help="convert units")
    conversions.add_argument("-i", "--input", required=True, help="value")
    conversions.add_argument("-b", "--base", required=True, help="base unit")
    conversions.add_argument("-c", "--convert", required=True, help="unit to convert")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    if args.task == "si":
        if args.options:
            print("Available options:")
            for option in (si(None, True)):
                print('- ' + option)
        elif args.input:
            # call si
            unit_name, symbol, definition = si(args.input)
            print(args.input + " has SI unit '" + unit_name + "' and the symbol is '" + symbol + "'")
    if args.task == "convert":
        # call convert
        value = convert(args.input, args.base, args.convert)
        print(args.input + args.base + " are " + str(value) + args.convert)
