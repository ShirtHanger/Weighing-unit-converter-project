# All lists here for conditional statements and input validation

start_prompt_validation = ("yes", "no")

metric_solids = ('gram', 'milligram', 'kilogram')

imperial_solids = ('solid ounce', 'pound', 'stone')

metric_liquids = ('milliliter', 'liter')

imperial_liquids = ('liquid ounce', 'cup', 'pint', 'quart', 'gallon')

accepted_inputs = ('solid', 'liquid')

imperial_units = imperial_liquids + imperial_solids

metric_units = metric_solids + metric_liquids

combined_solids = metric_solids + imperial_solids

combined_liquids = metric_liquids + imperial_liquids
