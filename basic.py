import sys
import json
import operator
import argparse



ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

def convert(quantity, unit_1, unit_2):
    with open('data/conversions.json') as f:
        data = json.load(f)
    if unit_1 not in data:
        print("Not an available unit")
        return(None,None)
    else:
        calculation_type = data[unit_1][unit_2][0]
        return(ops[calculation_type](float(quantity),float(data[unit_1][unit_2][1:])))


def si(physical_quantity):
    with open('data/si.json') as f:
        data = json.load(f)
    unit_name, symbol, definition = data[physical_quantity]['unit_name'], data[physical_quantity]['symbol'], data[physical_quantity]['definition']
    return(unit_name, symbol, definition)

def parse_arguments():
    parser = argparse.ArgumentParser(description="A demonstration script "
                                                 "for pyAudioAnalysis library")
    tasks = parser.add_subparsers(
        title="subcommands", description="available tasks",
        dest="task", metavar="")
    si = tasks.add_parser("si",
                                 help="basic SI unit ")
    si.add_argument("-i", "--input", required=True, help="physical quantity")
    convert = tasks.add_parser("convert",
                                 help="convert units")
    convert.add_argument("-i", "--input", required=True, help="value")
    convert.add_argument("-b", "--base", required=True, help="base unit")
    convert.add_argument("-c", "--convert", required=True, help="unit to convert")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    if args.task == "si":
        # call si
        unit_name, symbol, definition = si(args.input)
        print(args.input + " has SI unit '" + unit_name + "' and the symbol is '" + symbol + "'")
    if args.task == "convert":
        # call convert
        value = convert(args.input, args.base, args.convert)
        print(args.input + args.base + " are " + str(value) +args.convert)