#  Entry point for project. All user input here

from unit_converter_lists import *
from unit_converter_funcs import *


# Persistent while loop, user can repeat this entire program until they say no
begin = input('Want to convert some stuff? ("Yes" to begin, "No" to quit): ').lower()

while begin not in start_prompt_validation:
    begin = input('Invalid ("Yes" to begin, "No" to quit): ').lower()
while begin != "no":

    #  Determine if the user is weighing a solid or liquid object
    print("-------")
    print("-------")
    print("-------")
    item_type = input("Measure a (solid) or a (liquid): ").lower()
    while item_type not in accepted_inputs:
        item_type = input("Invalid. Again: ").lower()
    
    # This condition determine the original unit using item_type input, then asks user for its weight
    if item_type == "solid":
        display_units(item_type)
        origin_unit = input("What's the original unit: ").lower()
        while origin_unit not in combined_solids:
            origin_unit = input("Invalid. Again: ").lower()
        origin_weight = float(input("Weight of the solid in " + origin_unit + "s: "))

    else:  # the type is liquids
        display_units(item_type)
        origin_unit = input("What's the original unit: ").lower()
        while origin_unit not in combined_liquids:
            origin_unit = input("Invalid. Again: ").lower()
        origin_weight = float(input("Weight of the liquid in " + origin_unit + "s: "))
    
    # Determines if the original unit of measurement is imperial or metric
    measure_system = measure_system_check(origin_unit)
    
    # Takes above variables to convert input to a base unit (ml or grams)
    # Behind the scenes, user is unaware of this
    base_weight = conv_to_base(origin_weight, origin_unit, measure_system)
    
    # Now, asks the user what unit they want their input converted to.
    if item_type == "solid":
        display_units(item_type)
        output_unit = input("What do you want " + str(origin_weight) + " " + origin_unit + "s converted to: ").lower()
        while output_unit not in combined_solids:
            while output_unit == origin_unit:
                output_unit = input("You're already converting " + origin_unit + " to something else. Again:").lower()
            output_unit = input("Invalid. Again: ").lower()

        # Determines if the user wants to convert the original unit to imperial or metric
        measure_system = measure_system_check(output_unit)
        # Takes above variables to convert input to desired output
        converted_weight = conv_solids(base_weight, output_unit, measure_system)
    
    else:  # Then the type is liquid
        display_units(item_type)
        output_unit = input("What do you want " + str(origin_weight) + " " + origin_unit + "s converted to: ").lower()
        while output_unit not in combined_liquids:
            while output_unit == origin_unit:
                output_unit = input("You're already converting " + origin_unit + " to something else. Again:").lower()
            output_unit = input("Invalid. Again: ").lower()

        # Determines if the user wants to convert the original unit to imperial or metric
        measure_system = measure_system_check(output_unit)
        # Takes above variables to convert input to desired output
        converted_weight = conv_liquids(base_weight, output_unit, measure_system)

    # Rounds input and output weights to 2 decimals for easier display

    round(origin_weight, 2)
    round(converted_weight, 2)
    
    # Finally, print out results.
    # Prints the original weight and unit, then the converted weight and unit.

    print("-------")
    print("Original weight:", round(origin_weight, 2), origin_unit + "s")  # Original weight: 150 pounds
    print("Converted weight:", round(converted_weight, 2), output_unit + "s")  # Converted weight: 68.04 kilograms
    print("-------")
    print("Your", item_type, "weighs", round(converted_weight, 2), output_unit + "s!")  # Your solid weighs 68.04 kilograms!
    print("-------")
    print("-------")
    # Asks user if they want to measure something else. If they say "no", end program
    begin = input('Convert something else? ("Yes" to begin, "No" to quit): ').lower()
    while begin not in start_prompt_validation:
        begin = input('Invalid ("Yes" to begin, "No" to quit): ').lower()

print("-------")
print("Alright, see you later")
print("-------")
