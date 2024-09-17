# All lists here for conditional statements and input validation

# Used for input validation of persistent loop
start_prompt_validation = ("yes", "no")

# Used for input validation AND conditional statement branching
accepted_inputs = ('solid', 'liquid')

metric_solids = ('gram', 'milligram', 'kilogram')

imperial_solids = ('solid ounce', 'pound', 'stone')

metric_liquids = ('milliliter', 'liter')

imperial_liquids = ('liquid ounce', 'cup', 'pint', 'quart', 'gallon')

# Combined lists for bulk inclusion of imperial + metric units, as well as all liquids + all solids
# For input validation AND conditional statement branching

imperial_units = imperial_liquids + imperial_solids

metric_units = metric_solids + metric_liquids

combined_solids = metric_solids + imperial_solids

combined_liquids = metric_liquids + imperial_liquids
