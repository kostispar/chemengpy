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
    unit_name = data[physical_quantity]['unit_name']
    symbol = data[physical_quantity]['symbol']
    definition = data[physical_quantity]['definition']
    return(unit_name, symbol, definition)

def main():
    function = sys.argv[1]
    if function == "si":
        physical_quantity = sys.argv[2]
        unit_name, symbol, definition = si(physical_quantity)
        print(sys.argv[2]+ " has SI unit '"+ unit_name+ "' and the symbol is '"+ symbol+"'")
    if function == "convert":
        quantity = sys.argv[2]
        unit_1 = sys.argv[3]
        unit_2 = sys.argv[4]
        value = convert(quantity, unit_1, unit_2)
        print(quantity + unit_1 + " are " + str(value) + unit_2)

if __name__ == "__main__":
    main()