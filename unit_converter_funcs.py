#  All project functions

from unit_converter_lists import *


# I wrote this code in main, but realized at the very end I needed to
# re-run it unless the conv_solid and conv_liquid functions wouldn't work
# So to save space I just made a function

def measure_system_check(item_unit):
    """Confirms which measuring system is being used for the below three functions to work with"""
    if item_unit in imperial_units:
        measure_system = "imperial"
    else:  # the item unit must be metric then
        measure_system = "metric"
    return measure_system


# Same story for this code, made this function to save space

def display_units(item_type):
    """Displays tuple of acceptable inputs for user to see"""
    if item_type == "solid":
        print("Accepted solid units:")
        print(combined_solids)
        print("-------")
    else:  # Then it was a liquid
        print("Accepted liquid units:")
        print(combined_liquids)
        print("-------")


def conv_to_base(weight, item_unit, measure_system):

    """This will convert the input (weight user desires to convert to another value)
    into grams, ml (Which are both the same) or solid/liquid ounce to standardize, making the next
    conversion easier to code"""

    if item_unit in combined_solids:  # ... Then convert solid weight variable to grams
        # imperial to solid ounces first
        if measure_system == "imperial":
            if item_unit == "pound":
                weight *= 16
            elif item_unit == "stone":
                weight *= 224
            else:  # Already solid ounce. No change needed
                weight *= 1
            # Now turn it into grams
            weight *= 28.35

        # metric to grams
        else:  # It must already be metric then
            if item_unit == "milligram":
                weight *= 0.001
            elif item_unit == "kilogram":
                weight *= 1000
            else:  # it's gram, no need to change
                weight *= 1

    elif item_unit in combined_liquids:  # ... Then convert liquid weight variable to milliliters
        # imperial to liquid ounces first
        if measure_system == "imperial":
            if item_unit == "cup":
                weight *= 10
            elif item_unit == "pint":
                weight *= 20
            elif item_unit == "quart":
                weight *= 40
            elif item_unit == "gallon":
                weight *= 160
            else:  # Already liquid ounce. No change needed
                weight *= 1
            # Now make it into ml
            weight *= 28.413

    # metric to milliliters
        else:  # It must already be metric then
            if item_unit == "liter":
                weight *= 1000
            else:  # it's milliliter, no need to change
                weight *= 1
    return weight


def conv_liquids(weight, item_unit, measure_system):

    """Unless the user asked for mls, this will convert mls into any other liquid unit"""

    # mls to any imperial unit
    if measure_system == "imperial":
        if item_unit == "liquid ounce":
            weight /= 28.413
        elif item_unit == "cup":
            weight /= 284.1
        elif item_unit == "pint":
            weight /= 568.3
        elif item_unit == "quart":
            weight /= 1137
        elif item_unit == "gallon":
            weight /= 4546
        else:  # Already in ml. No change needed
            weight /= 1

    # mls to any metric unit
    else:  # It must be metric then
        if item_unit == "liter":
            weight /= 1000
        else:  # it's milliliter, no need to change
            weight /= 1
    return weight


def conv_solids(weight, item_unit, measure_system):

    """Unless the user asked for grams, this will convert grams into any other solid unit"""

    # grams to any imperial unit
    if measure_system == "imperial":
        if item_unit == "solid ounce":
            weight /= 28.35
        elif item_unit == "pound":
            weight /= 453.6
        elif item_unit == "stone":
            weight /= 6350
        else:  # Already grams. No change needed
            weight /= 1

    # grams to any metric unit
    else:  # It must be metric then
        if item_unit == "milligram":
            weight /= 0.001
        elif item_unit == "kilogram":
            weight /= 1000
        else:  # it's gram, no need to change
            weight /= 1
    return weight
