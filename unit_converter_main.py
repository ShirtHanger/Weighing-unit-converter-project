#  Entry point for project. All user input here

# IDK why unit_converter_lists is blacked out, it works fine

from unit_converter_lists import *
from unit_converter_funcs import *


# Persistent while loop
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
    
    # Determine the original unit and its weight
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
    
    # The last thing I realized is I needed to re-evaluate this line of code again after converting to base
    # So I decided to make it a function
    measure_system = measure_system_check(origin_unit)
    
    # Takes above arguments to convert input to ml or grams.
    base_weight = conv_to_base(origin_weight, origin_unit, measure_system)
    
    # Now, I ask the user what unit they want their input converted to.
    if item_type == "solid":
        display_units(item_type)
        output_unit = input("What do you want " + str(origin_weight) + " " + origin_unit + "s converted to: ").lower()
        while output_unit not in combined_solids:
            while output_unit == origin_unit:
                output_unit = input("You're converting " + origin_unit + " to something else. Again:").lower()
            output_unit = input("Invalid. Again: ").lower()
        measure_system = measure_system_check(output_unit)
        converted_weight = conv_solids(base_weight, output_unit, measure_system)
    
    else:  # Then the type is liquid
        display_units(item_type)
        output_unit = input("What do you want " + str(origin_weight) + " " + origin_unit + "s converted to: ").lower()
        while output_unit not in combined_liquids:
            output_unit = input("Invalid. Again: ").lower()
        measure_system = measure_system_check(output_unit)
        converted_weight = conv_liquids(base_weight, output_unit, measure_system)

    # Round input and output weights to 2 decimals

    round(origin_weight, 2)
    round(converted_weight, 2)
    
    # Final print statements (With examples)

    print("-------")
    print("Original weight:", round(origin_weight, 2), origin_unit + "s")  # Original weight: 150 pounds
    print("Converted weight:", round(converted_weight, 2), output_unit + "s")  # Converted weight: 68.04 kilograms
    print("-------")
    print("Your", item_type, "weighs", round(converted_weight, 2), output_unit + "s!")  # Your solid weighs 68.04 kilograms!
    print("-------")
    print("-------")
    begin = input('Convert something else? ("Yes" to begin, "No" to quit): ').lower()
    while begin not in start_prompt_validation:
        begin = input('Invalid ("Yes" to begin, "No" to quit): ').lower()

print("-------")
print("Alright, see you later")
print("-------")
