import json
import operator
import argparse
import re


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}


def mass_to_moles(compound, mass):
    mr = molecular_properties(compound)
    moles = float(mass) / mr
    return moles


def moles_to_mass(compound, moles):
    mr = molecular_properties(compound)
    mass = float(moles) * float(mr)
    return mass


def molecular_properties(compound):
    parentheses = re.findall(r'\(.*?\)\d+|\(.*?\)', compound)  # get compounds inside parentheses
    elements = re.findall(r'[A-Z][^A-Z]*', re.sub(r'\(.*?\)\d+|\(.*?\)', '',
                                                  compound))  # get compounds outside of parentheses
    mr = 0
    for compound in parentheses:
        compound_moles = (re.findall(r'\)(\d+)', compound))
        if not compound_moles:
            compound_moles = 1
        else:
            compound_moles = compound_moles[0]
        compound_base = re.sub(r'(\(|\)\d+|\))', '', compound)
        # split on elements
        sub_elements = re.findall(r'[A-Z][^A-Z]*', compound_base)
        value = 0
        for element in sub_elements:
            amount = re.findall(r'[0-9]', element)
            if not amount:
                amount.append(1)
            element = re.sub(str(amount[0]), '', element)
            value += float(atomic_properties(element)[0]) * float(amount[0])
        value = float(value) * float(compound_moles)
        mr += float(value)

    for element in elements:
        amount = re.findall('[0-9]', element)
        if not amount:
            amount.append(1)
        element = re.sub(str(amount[0]), '', element)
        value = float(atomic_properties(element)[0]) * float(amount[0])
        mr += float(value)
    return mr


def atomic_properties(element):
    with open('data/elements.json') as f:
        data = json.load(f)
    try:
        data[element]
    except Exception:
        print("\n-----Error-----\nUnexpected error: The element you entered is not available"
              "\n---------------\n")
        raise
    return data[element]['atomic_weight'], data[element]['atomic_number']


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
            print("\n-----Error-----\nUnexpected error: The quantity you entered is not available"
                  "\nPlease run 'python basic.py si --options' to see the available options\n---------------\n")
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

    atomic_weights = tasks.add_parser("atom_weight", help="atomic weights")
    atomic_weights.add_argument("-i", "--input", required=True, help="element")

    molecular_weights = tasks.add_parser("mol_weight", help="molecular weights")
    molecular_weights.add_argument("-i", "--input", required=True, help="compound")

    molestomass = tasks.add_parser("mol_to_mass", help="moles to mass")
    molestomass.add_argument("-m", "--moles", required=True, help="moles")
    molestomass.add_argument("-i", "--input", required=True, help="compound")

    masstomoles = tasks.add_parser("mass_to_mol", help="moles to mass")
    masstomoles.add_argument("-m", "--mass", required=True, help="mass")
    masstomoles.add_argument("-i", "--input", required=True, help="compound")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    if args.task == "si":
        if args.options:
            print("Available options:")
            for option in (si(None, True)):
                print('- ' + option)
        elif args.input:
            # call si and print output
            print(args.input + " has SI unit '" + si(args.input)[0] + "' and the symbol is '" + si(args.input)[1] + "'")
    if args.task == "convert":
        # call convert and print output
        print(args.input + args.base + " are " + str(convert(args.input, args.base, args.convert)) + args.convert)
    if args.task == "atom_weight":
        # call atomic_weights and print output
        print(args.input + " has atomic weight " + atomic_properties(args.input)[0] + "u " + "and atomic number " +
              atomic_properties(args.input)[1])
    if args.task == "mol_weight":
        # call molecular_weight and print output
        print(molecular_properties(args.input))
    if args.task == "mol_to_mass":
        # call molecular_weight and print output
        print(moles_to_mass(args.input, args.moles))
    if args.task == "mass_to_mol":
        # call molecular_weight and print output
        print(mass_to_moles(args.input, args.mass))
